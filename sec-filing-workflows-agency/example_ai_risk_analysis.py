#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "edgartools>=4.26.0,<5.0.0",  # SEC filing data access
#     "anthropic>=0.40.0",           # Claude API
#     "pandas>=2.0.0",               # Data manipulation
#     "pydantic>=2.0.0",             # Data validation
# ]
# ///
"""
Example 2: AI-Augmented Risk Factor Analysis (Single Agent)

This workflow demonstrates using AI (Claude) to analyze and summarize risk
factors from SEC 10-K filings.

Use Case: Investment analysts need to quickly understand and compare risk
factors across portfolio companies to identify emerging risks.

Business Value:
- Saves 2-3 hours per company (from manual reading)
- Consistent risk categorization
- Identifies emerging themes across multiple filings
- Generates actionable summaries for investment committee

Technical Approach:
- edgartools for filing extraction and text chunking
- Claude for natural language understanding
- Structured output for downstream processing
- Full audit trail for compliance
"""

import os
import json
from datetime import datetime
from typing import List, Dict, Optional
from pydantic import BaseModel, Field
from anthropic import Anthropic
from edgartools import Company, Filing


# Data Models for Structured Output

class RiskCategory(BaseModel):
    """Structured risk category."""
    name: str = Field(description="Risk category name (e.g., 'Market Risk', 'Regulatory Risk')")
    severity: str = Field(description="Severity: Low, Medium, High, Critical")
    summary: str = Field(description="Brief summary of the risk")
    key_points: List[str] = Field(description="Key specific risk factors")


class RiskAnalysis(BaseModel):
    """Complete risk analysis for a filing."""
    ticker: str
    filing_date: str
    accession_number: str
    categories: List[RiskCategory]
    overall_assessment: str = Field(description="Overall risk assessment summary")
    year_over_year_changes: Optional[str] = Field(
        None,
        description="Notable changes from previous year (if available)"
    )


class AuditLog(BaseModel):
    """Audit log for compliance."""
    timestamp: str
    ticker: str
    accession_number: str
    model_used: str
    prompt_tokens: int
    completion_tokens: int
    total_cost: float
    analysis: RiskAnalysis


class RiskFactorAnalyzer:
    """AI-powered risk factor analyzer."""

    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize analyzer.

        Args:
            api_key: Anthropic API key (or set ANTHROPIC_API_KEY env var)
        """
        self.api_key = api_key or os.getenv('ANTHROPIC_API_KEY')
        if not self.api_key:
            raise ValueError("ANTHROPIC_API_KEY must be set")

        self.client = Anthropic(api_key=self.api_key)
        self.audit_logs: List[AuditLog] = []

    def extract_risk_section(self, filing: Filing) -> str:
        """
        Extract the risk factors section from a 10-K filing.

        Args:
            filing: SEC Filing object

        Returns:
            Text of risk factors section
        """
        print(f"Extracting risk factors from {filing.company} {filing.filing_date}...")

        # In production, would use edgartools to extract specific sections
        # For this example, we'll use a simplified approach
        full_text = filing.text()

        # Find "Risk Factors" section (Item 1A in 10-K)
        # This is simplified - production would use proper section parsing
        risk_start = full_text.find("Item 1A")
        if risk_start == -1:
            risk_start = full_text.find("Risk Factors")

        if risk_start == -1:
            raise ValueError("Could not find Risk Factors section")

        # Find end of section (next Item or reasonable limit)
        risk_end = full_text.find("Item 1B", risk_start)
        if risk_end == -1:
            risk_end = risk_start + 50000  # Reasonable limit

        risk_text = full_text[risk_start:risk_end]

        return risk_text[:50000]  # Limit for context window

    def analyze_risks(self, ticker: str, year: int) -> RiskAnalysis:
        """
        Analyze risk factors using AI.

        Args:
            ticker: Company ticker symbol
            year: Year of filing to analyze

        Returns:
            Structured risk analysis
        """
        # Get filing
        company = Company(ticker)
        filings = company.get_filings(form='10-K', year=year)
        filing = list(filings)[0]

        # Extract risk section
        risk_text = self.extract_risk_section(filing)

        # Analyze with Claude
        print(f"Analyzing risk factors with AI...")

        prompt = f"""You are a financial analyst reviewing SEC 10-K filings. Analyze the risk factors section below and provide a structured analysis.

Risk Factors Section:
{risk_text}

Please provide:
1. Categorize the risks into major categories (e.g., Market Risk, Operational Risk, Regulatory Risk, etc.)
2. For each category, assess severity (Low, Medium, High, Critical)
3. Summarize each risk category
4. List 3-5 key specific points for each category
5. Provide an overall risk assessment

