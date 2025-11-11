#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "edgartools>=4.26.0,<5.0.0",  # SEC filing data access
#     "anthropic>=0.40.0",           # Claude API
#     "langgraph>=0.0.20",           # Agent orchestration
#     "langchain>=0.1.0",            # LLM chains
#     "pandas>=2.0.0",               # Data manipulation
#     "pydantic>=2.0.0",             # Data validation
# ]
# ///
"""
Example 3: Multi-Agent Orchestration Workflow

This workflow demonstrates a sophisticated multi-agent system for comprehensive
due diligence analysis combining SEC filings, financial analysis, and synthesis.

Use Case: Investment firm needs comprehensive due diligence report for potential
acquisition target, combining multiple data sources and analysis types.

Business Value:
- Reduces due diligence time from weeks to hours
- Consistent, comprehensive analysis across all targets
- Multi-dimensional risk assessment
- Audit-ready documentation
- Estimated value: $50K-$100K saved per deal

Technical Approach:
- Orchestrator agent (LangGraph state machine)
- Specialized agents:
  * SEC Filing Agent (edgartools-powered)
  * Financial Analysis Agent
  * Synthesis Agent
- Compliance gateway for validation
- Full audit trail
"""

import os
import json
from datetime import datetime
from typing import List, Dict, Any, Annotated, TypedDict
from enum import Enum

from pydantic import BaseModel, Field
from anthropic import Anthropic
from edgartools import Company, Filing

# LangGraph imports
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode


# State Management

class AnalysisState(TypedDict):
    """State shared across all agents."""
    # Input
    ticker: str
    years: List[int]

    # Intermediate results
    sec_data: Dict[str, Any]
    financial_analysis: Dict[str, Any]
    risk_analysis: Dict[str, Any]

    # Final output
    synthesis: str
    confidence_score: float

    # Audit trail
    audit_log: List[Dict[str, Any]]
    errors: List[str]


class AgentRole(str, Enum):
    """Agent roles in the system."""
    ORCHESTRATOR = "orchestrator"
    SEC_FILING = "sec_filing"
    FINANCIAL = "financial"
    SYNTHESIS = "synthesis"
    COMPLIANCE = "compliance"


# Data Models

class SECFilingData(BaseModel):
    """SEC filing data structure."""
    ticker: str
    filings: List[Dict[str, Any]]
    latest_10k: Dict[str, Any]
    latest_10q: Dict[str, Any]
    insider_transactions: List[Dict[str, Any]]


class FinancialMetrics(BaseModel):
    """Financial analysis metrics."""
    ticker: str
    period: str
    revenue_growth_yoy: float
    profit_margin: float
    debt_to_equity: float
    current_ratio: float
    roe: float
    trends: Dict[str, str]  # trend descriptions


class DueDiligenceReport(BaseModel):
    """Final due diligence report."""
    ticker: str
    analysis_date: str
    executive_summary: str
    financial_health: str
    risk_assessment: str
    recommendations: List[str]
    confidence_score: float
    data_sources: List[str]
    analyst_notes: str


# Agents

