# Research Notes: SEC Filing Workflows Design Agency

## Project Overview
Research and design a specialized agency that designs workflows and systems for accessing SEC filing data using edgartools. The agency will combine AI and non-AI approaches, leveraging both human expertise and AI agents.

## Research Log

### Initial Setup
- Created project folder: sec-filing-workflows-agency
- Started research on 2025-11-11

### EdgarTools Research Findings

**Key Capabilities:**
- Comprehensive SEC data access (filings back to 1994)
- 10-30x faster than alternatives (lxml & PyArrow optimized)
- Built specifically for AI agents and LLMs
- Production-ready MCP server included
- Supports: 10-K, 10-Q, 8-K, Forms 3/4/5, 13F-HR
- XBRL financial statement extraction
- Automatic throttling to prevent SEC blocks
- Text chunking for vector embeddings
- Output formats: DataFrames, Objects, Clean Text

**Unique Advantages:**
- Only SEC EDGAR library built from ground up for AI agents
- 1000+ tests, type hints, battle-tested
- Simple API (3 lines vs 100+)
- MIT license, open source

### Market Use Cases Identified

**Traditional Workflows:**
1. Financial statement extraction and benchmarking
2. Risk assessment and management (10-K risk factors)
3. Investment decision-making and due diligence
4. Insider trading tracking (Forms 3/4/5)
5. Fund holdings analysis (13F-HR)
6. Regulatory compliance monitoring

**AI-Enhanced Workflows (2025 Trends):**
1. Automated earnings call preparation
2. Risk factor identification and drafting
3. MD&A summarization for audit committees
4. Debt agreement analysis and term extraction
5. Real-time filing analysis (RBC's Aiden example)
6. Multi-source financial modeling
7. Automated three-statement model generation

**Key Market Trend:**
2025 represents significant shift toward AI-powered automation in SEC filing analysis. Companies like RBC using orchestration agents with specialized SEC filing agents.

### AI Agent Orchestration Research

**Orchestration Patterns:**
- Multi-agent systems with specialized agents (SEC filing agent, earnings agent, news agent)
- LangChain for building chains of LLM calls
- LangGraph for complex workflows and state management
- Graph-based visual workflow modeling

**Compliance & Governance:**
- Compliance gateways for automated validation
- Full audit logging (queries, data accessed, tokens, evaluations)
- SEC and FINRA regulatory tracking
- Encrypted, immutable audit trails

**Real-World Examples:**
- RBC's Aiden platform with agent orchestration
- Claude 3.5 Sonnet-powered financial analysis agents
- Portfolio advisory, bookkeeping, fraud detection agents

### Target Market Segments

1. **Investment Firms & Hedge Funds**
   - Due diligence workflows
   - Real-time filing alerts
   - Multi-company comparisons

2. **Corporate Finance Teams**
   - Competitor analysis
   - Benchmark reporting
   - Risk factor monitoring

3. **Compliance & Legal Teams**
   - Regulatory change tracking
   - Disclosure analysis
   - Audit trail generation

4. **Financial Research Firms**
   - Custom data extraction
   - Industry trend analysis
   - Historical data mining

5. **Fintech Companies**
   - API integration workflows
   - Automated reporting systems
   - Data pipeline design

### Example Workflows Created

Created three production-ready workflow examples:

1. **Classic ETL Workflow** (example_classic_etl.py)
   - Non-AI approach
   - Financial statement extraction
   - Data warehouse loading
   - Scheduled execution pattern
   - Use case: Regular reporting & benchmarking

2. **AI-Augmented Risk Analysis** (example_ai_risk_analysis.py)
   - Single-agent AI workflow
   - Risk factor extraction and analysis
   - Claude-powered categorization
   - Structured outputs with audit logs
   - Use case: Investment analyst research

3. **Multi-Agent Orchestration** (example_multi_agent.py)
   - LangGraph state machine
   - 4 specialized agents: SEC Filing, Financial Analysis, Synthesis, Compliance
   - Comprehensive due diligence workflow
   - Full compliance and audit trail
   - Use case: M&A due diligence

### Key Technical Learnings

**When to Use AI vs Non-AI:**
- Deterministic tasks (XBRL parsing, financial ratios) → No AI needed
- Natural language understanding (risk summaries, MD&A) → AI beneficial
- Judgment and synthesis (recommendations, trend interpretation) → AI valuable
- Data validation and compliance checks → Deterministic rules preferred

**Workflow Pattern Selection:**
- Simple, scheduled data extraction → Classic ETL
- Real-time alerts → Event-driven pattern
- Deep analysis of text → AI-augmented single agent
- Complex multi-source synthesis → Multi-agent orchestration
- Batch processing → Distributed worker pool

**edgartools Best Practices:**
- Built-in throttling respects SEC rate limits
- Cache filings to avoid repeated requests
- Text chunking feature ready for LLM processing
- XBRL parsing is deterministic and reliable
- Works well with both traditional and AI workflows