Format your response as JSON matching this structure:
{{
  "categories": [
    {{
      "name": "Category Name",
      "severity": "High",
      "summary": "Brief summary...",
      "key_points": ["Point 1", "Point 2", "Point 3"]
    }}
  ],
  "overall_assessment": "Overall assessment summary..."
}}
"""

        # Call Claude
        response = self.client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=4000,
            temperature=0.0,  # Deterministic for consistency
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        # Parse response
        response_text = response.content[0].text

        # Extract JSON from response (might be wrapped in markdown)
        if "```json" in response_text:
            json_start = response_text.find("```json") + 7
            json_end = response_text.find("```", json_start)
            response_text = response_text[json_start:json_end].strip()
        elif "```" in response_text:
            json_start = response_text.find("```") + 3
            json_end = response_text.find("```", json_start)
            response_text = response_text[json_start:json_end].strip()

        analysis_data = json.loads(response_text)

        # Create structured analysis
        analysis = RiskAnalysis(
            ticker=ticker,
            filing_date=filing.filing_date.isoformat(),
            accession_number=filing.accession_number,
            categories=[
                RiskCategory(**cat) for cat in analysis_data['categories']
            ],
            overall_assessment=analysis_data['overall_assessment']
        )

        # Create audit log
        audit_log = AuditLog(
            timestamp=datetime.utcnow().isoformat(),
            ticker=ticker,
            accession_number=filing.accession_number,
            model_used="claude-sonnet-4-20250514",
            prompt_tokens=response.usage.input_tokens,
            completion_tokens=response.usage.output_tokens,
            total_cost=self._calculate_cost(response.usage),
            analysis=analysis
        )

        self.audit_logs.append(audit_log)

        return analysis

    def _calculate_cost(self, usage) -> float:
        """Calculate cost based on token usage."""
        # Claude Sonnet pricing (as of 2024)
        input_cost = (usage.input_tokens / 1_000_000) * 3.00
        output_cost = (usage.output_tokens / 1_000_000) * 15.00
        return input_cost + output_cost

    def compare_risks(
        self,
        ticker: str,
        years: List[int]
    ) -> Dict[str, RiskAnalysis]:
        """
        Compare risk factors across multiple years.

        Args:
            ticker: Company ticker symbol
            years: List of years to compare

        Returns:
            Dictionary of year -> RiskAnalysis
        """
        analyses = {}

        for year in years:
            analysis = self.analyze_risks(ticker, year)
            analyses[str(year)] = analysis

        return analyses

    def generate_report(
        self,
        analyses: Dict[str, RiskAnalysis],
        output_file: str = None
    ) -> str:
        """
        Generate a human-readable report.

        Args:
            analyses: Dictionary of analyses
            output_file: Optional file to save report to

        Returns:
            Report text
        """
        report_lines = []
        report_lines.append("=" * 80)
        report_lines.append("SEC 10-K RISK FACTOR ANALYSIS")
        report_lines.append("=" * 80)
        report_lines.append("")

        for year, analysis in sorted(analyses.items()):
            report_lines.append(f"\n{analysis.ticker} - {year}")
            report_lines.append("-" * 80)
            report_lines.append(f"Filing Date: {analysis.filing_date}")
            report_lines.append(f"Accession: {analysis.accession_number}")
            report_lines.append("")

            report_lines.append("Risk Categories:")
            for cat in analysis.categories:
                report_lines.append(f"\n  {cat.name} (Severity: {cat.severity})")
                report_lines.append(f"  {cat.summary}")
                report_lines.append("  Key Points:")
                for point in cat.key_points:
                    report_lines.append(f"    - {point}")

            report_lines.append(f"\nOverall Assessment:")
            report_lines.append(f"  {analysis.overall_assessment}")
            report_lines.append("")

        # Add audit summary
        report_lines.append("\n" + "=" * 80)
        report_lines.append("AUDIT SUMMARY")
        report_lines.append("=" * 80)
        total_tokens = sum(log.prompt_tokens + log.completion_tokens for log in self.audit_logs)
        total_cost = sum(log.total_cost for log in self.audit_logs)
        report_lines.append(f"Total API calls: {len(self.audit_logs)}")
        report_lines.append(f"Total tokens: {total_tokens:,}")
        report_lines.append(f"Total cost: ${total_cost:.4f}")

        report = "\n".join(report_lines)

        if output_file:
            with open(output_file, 'w') as f:
                f.write(report)
            print(f"Report saved to {output_file}")

        return report

    def save_audit_logs(self, output_file: str) -> None:
        """Save audit logs to JSON file."""
        with open(output_file, 'w') as f:
            json.dump(
                [log.model_dump() for log in self.audit_logs],
                f,
                indent=2
            )
        print(f"Audit logs saved to {output_file}")


def main():
    """Main entry point."""
    # Check for API key
    if not os.getenv('ANTHROPIC_API_KEY'):
        print("ERROR: ANTHROPIC_API_KEY environment variable must be set")
        print("Example: export ANTHROPIC_API_KEY='your-api-key'")
        return

    # Initialize analyzer
    analyzer = RiskFactorAnalyzer()

    # Analyze single company across multiple years
    ticker = 'AAPL'
    years = [2023, 2024]

    print(f"Analyzing {ticker} risk factors for {years}...")
    analyses = analyzer.compare_risks(ticker, years)

    # Generate report
    report = analyzer.generate_report(
        analyses,
        output_file=f'{ticker}_risk_analysis_{datetime.now().strftime("%Y%m%d")}.txt'
    )

    # Save audit logs
    analyzer.save_audit_logs(
        f'{ticker}_risk_audit_{datetime.now().strftime("%Y%m%d")}.json'
    )

    # Display report
    print("\n" + report)


if __name__ == '__main__':
    main()