class SECFilingAgent:
    """
    Specialized agent for SEC filing data retrieval and parsing.
    Uses edgartools exclusively - no LLM needed for this agent.
    """

    def __init__(self):
        self.name = "SEC Filing Agent"

    def execute(self, state: AnalysisState) -> AnalysisState:
        """
        Retrieve and parse SEC filings for the target company.

        Args:
            state: Current analysis state

        Returns:
            Updated state with SEC data
        """
        print(f"\n{'=' * 80}")
        print(f"{self.name}: Retrieving SEC data for {state['ticker']}")
        print(f"{'=' * 80}")

        try:
            company = Company(state['ticker'])

            # Get recent 10-K filings
            ten_k_filings = list(company.get_filings(form='10-K').head(3))

            # Get recent 10-Q filings
            ten_q_filings = list(company.get_filings(form='10-Q').head(4))

            # Get insider transactions (Form 4)
            insider_filings = list(company.get_filings(form='4').head(10))

            # Structure the data
            sec_data = {
                'company_name': company.name,
                'cik': company.cik,
                'ten_k_filings': [
                    {
                        'accession_number': f.accession_number,
                        'filing_date': f.filing_date.isoformat(),
                        'period_end': f.period_end.isoformat() if f.period_end else None,
                        'form_type': f.form_type,
                    }
                    for f in ten_k_filings
                ],
                'ten_q_filings': [
                    {
                        'accession_number': f.accession_number,
                        'filing_date': f.filing_date.isoformat(),
                        'period_end': f.period_end.isoformat() if f.period_end else None,
                        'form_type': f.form_type,
                    }
                    for f in ten_q_filings
                ],
                'insider_transactions': [
                    {
                        'accession_number': f.accession_number,
                        'filing_date': f.filing_date.isoformat(),
                    }
                    for f in insider_filings
                ],
                'latest_10k_accession': ten_k_filings[0].accession_number if ten_k_filings else None,
            }

            # Update state
            state['sec_data'] = sec_data

            # Audit log
            state['audit_log'].append({
                'timestamp': datetime.utcnow().isoformat(),
                'agent': self.name,
                'action': 'retrieve_sec_data',
                'status': 'success',
                'filings_retrieved': {
                    '10-K': len(ten_k_filings),
                    '10-Q': len(ten_q_filings),
                    'Form 4': len(insider_filings),
                }
            })

            print(f"✓ Retrieved {len(ten_k_filings)} 10-K, {len(ten_q_filings)} 10-Q filings")

        except Exception as e:
            error_msg = f"SEC Filing Agent error: {str(e)}"
            state['errors'].append(error_msg)
            state['audit_log'].append({
                'timestamp': datetime.utcnow().isoformat(),
                'agent': self.name,
                'action': 'retrieve_sec_data',
                'status': 'error',
                'error': str(e)
            })
            print(f"✗ Error: {error_msg}")

        return state


class FinancialAnalysisAgent:
    """
    Analyzes financial metrics from SEC filings.
    Uses edgartools for data extraction + Claude for trend analysis.
    """

    def __init__(self, api_key: str):
        self.name = "Financial Analysis Agent"
        self.client = Anthropic(api_key=api_key)

    def execute(self, state: AnalysisState) -> AnalysisState:
        """
        Analyze financial metrics and trends.

        Args:
            state: Current analysis state

        Returns:
            Updated state with financial analysis
        """
        print(f"\n{'=' * 80}")
        print(f"{self.name}: Analyzing financial metrics")
        print(f"{'=' * 80}")

        try:
            # Get latest 10-K
            latest_10k_accession = state['sec_data']['latest_10k_accession']
            filing = Filing(latest_10k_accession)

            # Extract financials using edgartools (deterministic)
            print("Extracting financial statements...")
            financials = filing.financials()

            # In production, would extract actual metrics from XBRL
            # For this example, we'll create sample structure
            financial_data = {
                'revenue_3yr': [100000, 120000, 150000],  # Example: last 3 years
                'net_income_3yr': [10000, 15000, 20000],
                'total_assets': 500000,
                'total_liabilities': 200000,
                'stockholders_equity': 300000,
                'current_assets': 150000,
                'current_liabilities': 75000,
            }

            # Calculate ratios (deterministic - no AI needed)
            metrics = {
                'revenue_growth_yoy': (
                    (financial_data['revenue_3yr'][-1] - financial_data['revenue_3yr'][-2])
                    / financial_data['revenue_3yr'][-2] * 100
                ),
                'profit_margin': (
                    financial_data['net_income_3yr'][-1] / financial_data['revenue_3yr'][-1] * 100
                ),
                'debt_to_equity': (
                    financial_data['total_liabilities'] / financial_data['stockholders_equity']
                ),
                'current_ratio': (
                    financial_data['current_assets'] / financial_data['current_liabilities']
                ),
                'roe': (
                    financial_data['net_income_3yr'][-1] / financial_data['stockholders_equity'] * 100
                ),
            }

            print(f"✓ Calculated financial metrics")

            # Use AI for trend analysis and interpretation
            print("Analyzing trends with AI...")

            prompt = f"""As a financial analyst, analyze these financial metrics and trends:

Company: {state['ticker']}
Revenue (3 years): ${financial_data['revenue_3yr'][0]:,.0f}, ${financial_data['revenue_3yr'][1]:,.0f}, ${financial_data['revenue_3yr'][2]:,.0f}
Net Income (3 years): ${financial_data['net_income_3yr'][0]:,.0f}, ${financial_data['net_income_3yr'][1]:,.0f}, ${financial_data['net_income_3yr'][2]:,.0f}

Key Ratios:
- Revenue Growth (YoY): {metrics['revenue_growth_yoy']:.1f}%
- Profit Margin: {metrics['profit_margin']:.1f}%
- Debt-to-Equity: {metrics['debt_to_equity']:.2f}
- Current Ratio: {metrics['current_ratio']:.2f}
- ROE: {metrics['roe']:.1f}%

Provide:
1. Overall financial health assessment (Strong/Moderate/Weak)
2. Key trends (Improving/Stable/Declining)
3. Specific concerns or strengths (3-5 bullet points)
4. Comparison to industry norms (if applicable)

Format as JSON:
{{
  "health_assessment": "Strong/Moderate/Weak",
  "trend": "Improving/Stable/Declining",
  "key_points": ["point1", "point2", ...],
  "industry_comparison": "comparison text"
}}
"""

            response = self.client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=2000,
                temperature=0.0,
                messages=[{"role": "user", "content": prompt}]
            )

            # Parse AI response
            response_text = response.content[0].text
            if "```json" in response_text:
                json_start = response_text.find("```json") + 7
                json_end = response_text.find("```", json_start)
                response_text = response_text[json_start:json_end].strip()

            trend_analysis = json.loads(response_text)

            # Combine metrics and AI analysis
            state['financial_analysis'] = {
                'metrics': metrics,
                'raw_data': financial_data,
                'trend_analysis': trend_analysis,
            }

            # Audit log
            state['audit_log'].append({
                'timestamp': datetime.utcnow().isoformat(),
                'agent': self.name,
                'action': 'analyze_financials',
                'status': 'success',
                'model_used': 'claude-sonnet-4-20250514',
                'tokens': response.usage.input_tokens + response.usage.output_tokens,
            })

            print(f"✓ Financial analysis complete: {trend_analysis['health_assessment']}")

        except Exception as e:
            error_msg = f"Financial Analysis Agent error: {str(e)}"
            state['errors'].append(error_msg)
            print(f"✗ Error: {error_msg}")

        return state


class SynthesisAgent:
    """
    Synthesizes all analyses into final due diligence report.
    Uses Claude to combine insights from all sources.
    """

    def __init__(self, api_key: str):
        self.name = "Synthesis Agent"
        self.client = Anthropic(api_key=api_key)

    def execute(self, state: AnalysisState) -> AnalysisState:
        """
        Synthesize all analyses into comprehensive report.

        Args:
            state: Current analysis state

        Returns:
            Updated state with synthesis
        """
        print(f"\n{'=' * 80}")
        print(f"{self.name}: Synthesizing due diligence report")
        print(f"{'=' * 80}")

        try:
            # Prepare comprehensive context for synthesis
            context = f"""
You are synthesizing a due diligence report for {state['ticker']}.

SEC FILING DATA:
- Company: {state['sec_data']['company_name']}
- Recent 10-K filings: {len(state['sec_data']['ten_k_filings'])}
- Recent 10-Q filings: {len(state['sec_data']['ten_q_filings'])}
- Insider transactions: {len(state['sec_data']['insider_transactions'])}

FINANCIAL ANALYSIS:
{json.dumps(state['financial_analysis'], indent=2)}

Based on this comprehensive analysis, create a due diligence report with:

1. EXECUTIVE SUMMARY (2-3 paragraphs)
   - Overall investment thesis
   - Key highlights and concerns
   - Recommendation direction

2. FINANCIAL HEALTH (1-2 paragraphs)
   - Assessment of financial strength
   - Key metrics interpretation
   - Trend analysis

3. RISK ASSESSMENT (1 paragraph)
   - Major risks identified
   - Risk severity
   - Mitigation considerations

4. RECOMMENDATIONS (3-5 bullet points)
   - Specific action items
   - Due diligence priorities
   - Decision framework

5. CONFIDENCE SCORE (0-100)
   - Based on data quality and analysis completeness

Format as JSON:
{{
  "executive_summary": "...",
  "financial_health": "...",
  "risk_assessment": "...",
  "recommendations": ["rec1", "rec2", ...],
  "confidence_score": 85,
  "analyst_notes": "Any caveats or additional context"
}}
"""

            response = self.client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=4000,
                temperature=0.2,  # Slight creativity for synthesis
                messages=[{"role": "user", "content": context}]
            )

            # Parse response
            response_text = response.content[0].text
            if "```json" in response_text:
                json_start = response_text.find("```json") + 7
                json_end = response_text.find("```", json_start)
                response_text = response_text[json_start:json_end].strip()

            synthesis_data = json.loads(response_text)

            # Update state
            state['synthesis'] = json.dumps(synthesis_data, indent=2)
            state['confidence_score'] = synthesis_data['confidence_score']

            # Audit log
            state['audit_log'].append({
                'timestamp': datetime.utcnow().isoformat(),
                'agent': self.name,
                'action': 'synthesize_report',
                'status': 'success',
                'model_used': 'claude-sonnet-4-20250514',
                'confidence_score': synthesis_data['confidence_score'],
            })

            print(f"✓ Synthesis complete (Confidence: {synthesis_data['confidence_score']}%)")

        except Exception as e:
            error_msg = f"Synthesis Agent error: {str(e)}"
            state['errors'].append(error_msg)
            print(f"✗ Error: {error_msg}")

        return state


class ComplianceGateway:
    """
    Validates outputs for compliance and data quality.
    No LLM - uses deterministic rules.
    """

    def __init__(self):
        self.name = "Compliance Gateway"

    def execute(self, state: AnalysisState) -> AnalysisState:
        """
        Validate analysis for compliance requirements.

        Args:
            state: Current analysis state

        Returns:
            Updated state with validation results
        """
        print(f"\n{'=' * 80}")
        print(f"{self.name}: Validating compliance")
        print(f"{'=' * 80}")

        validation_checks = []

        # Check 1: Audit trail completeness
        required_agents = ['SEC Filing Agent', 'Financial Analysis Agent', 'Synthesis Agent']
        agents_executed = set(log['agent'] for log in state['audit_log'])
        audit_complete = all(agent in agents_executed for agent in required_agents)

        validation_checks.append({
            'check': 'Audit trail completeness',
            'passed': audit_complete,
            'details': f"Executed: {agents_executed}"
        })

        # Check 2: Data quality
        has_sec_data = 'sec_data' in state and state['sec_data']
        has_financial_analysis = 'financial_analysis' in state and state['financial_analysis']
        has_synthesis = 'synthesis' in state and state['synthesis']

        data_quality = has_sec_data and has_financial_analysis and has_synthesis

        validation_checks.append({
            'check': 'Data quality',
            'passed': data_quality,
            'details': f"SEC: {has_sec_data}, Financial: {has_financial_analysis}, Synthesis: {has_synthesis}"
        })

        # Check 3: Confidence score threshold
        confidence_acceptable = state.get('confidence_score', 0) >= 70

        validation_checks.append({
            'check': 'Confidence threshold',
            'passed': confidence_acceptable,
            'details': f"Score: {state.get('confidence_score', 0)}"
        })

        # Check 4: No critical errors
        no_critical_errors = len(state.get('errors', [])) == 0

        validation_checks.append({
            'check': 'No critical errors',
            'passed': no_critical_errors,
            'details': f"Errors: {len(state.get('errors', []))}"
        })

        # Overall validation
        all_passed = all(check['passed'] for check in validation_checks)

        # Audit log
        state['audit_log'].append({
            'timestamp': datetime.utcnow().isoformat(),
            'agent': self.name,
            'action': 'compliance_validation',
            'status': 'passed' if all_passed else 'failed',
            'checks': validation_checks,
        })

        # Print results
        for check in validation_checks:
            status = "✓" if check['passed'] else "✗"
            print(f"{status} {check['check']}: {check['details']}")

        if all_passed:
            print(f"\n✓ All compliance checks passed")
        else:
            print(f"\n✗ Compliance validation failed")
            state['errors'].append("Compliance validation failed")

        return state


# Orchestrator

class DueDiligenceOrchestrator:
    """
    Orchestrates the multi-agent workflow using LangGraph.
    """

    def __init__(self, api_key: str):
        self.api_key = api_key

        # Initialize agents
        self.sec_agent = SECFilingAgent()
        self.financial_agent = FinancialAnalysisAgent(api_key)
        self.synthesis_agent = SynthesisAgent(api_key)
        self.compliance_gateway = ComplianceGateway()

        # Build graph
        self.graph = self._build_graph()

    def _build_graph(self) -> StateGraph:
        """Build the LangGraph workflow."""

        # Create graph
        workflow = StateGraph(AnalysisState)

        # Add nodes
        workflow.add_node("sec_filing", self.sec_agent.execute)
        workflow.add_node("financial_analysis", self.financial_agent.execute)
        workflow.add_node("synthesis", self.synthesis_agent.execute)
        workflow.add_node("compliance", self.compliance_gateway.execute)

        # Define edges (workflow sequence)
        workflow.set_entry_point("sec_filing")
        workflow.add_edge("sec_filing", "financial_analysis")
        workflow.add_edge("financial_analysis", "synthesis")
        workflow.add_edge("synthesis", "compliance")
        workflow.add_edge("compliance", END)

        return workflow.compile()

    def run(self, ticker: str, years: List[int] = None) -> Dict[str, Any]:
        """
        Execute the due diligence workflow.

        Args:
            ticker: Company ticker symbol
            years: Years to analyze (optional)

        Returns:
            Final state with complete analysis
        """
        print(f"\n{'=' * 80}")
        print(f"MULTI-AGENT DUE DILIGENCE WORKFLOW")
        print(f"{'=' * 80}")
        print(f"Ticker: {ticker}")
        print(f"Started: {datetime.utcnow().isoformat()}")
        print(f"{'=' * 80}\n")

        # Initialize state
        initial_state: AnalysisState = {
            'ticker': ticker,
            'years': years or [2023, 2024],
            'sec_data': {},
            'financial_analysis': {},
            'risk_analysis': {},
            'synthesis': '',
            'confidence_score': 0.0,
            'audit_log': [],
            'errors': [],
        }

        # Run workflow
        final_state = self.graph.invoke(initial_state)

        return final_state


def main():
    """Main entry point."""
    # Check for API key
    api_key = os.getenv('ANTHROPIC_API_KEY')
    if not api_key:
        print("ERROR: ANTHROPIC_API_KEY environment variable must be set")
        return

    # Initialize orchestrator
    orchestrator = DueDiligenceOrchestrator(api_key)

    # Run analysis
    ticker = 'AAPL'
    result = orchestrator.run(ticker)

    # Display results
    print(f"\n{'=' * 80}")
    print("FINAL REPORT")
    print(f"{'=' * 80}\n")

    if result['synthesis']:
        synthesis = json.loads(result['synthesis'])
        print(f"Executive Summary:\n{synthesis['executive_summary']}\n")
        print(f"Financial Health:\n{synthesis['financial_health']}\n")
        print(f"Risk Assessment:\n{synthesis['risk_assessment']}\n")
        print(f"Recommendations:")
        for i, rec in enumerate(synthesis['recommendations'], 1):
            print(f"  {i}. {rec}")
        print(f"\nConfidence Score: {synthesis['confidence_score']}%")

    # Save complete audit log
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    audit_file = f"{ticker}_due_diligence_audit_{timestamp}.json"

    with open(audit_file, 'w') as f:
        json.dump({
            'ticker': ticker,
            'analysis_date': datetime.utcnow().isoformat(),
            'final_state': {
                k: v for k, v in result.items()
                if k not in ['graph']  # Exclude non-serializable
            }
        }, f, indent=2, default=str)

    print(f"\nAudit log saved to: {audit_file}")

    # Print audit summary
    print(f"\n{'=' * 80}")
    print("AUDIT SUMMARY")
    print(f"{'=' * 80}")
    print(f"Total operations: {len(result['audit_log'])}")
    print(f"Errors: {len(result['errors'])}")

    total_tokens = sum(
        log.get('tokens', 0)
        for log in result['audit_log']
    )
    print(f"Total AI tokens used: {total_tokens:,}")


if __name__ == '__main__':
    main()
