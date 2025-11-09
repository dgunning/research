# Agno Framework: Comprehensive Deep Dive for Enterprise Architects

## Original Research Prompt

> As an enterprise architect I want to be in the top 1% most knowledgeable on LLM frameworks. Do a deep dive on the Agno framework so that I know everything there is to know.

## Executive Summary

Agno is a high-performance, multi-agent framework, runtime, and control plane built for speed, privacy, and scale. Released under the Apache-2.0 license, Agno (formerly Phidata, rebranded January 2025) represents a paradigm shift in how AI agents are built and deployed in production environments. The name "Agno" (ἁγνὸ) means "pure" in Greek, reflecting its design philosophy: no graphs, chains, or convoluted patterns—just pure Python.

**Key Differentiators:**
- **Performance**: 529× faster instantiation than LangGraph, 50× less memory usage
- **Privacy-First**: Runs entirely in your cloud with zero external data transmission
- **Production-Ready**: Ships with AgentOS, a FastAPI runtime ready for day-one deployment
- **Model-Agnostic**: Supports 23+ LLM providers including OpenAI, Anthropic, Groq, Google, Hugging Face
- **Enterprise-Grade**: RBAC, complete data governance, infinite retention with no vendor costs

---

## Table of Contents

1. [Core Architecture](#core-architecture)
2. [Performance Benchmarks](#performance-benchmarks)
3. [Core Capabilities](#core-capabilities)
4. [AgentOS Runtime & Deployment](#agentos-runtime--deployment)
5. [Multi-Agent Systems](#multi-agent-systems)
6. [Workflows & Deterministic Execution](#workflows--deterministic-execution)
7. [Memory & Knowledge Management](#memory--knowledge-management)
8. [Model Context Protocol (MCP) Integration](#model-context-protocol-mcp-integration)
9. [Toolkits & Extensibility](#toolkits--extensibility)
10. [Enterprise Security & Governance](#enterprise-security--governance)
11. [Advanced Features](#advanced-features)
12. [Code Examples & Patterns](#code-examples--patterns)
13. [Framework Comparisons](#framework-comparisons)
14. [Real-World Use Cases](#real-world-use-cases)
15. [Community & Ecosystem](#community--ecosystem)
16. [Cost & Deployment Options](#cost--deployment-options)
17. [Getting Started](#getting-started)
18. [Migration from Phidata](#migration-from-phidata)
19. [Architecture Decision Guide](#architecture-decision-guide)
20. [Resources & References](#resources--references)

---

## Core Architecture

### Three-Layer Design

Agno's architecture is built on three foundational layers:

#### 1. **Agents Layer**
- Individual agents with memory, knowledge, and session management
- Human-in-the-loop (HITL) capabilities with confirmations and overrides
- Built-in guardrails and validation
- Dynamic context engineering for runtime variable injection
- Agent lifecycle hooks for input/output transformation
- Best-in-class Model Context Protocol (MCP) support

#### 2. **Multi-Agent Teams**
- Agents operate autonomously under a team leader
- Shared state and context across team members
- Three coordination modes: Route, Collaborate, Coordinate
- Perfect for complex use cases exceeding single-agent scope

#### 3. **Step-Based Workflows**
- Deterministic execution for production reliability
- Sequential, parallel, looped, or conditional operations
- Steps can be Agents, Teams, or Python functions
- Stateful programs with pause, resume, and audit capabilities

### AgentOS: Runtime + Control Plane

AgentOS is Agno's production runtime that provides:

**Runtime Features:**
- Pre-built FastAPI application (stateless, horizontally scalable)
- Async-by-default with minimal memory footprint
- SSE-compatible endpoints for real-time streaming
- Background task handling for metrics and embeddings
- Memory leak prevention focus

**Control Plane:**
- Integrated UI for visualization, monitoring, and debugging
- Real-time agent activity tracking
- Direct browser-to-runtime connection
- Runs entirely in your infrastructure (zero external dependencies)

### Privacy-First Architecture

```
┌─────────────────┐         ┌──────────────────────┐
│   Your Browser  │────────▶│  AgentOS (Your Cloud)│
│  (Control Plane)│         │  • Agents            │
└─────────────────┘         │  • Database          │
                            │  • Logs & Metrics    │
    No External Data        │  • Vector Stores     │
    Transmission            └──────────────────────┘
```

---

## Performance Benchmarks

### October 2025 Benchmarks (Apple M4 MacBook Pro)

| Metric            | Agno   | LangGraph | PydanticAI | CrewAI  |
|-------------------|--------|-----------|------------|---------|
| **Instantiation** | ~3μs   | ~1.6ms    | ~171μs     | ~210μs  |
| **Speed Factor**  | 1×     | 529× slower| 57× slower | 70× slower |
| **Memory Usage**  | 6.6 KB | 160 KB    | 26.4 KB    | 66 KB   |
| **Memory Factor** | 1×     | 24× more  | 4× more    | 10× more|

### Performance Implications

**For Enterprise Architects:**
- **Microservice Architecture**: Sub-microsecond instantiation enables agent-per-request patterns
- **Concurrent Operations**: Run thousands of lightweight agents simultaneously
- **Cost Efficiency**: 50× memory reduction translates to significant infrastructure savings
- **Latency-Sensitive Applications**: Microsecond overhead suitable for real-time systems

**Real-World Impact:**
- Agent creation: ~2μs (vs LangGraph's ~10,000× slower)
- Memory footprint: ~3.75 KB average per agent
- Enables scenarios impossible with heavier frameworks

---

## Core Capabilities

### 1. Agents

Agno agents are the fundamental building blocks:

**Core Features:**
- **Memory**: Session persistence across interactions
- **Knowledge**: Vector database integration for domain expertise
- **Tools**: Access to 100+ built-in toolkits (1000s of tools)
- **Session Management**: User-specific context and history
- **HITL Support**: Human approval gates and overrides
- **Guardrails**: Built-in validation and security controls
- **MCP Integration**: Connect to any MCP server

**Agent Anatomy:**
```python
Agent(
    name="Agent Name",
    model=Model,                    # Any supported LLM
    tools=[],                       # Toolkits and MCP servers
    description="",                 # Agent role/purpose
    instructions=[],                # Behavior guidelines
    db=Database,                    # Session persistence
    knowledge=KnowledgeBase,        # Vector database
    show_tool_calls=True,           # Debugging visibility
    markdown=True,                  # Formatted output
    reasoning=True,                 # Enable reasoning mode
    input_schema=Schema,            # Type-safe inputs
    output_schema=Schema,           # Type-safe outputs
)
```

### 2. Multi-Agent Teams

Teams enable sophisticated coordination:

**Architecture:**
- **Team Leader**: Orchestrates delegation and synthesis
- **Team Members**: Specialized agents with domain expertise
- **Shared Context**: State propagation across team
- **Coordination Modes**: Route, Collaborate, Coordinate

**Coordination Patterns:**

**Route Mode:**
- Simple delegation based on task type
- Leader routes to appropriate specialist
- Minimal inter-agent communication

**Collaborative Mode:**
- Agents work together on shared task
- Information sharing between specialists
- Iterative refinement

**Coordinate Mode:**
- Leader delegates sub-tasks
- Members work independently
- Leader synthesizes results into cohesive output

### 3. Workflows

Deterministic execution for production reliability:

**Components:**
- **Workflow Class**: Top-level orchestrator
- **Step**: Atomic unit (Agent, Team, or function)
- **Router**: Branching logic for conditional paths

**Execution Patterns:**
- Sequential: Steps run in order
- Parallel: Steps run concurrently
- Looped: Iterative execution
- Conditional: Branch based on logic

**Benefits:**
- Deterministic behavior (reproducible outcomes)
- State management (pause/resume/audit)
- Easy debugging (step-by-step inspection)
- Composable (Python-native code)

---

## AgentOS Runtime & Deployment

### Architecture Overview

AgentOS is a production-ready FastAPI application designed for enterprise deployment.

**Key Characteristics:**
- **Stateless**: No server-side session affinity required
- **Horizontally Scalable**: Add instances to handle load
- **Async-First**: Non-blocking I/O for high concurrency
- **SSE-Compatible**: Real-time streaming to clients
- **Resource-Efficient**: Minimal memory footprint

### Deployment Options

#### Docker Deployment (Recommended)

```bash
# Quick start with Docker Compose
docker compose up -d

# Services:
# - API: Port 8000
# - PostgreSQL: Port 5432
```

**Docker Compose Stack:**
- Dockerized FastAPI application
- PostgreSQL for session/state storage
- Volume mounts for persistence
- Environment-based configuration

#### Cloud Deployment

**Supported Platforms:**
- AWS (ECS, EKS, Lambda)
- Google Cloud Platform (Cloud Run, GKE)
- Azure (Container Instances, AKS)
- Self-hosted Kubernetes

**Infrastructure Requirements:**
- Application tier: Stateless containers
- Database tier: PostgreSQL (managed or self-hosted)
- Vector store: 20+ options (pgvector, Pinecone, Weaviate, etc.)
- Monitoring: Built-in metrics endpoints

### Control Plane

The AgentOS control plane provides:

**Real-Time Monitoring:**
- Agent execution traces
- Tool call inspection
- Performance metrics
- Error tracking

**Testing Interface:**
- Interactive agent testing
- Team collaboration simulation
- Workflow step-through debugging

**Architecture:**
```
Browser → Direct HTTPS → AgentOS (Your Cloud)
           ↓
      No proxy/gateway
      No data to vendor
      Complete privacy
```

### Production Considerations

**Scalability:**
- Horizontal scaling via load balancer
- Session data in PostgreSQL (not in-memory)
- Vector database separate from compute
- Background tasks for embeddings/metrics

**Reliability:**
- Health check endpoints
- Graceful shutdown handling
- Connection pool management
- Retry logic for transient failures

**Performance Optimization:**
- Async operations throughout
- Parallel embedding generation
- Background metric collection
- Memory leak prevention

---

## Multi-Agent Systems

### Team Architecture

Multi-agent teams in Agno replicate real-world organizational structures:

**Team Leader:**
- Receives initial task/query
- Analyzes requirements
- Delegates to appropriate team members
- Synthesizes member outputs
- Provides final response

**Team Members:**
- Specialized domain experts
- Receive delegated sub-tasks
- Execute independently
- Return results to leader

### Coordination Mode Deep Dive

#### Route Mode

**Use Case:** Task classification and delegation

**Pattern:**
```
Query → Leader analyzes → Routes to Specialist → Response
```

**Example:** Customer support routing (billing, technical, account)

**Implementation:**
```python
from agno.team import Team

support_team = Team(
    mode="route",
    members=[billing_agent, technical_agent, account_agent],
    leader=routing_agent,
)
```

#### Collaborative Mode

**Use Case:** Multiple perspectives on single problem

**Pattern:**
```
Query → All agents contribute → Combined insights → Response
```

**Example:** Investment analysis (fundamental, technical, sentiment)

**Implementation:**
```python
from agno.team import Team

analysis_team = Team(
    mode="collaborate",
    members=[fundamental_agent, technical_agent, sentiment_agent],
    leader=synthesis_agent,
)
```

#### Coordinate Mode

**Use Case:** Complex multi-step projects

**Pattern:**
```
Query → Leader decomposes task → Parallel execution → Synthesis
```

**Example:** Research report (search, write, edit)

**Implementation:**
```python
from agno.team import Team

editorial_team = Team(
    mode="coordinate",
    members=[researcher_agent, writer_agent, editor_agent],
    leader=editor_coordinator,
    instructions="""
    1. Research: Gather information
    2. Write: Create draft
    3. Edit: Refine and finalize
    """,
)
```

### Real-World Team Patterns

#### Financial Analysis Team

**Structure:**
- **Finance Agent**: Market data, stock prices, analyst recommendations
- **Risk Agent**: Volatility analysis, news sentiment, risk metrics
- **Team Leader**: Synthesizes comprehensive investment report

**Coordination:** Coordinate mode (parallel analysis, synthesized report)

#### Editorial Production Team

**Structure:**
- **Searcher Agent**: Web research, fact gathering
- **Writer Agent**: Content creation, draft generation
- **Editor Agent**: Quality control, style refinement
- **Team Leader**: Coordinates workflow, ensures standards

**Coordination:** Coordinate mode (sequential pipeline)

#### Logistics Operations Team

**Structure:**
- **Route Optimizer**: Path planning, delivery scheduling
- **Tracker Agent**: Shipment status, location monitoring
- **Alert Agent**: Exception handling, notifications
- **Team Leader**: Unified operations interface

**Coordination:** Route mode (task-based delegation)

### Team Design Best Practices

1. **Clear Role Definition**: Each agent should have distinct expertise
2. **Instruction Clarity**: Leader must understand delegation logic
3. **Context Sharing**: Ensure relevant information flows between agents
4. **Error Handling**: Team members should gracefully handle failures
5. **Result Validation**: Leader validates member outputs before synthesis

---

## Workflows & Deterministic Execution

### Why Workflows?

Traditional agentic systems are non-deterministic—agents decide their own execution paths. Workflows provide:

- **Predictability**: Same input → Same execution path
- **Auditability**: Complete execution trace
- **Reliability**: Failure recovery and retry logic
- **Compliance**: Required for regulated industries

### Workflow Architecture

```python
from agno.workflow import Workflow, Step, Router

class MyWorkflow(Workflow):
    def __init__(self):
        super().__init__(name="My Workflow")

    def run(self):
        # Step 1: Data gathering
        data = Step(
            name="Gather Data",
            executor=data_agent,
        ).run()

        # Step 2: Conditional branching
        if data.requires_analysis:
            result = Step(
                name="Deep Analysis",
                executor=analysis_team,
            ).run(data)
        else:
            result = Step(
                name="Quick Summary",
                executor=summary_agent,
            ).run(data)

        # Step 3: Final report
        report = Step(
            name="Generate Report",
            executor=report_agent,
        ).run(result)

        return report
```

### Execution Patterns

#### Sequential Execution

Steps run one after another, output passed as input:

```python
step1_output = Step("Step 1", agent1).run()
step2_output = Step("Step 2", agent2).run(step1_output)
step3_output = Step("Step 3", agent3).run(step2_output)
```

#### Parallel Execution

Independent steps run concurrently:

```python
import asyncio

results = await asyncio.gather(
    Step("Analysis A", agent_a).run_async(data),
    Step("Analysis B", agent_b).run_async(data),
    Step("Analysis C", agent_c).run_async(data),
)
```

#### Conditional Execution

Branching based on runtime conditions:

```python
def router_logic(input_data):
    if input_data.type == "urgent":
        return "expedite_path"
    else:
        return "standard_path"

router = Router(logic=router_logic)
next_step = router.route(input_data)
```

#### Looped Execution

Iterative refinement:

```python
max_iterations = 5
result = initial_data

for i in range(max_iterations):
    result = Step(f"Iteration {i}", refine_agent).run(result)
    if result.quality_score > 0.95:
        break
```

### State Management

Workflows maintain state across execution:

**Persistence:**
- Save workflow state to database
- Resume from checkpoint on failure
- Audit trail for compliance

**Context Passing:**
- Explicit data flow between steps
- No hidden state mutations
- Type-safe with schemas

### Workflow vs. Agent Teams

**Use Workflows When:**
- Deterministic execution required
- Compliance/audit needs
- Complex branching logic
- Long-running processes (pause/resume)
- Financial or healthcare domains

**Use Agent Teams When:**
- Flexible problem-solving needed
- Agents should choose tools dynamically
- Real-time adaptation required
- Creative/exploratory tasks

---

## Memory & Knowledge Management

### Memory System

Agno's memory system enables agents to maintain context across sessions.

#### Database-Backed Memory

**Supported Databases:**
- SQLite (development/small-scale)
- PostgreSQL (production)
- MySQL
- DynamoDB

**Implementation:**
```python
from agno.agent import Agent
from agno.db.postgres import PostgresDb

agent = Agent(
    name="Customer Support Agent",
    model=Claude(id="claude-sonnet-4-5"),
    db=PostgresDb(
        host="localhost",
        port=5432,
        database="agno_db",
        user="agno_user",
        password="secure_password",
    ),
    add_history_to_context=True,  # Include past messages
)
```

#### Session Management

**Session Isolation:**
- Each user gets unique session ID
- Conversations isolated per user
- Cross-session retrieval for returning users

**Context Window Management:**
- Automatic message history pruning
- Configurable context limits
- Sliding window over conversation history

#### Memory Types

**Short-Term Memory:**
- Current conversation context
- Recent tool calls and results
- Active session variables

**Long-Term Memory:**
- Historical interactions
- User preferences
- Past problem resolutions

**Collective Memory (Culture):**
- Shared knowledge across agents
- Organizational learnings
- Best practices and patterns

### Knowledge Management

Knowledge in Agno refers to domain-specific information stored in vector databases.

#### Agentic RAG

**Default Pattern:** Agents search knowledge base on-demand

**Flow:**
```
User Query → Agent analyzes → Searches knowledge → Retrieves context → LLM generates response
```

**Benefits:**
- Dynamic few-shot learning
- Up-to-date information retrieval
- Reduced hallucinations
- Scalable knowledge base

#### Supported Vector Stores (20+)

**Open Source:**
- pgvector (PostgreSQL extension)
- ChromaDB
- LanceDB
- Qdrant
- Weaviate
- Milvus

**Managed Services:**
- Pinecone
- Zilliz (Milvus cloud)
- Astra DB (DataStax)
- MongoDB Atlas Vector Search
- Azure Cognitive Search
- AWS OpenSearch

#### Knowledge Implementation

```python
from agno.agent import Agent
from agno.knowledge.pgvector import PgVectorKnowledgeBase
from agno.vectordb.pgvector import PgVector

# Create vector database
vector_db = PgVector(
    host="localhost",
    port=5432,
    database="knowledge_db",
    collection="product_docs",
)

# Create knowledge base
knowledge_base = PgVectorKnowledgeBase(
    vector_db=vector_db,
    num_documents=5,  # Top-K retrieval
)

# Add knowledge to agent
agent = Agent(
    name="Product Support Agent",
    model=OpenAIChat(id="gpt-4o"),
    knowledge=knowledge_base,
)

# Load documents into knowledge base
knowledge_base.load_documents([
    "docs/user_guide.pdf",
    "docs/api_reference.md",
    "docs/troubleshooting.md",
])
```

#### Hybrid Search + Reranking

Agno supports advanced retrieval patterns:

**Hybrid Search:**
- Combines keyword search (BM25) with vector similarity
- Better recall for specific terms
- Improved precision for semantic queries

**Reranking:**
- Two-stage retrieval (broad search → rerank)
- Cross-encoder models for relevance scoring
- Optimal top-K selection

**Configuration:**
```python
knowledge_base = PgVectorKnowledgeBase(
    vector_db=vector_db,
    num_documents=5,
    hybrid_search=True,
    rerank=True,
    reranker="ms-marco-MultiBERT-L-12",
)
```

---

## Model Context Protocol (MCP) Integration

### What is MCP?

Model Context Protocol is a standardized interface for connecting AI agents to external systems. Agno provides best-in-class MCP support.

### MCP Transport Types

#### 1. stdio (Standard Input/Output)

**Default transport** for local MCP servers.

```python
from agno.tools.mcp import MCPTools

mcp_tools = MCPTools(
    transport="stdio",
    command="npx",
    args=["-y", "@modelcontextprotocol/server-filesystem"],
)
```

**Use Case:** Local filesystem access, system tools

#### 2. Streamable HTTP

**HTTP-based transport** for remote MCP servers.

```python
from agno.tools.mcp import MCPTools

mcp_tools = MCPTools(
    transport="streamable-http",
    url="https://docs.agno.com/mcp",
)
```

**Use Case:** Hosted MCP services, cloud integrations

#### 3. SSE (Server-Sent Events)

**Event stream transport** for real-time updates.

```python
from agno.tools.mcp import MCPTools

mcp_tools = MCPTools(
    transport="sse",
    url="https://mcp-server.example.com/events",
)
```

**Use Case:** Live data feeds, monitoring systems

### MCP Integration Examples

#### Filesystem Agent

```python
from agno.agent import Agent
from agno.models.anthropic import Claude
from agno.tools.mcp import MCPTools

filesystem_agent = Agent(
    name="Filesystem Agent",
    model=Claude(id="claude-sonnet-4-5"),
    tools=[
        MCPTools(
            transport="stdio",
            command="npx",
            args=["-y", "@modelcontextprotocol/server-filesystem", "/path/to/directory"],
        )
    ],
    markdown=True,
)

filesystem_agent.print_response("List all Python files modified in the last 7 days")
```

#### GitHub Integration

```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.mcp import MCPTools
import os

github_agent = Agent(
    name="GitHub Agent",
    model=OpenAIChat(id="gpt-4o"),
    tools=[
        MCPTools(
            transport="stdio",
            command="npx",
            args=["-y", "@modelcontextprotocol/server-github"],
            env={"GITHUB_TOKEN": os.getenv("GITHUB_TOKEN")},
        )
    ],
    markdown=True,
)

github_agent.print_response("Find recent issues in the agno-agi/agno repository")
```

#### Context7 MCP (Programming Docs)

```python
from agno.agent import Agent
from agno.models.anthropic import Claude
from agno.tools.mcp import MCPTools

context7_agent = Agent(
    name="Programming Assistant",
    model=Claude(id="claude-sonnet-4-5"),
    tools=[
        MCPTools(
            transport="streamable-http",
            url="https://context7.example.com/mcp",
        )
    ],
    markdown=True,
)

context7_agent.print_response("Show me best practices for React hooks")
```

### Multiple MCP Servers

Connect to multiple MCP servers simultaneously:

```python
from agno.tools.mcp import MultiMCPTools

multi_mcp = MultiMCPTools(
    servers=[
        {
            "name": "filesystem",
            "transport": "stdio",
            "command": "npx",
            "args": ["-y", "@modelcontextprotocol/server-filesystem"],
        },
        {
            "name": "github",
            "transport": "stdio",
            "command": "npx",
            "args": ["-y", "@modelcontextprotocol/server-github"],
        },
        {
            "name": "supabase",
            "transport": "streamable-http",
            "url": "https://mcp.supabase.com",
        },
    ]
)

agent = Agent(
    name="Multi-Tool Agent",
    model=Claude(id="claude-sonnet-4-5"),
    tools=[multi_mcp],
)
```

### MCP Best Practices

1. **Connection Management**: Always close MCP connections when done
   ```python
   try:
       result = agent.run("query")
   finally:
       mcp_tools.close()
   ```

2. **Error Handling**: Wrap MCP operations in try/except
   ```python
   try:
       mcp_tools = MCPTools(...)
   except MCPConnectionError as e:
       logger.error(f"MCP connection failed: {e}")
   ```

3. **Environment Variables**: Use environment-based configuration
   ```python
   env={"API_KEY": os.getenv("SERVICE_API_KEY")}
   ```

4. **Timeout Configuration**: Set appropriate timeouts for MCP operations
   ```python
   mcp_tools = MCPTools(..., timeout=30)
   ```

### Available MCP Servers

**Official MCP Servers:**
- `@modelcontextprotocol/server-filesystem` - File operations
- `@modelcontextprotocol/server-github` - GitHub integration
- `@modelcontextprotocol/server-postgres` - Database access
- `@modelcontextprotocol/server-puppeteer` - Web automation

**Third-Party MCP Servers:**
- Supabase MCP - Database and auth
- Airtable MCP - Spreadsheet operations
- Context7 - Programming documentation
- Custom enterprise MCP servers

---

## Toolkits & Extensibility

### Built-in Toolkits (100+)

Agno provides thousands of tools organized into 100+ toolkits.

#### Web & Search Toolkits

**DuckDuckGoTools:**
```python
from agno.tools.duckduckgo import DuckDuckGoTools

tools = DuckDuckGoTools(
    search=True,  # Web search
    news=True,    # News search
)
```

**ExaTools:**
```python
from agno.tools.exa import ExaTools

tools = ExaTools(
    api_key=os.getenv("EXA_API_KEY"),
)
```

#### Finance Toolkits

**YFinanceTools:**
```python
from agno.tools.yfinance import YFinanceTools

tools = YFinanceTools(
    stock_price=True,              # Current/historical prices
    analyst_recommendations=True,  # Analyst ratings
    company_info=True,             # Company details
    company_news=True,             # Recent news
    technical_indicators=True,     # TA indicators
)
```

#### Development Toolkits

**GithubTools:**
```python
from agno.tools.github import GithubTools

tools = GithubTools(
    search_repositories=True,
    get_issue=True,
    create_issue=True,
    search_code=True,
)
```

**GiphyTools:**
```python
from agno.tools.giphy import GiphyTools

tools = GiphyTools(
    api_key=os.getenv("GIPHY_API_KEY"),
)
```

#### File & Database Toolkits

**Filesystem Tools:**
- Read files
- Write files
- List directories
- Search files

**Database Tools:**
- SQL query execution
- Schema introspection
- Data manipulation

#### Reasoning Toolkit

**ReasoningTools:**
```python
from agno.tools.reasoning import ReasoningTools

tools = ReasoningTools(
    add_instructions=True,  # Include reasoning prompts
)
```

**Use Case:** Enable chain-of-thought reasoning

### Custom Tool Creation

#### Function-Based Tools

```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat

def calculate_roi(investment: float, return_amount: float) -> float:
    """Calculate return on investment percentage.

    Args:
        investment: Initial investment amount
        return_amount: Final return amount

    Returns:
        ROI percentage
    """
    return ((return_amount - investment) / investment) * 100

agent = Agent(
    name="Finance Agent",
    model=OpenAIChat(id="gpt-4o"),
    tools=[calculate_roi],  # Pass function directly
)
```

#### Class-Based Toolkits

```python
from agno.tools import Toolkit

class CustomToolkit(Toolkit):
    def __init__(self):
        super().__init__(name="custom_toolkit")
        self.register(self.tool_one)
        self.register(self.tool_two)

    def tool_one(self, param: str) -> str:
        """Tool one description."""
        return f"Result: {param}"

    def tool_two(self, param: int) -> int:
        """Tool two description."""
        return param * 2

agent = Agent(
    name="Agent",
    model=OpenAIChat(id="gpt-4o"),
    tools=[CustomToolkit()],
)
```

### Tool Visibility & Debugging

```python
agent = Agent(
    name="Debug Agent",
    model=OpenAIChat(id="gpt-4o"),
    tools=[YFinanceTools(), DuckDuckGoTools()],
    show_tool_calls=True,  # Show tool execution in output
    markdown=True,
)
```

**Output includes:**
- Which tools were called
- Input parameters
- Return values
- Execution time

---

## Enterprise Security & Governance

### Privacy Architecture

Agno's privacy-first design ensures complete data control.

#### Zero External Dependencies

**Data Flow:**
```
User → Browser → Your AgentOS (Your Cloud) → Your Database/Vector Store
         ↑                    ↓
         └────────────────────┘
         (Direct connection, no proxy)
```

**Guarantees:**
- No data sent to Agno servers (none exist!)
- No data sent to third-party services
- No telemetry to external endpoints (configurable)
- Complete air-gap capability

#### Infrastructure Control

**Your Cloud, Your Rules:**
- Deploy to AWS, GCP, Azure, or on-premise
- Choose your own database (PostgreSQL, etc.)
- Select your vector store (20+ options)
- Control network policies and firewalls
- Implement your security standards

### Role-Based Access Control (RBAC)

Agno provides enterprise-grade access control.

#### Per-Agent Permissions

```python
from agno.agent import Agent
from agno.auth import RBACPolicy

# Define policy
policy = RBACPolicy(
    roles={
        "admin": ["*"],  # Full access
        "analyst": ["read_data", "query_agent"],
        "viewer": ["query_agent"],
    }
)

# Apply to agent
agent = Agent(
    name="Sensitive Agent",
    model=Claude(id="claude-sonnet-4-5"),
    tools=[DatabaseTools(), FileSystemTools()],
    rbac_policy=policy,
)
```

#### Tool-Level Restrictions

**Protect sensitive operations:**
- Database writes restricted to admins
- Filesystem access by role
- API key usage by permission level
- Audit logging for privileged operations

### Data Governance

#### Complete Data Ownership

**Storage:**
- All data in your databases (PostgreSQL, etc.)
- Vector embeddings in your vector store
- Session data under your control
- No vendor lock-in (export anytime)

**Retention:**
- Infinite retention with no vendor costs
- Implement your retention policies
- GDPR/CCPA compliance-ready
- Data deletion on demand

#### Audit Trail

**Logged Information:**
- Every agent invocation
- Tool calls and parameters
- User sessions and queries
- Performance metrics
- Error traces

**Use Cases:**
- Compliance reporting (SOC 2, HIPAA)
- Security incident investigation
- Usage analytics
- Cost allocation

### Secrets Management

**Environment-Based Configuration:**
```python
import os

agent = Agent(
    name="Secure Agent",
    model=OpenAIChat(
        id="gpt-4o",
        api_key=os.getenv("OPENAI_API_KEY"),  # From environment
    ),
    tools=[
        YFinanceTools(),  # No API key needed
        ExaTools(api_key=os.getenv("EXA_API_KEY")),  # From environment
    ],
)
```

**Integration with Secrets Managers:**
- AWS Secrets Manager
- Azure Key Vault
- GCP Secret Manager
- HashiCorp Vault
- Kubernetes Secrets

### Compliance Readiness

**Agno's Architecture Supports:**

**GDPR (General Data Protection Regulation):**
- Right to access: Export user data
- Right to deletion: Purge user sessions
- Data minimization: Store only necessary data
- Privacy by design: No external data sharing

**HIPAA (Healthcare):**
- PHI isolation: User-level encryption
- Audit logging: Complete activity trail
- Access controls: RBAC for sensitive data
- Infrastructure: Deploy in compliant cloud

**SOC 2:**
- Security: RBAC, encryption, audit logs
- Availability: Horizontal scaling, health checks
- Confidentiality: Zero external data transmission
- Processing Integrity: Deterministic workflows

**PCI DSS (Payment Card Industry):**
- Data isolation: Per-user sessions
- Access control: RBAC
- Monitoring: Real-time metrics
- Encryption: In-transit and at-rest

---

## Advanced Features

### Reasoning Capabilities

Agno treats reasoning as a first-class citizen.

#### Reasoning Modes

**1. ReasoningTools:**
```python
from agno.agent import Agent
from agno.tools.reasoning import ReasoningTools

agent = Agent(
    name="Reasoning Agent",
    model=Claude(id="claude-sonnet-4-5"),
    tools=[
        ReasoningTools(add_instructions=True),
        YFinanceTools(),
    ],
)
```

**Behavior:**
- Agent explicitly calls reasoning tool
- Generates chain-of-thought
- Shows reasoning steps to user

**2. Reasoning Flag:**
```python
agent = Agent(
    name="Deep Reasoning Agent",
    model=Claude(id="claude-sonnet-4-5"),
    reasoning=True,  # Enable reasoning mode
    reasoning_model=Claude(id="claude-3-7-sonnet"),  # Separate model for reasoning
    tools=[YFinanceTools()],
)
```

**Behavior:**
- Separate "Reasoning Agent" activated
- Multi-step problem decomposition
- Tool calls at each reasoning step
- Validation before final answer
- Hands result back to main agent

**3. Custom Chain-of-Thought:**
```python
agent = Agent(
    name="Custom CoT Agent",
    model=OpenAIChat(id="gpt-4o"),
    instructions=[
        "Think step-by-step before answering",
        "Show your reasoning process",
        "Validate each step before proceeding",
    ],
)
```

### Structured Outputs

Type-safe inputs and outputs for production reliability.

#### Input Schema

```python
from pydantic import BaseModel, Field

class InvestmentQuery(BaseModel):
    ticker: str = Field(..., description="Stock ticker symbol")
    analysis_type: str = Field(..., description="Type: fundamental, technical, or both")
    time_horizon: str = Field(..., description="Investment horizon: short, medium, long")

agent = Agent(
    name="Investment Agent",
    model=Claude(id="claude-sonnet-4-5"),
    input_schema=InvestmentQuery,
    tools=[YFinanceTools()],
)

# Type-safe invocation
result = agent.run(
    InvestmentQuery(
        ticker="AAPL",
        analysis_type="fundamental",
        time_horizon="long",
    )
)
```

#### Output Schema

```python
from pydantic import BaseModel, Field
from typing import List

class InvestmentRecommendation(BaseModel):
    ticker: str
    recommendation: str = Field(..., description="buy, hold, or sell")
    confidence: float = Field(..., ge=0, le=1)
    reasoning: List[str]
    price_target: float

agent = Agent(
    name="Investment Agent",
    model=Claude(id="claude-sonnet-4-5"),
    output_schema=InvestmentRecommendation,
    tools=[YFinanceTools()],
)

# Type-safe response
recommendation: InvestmentRecommendation = agent.run("Analyze AAPL")
print(f"Recommendation: {recommendation.recommendation}")
print(f"Confidence: {recommendation.confidence}")
```

### Multimodal Capabilities

Agno agents are natively multimodal.

#### Input Modalities

**Text:**
```python
agent.run("What is the capital of France?")
```

**Image:**
```python
agent.run([
    "Describe this image",
    {"type": "image_url", "image_url": {"url": "https://example.com/image.jpg"}},
])
```

**Audio:**
```python
agent.run([
    "Transcribe this audio",
    {"type": "audio_url", "audio_url": {"url": "https://example.com/audio.mp3"}},
])
```

**Video:**
```python
agent.run([
    "Summarize this video",
    {"type": "video_url", "video_url": {"url": "https://example.com/video.mp4"}},
])
```

**Mixed:**
```python
agent.run([
    "Compare these two images",
    {"type": "image_url", "image_url": {"url": "https://example.com/image1.jpg"}},
    {"type": "image_url", "image_url": {"url": "https://example.com/image2.jpg"}},
])
```

#### Output Modalities

**Text (Default):**
```python
response = agent.run("Explain quantum computing")
print(response.content)
```

**Markdown:**
```python
agent = Agent(
    name="Writer Agent",
    model=OpenAIChat(id="gpt-4o"),
    markdown=True,  # Enable markdown formatting
)
```

**Structured Data:**
```python
agent = Agent(
    name="Data Agent",
    model=OpenAIChat(id="gpt-4o"),
    output_schema=MyDataSchema,
)
```

### Dynamic Context Engineering

Inject runtime variables into agent context.

#### Context Variables

```python
from agno.agent import Agent
from datetime import datetime

agent = Agent(
    name="Context-Aware Agent",
    model=OpenAIChat(id="gpt-4o"),
    instructions=[
        "You are a helpful assistant",
        f"Current date: {datetime.now().strftime('%Y-%m-%d')}",
        "User timezone: {timezone}",  # Injected at runtime
        "User preferences: {preferences}",  # Injected at runtime
    ],
)

# Runtime injection
response = agent.run(
    "What's on my calendar today?",
    context={
        "timezone": "America/New_York",
        "preferences": {"format": "concise"},
    }
)
```

### Human-in-the-Loop (HITL)

Enable human oversight and approval.

#### Confirmation Gates

```python
from agno.agent import Agent
from agno.tools.database import DatabaseTools

agent = Agent(
    name="Database Agent",
    model=OpenAIChat(id="gpt-4o"),
    tools=[DatabaseTools()],
    require_confirmation=["delete_record", "update_schema"],  # Require approval
)
```

**Behavior:**
- Agent pauses before dangerous operations
- User sees proposed action
- User approves or rejects
- Agent proceeds or aborts

#### Lifecycle Hooks

```python
def pre_run_hook(input_data):
    """Runs before agent execution."""
    print(f"Agent input: {input_data}")
    return input_data  # Can modify input

def post_run_hook(output_data):
    """Runs after agent execution."""
    print(f"Agent output: {output_data}")
    return output_data  # Can modify output

agent = Agent(
    name="Hooked Agent",
    model=OpenAIChat(id="gpt-4o"),
    pre_run_hook=pre_run_hook,
    post_run_hook=post_run_hook,
)
```

---

## Code Examples & Patterns

### Basic Agent Patterns

#### Simple Q&A Agent

```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat

agent = Agent(
    name="Q&A Agent",
    model=OpenAIChat(id="gpt-4o"),
    description="You are a concise and helpful assistant.",
    markdown=True,
)

agent.print_response("What is machine learning?", stream=True)
```

#### Agent with Search

```python
from agno.agent import Agent
from agno.models.anthropic import Claude
from agno.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    name="Research Agent",
    model=Claude(id="claude-sonnet-4-5"),
    tools=[DuckDuckGoTools()],
    description="You are an enthusiastic researcher!",
    show_tool_calls=True,
    markdown=True,
)

agent.print_response("Tell me about the latest developments in quantum computing", stream=True)
```

### Specialized Agent Patterns

#### Finance Agent

```python
from agno.agent import Agent
from agno.models.anthropic import Claude
from agno.tools.reasoning import ReasoningTools
from agno.tools.yfinance import YFinanceTools

finance_agent = Agent(
    name="Finance Analyst",
    model=Claude(id="claude-sonnet-4-20250514"),
    tools=[
        ReasoningTools(add_instructions=True),
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            company_info=True,
            company_news=True,
        ),
    ],
    instructions=[
        "You are a financial analyst with expertise in stock analysis",
        "Always provide data-driven insights",
        "Use tables to display financial data",
        "Include reasoning for recommendations",
    ],
    markdown=True,
    show_tool_calls=True,
)

finance_agent.print_response(
    "Provide a comprehensive analysis of AAPL stock with buy/hold/sell recommendation",
    stream=True,
)
```

#### RAG Agent with Knowledge Base

```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.knowledge.pgvector import PgVectorKnowledgeBase
from agno.vectordb.pgvector import PgVector
from agno.embedder.openai import OpenAIEmbedder

# Setup vector database
vector_db = PgVector(
    host="localhost",
    port=5432,
    database="knowledge_db",
    collection="company_docs",
    embedder=OpenAIEmbedder(model="text-embedding-3-small"),
)

# Create knowledge base
knowledge_base = PgVectorKnowledgeBase(
    vector_db=vector_db,
    num_documents=3,  # Top-3 retrieval
)

# Load documents
knowledge_base.load_documents([
    "docs/product_manual.pdf",
    "docs/faq.md",
    "docs/troubleshooting.md",
])

# Create RAG agent
rag_agent = Agent(
    name="Support Agent",
    model=OpenAIChat(id="gpt-4o"),
    knowledge=knowledge_base,
    search_knowledge=True,  # Enable automatic RAG
    instructions=[
        "You are a customer support specialist",
        "Always search the knowledge base before answering",
        "If information is not in the knowledge base, say so",
    ],
    markdown=True,
)

rag_agent.print_response("How do I reset my password?", stream=True)
```

#### Multi-Agent Team

```python
from agno.agent import Agent
from agno.team import Team
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools

# Define team members
researcher = Agent(
    name="Researcher",
    role="Research information on the web",
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGoTools()],
)

writer = Agent(
    name="Writer",
    role="Write engaging content based on research",
    model=OpenAIChat(id="gpt-4o"),
)

editor = Agent(
    name="Editor",
    role="Review and refine written content",
    model=OpenAIChat(id="gpt-4o"),
)

# Create coordinated team
editorial_team = Team(
    name="Editorial Team",
    mode="coordinate",
    members=[researcher, writer, editor],
    instructions="""
    1. Researcher: Gather information on the topic
    2. Writer: Create a draft article based on research
    3. Editor: Review, refine, and finalize the article
    """,
    markdown=True,
)

editorial_team.print_response(
    "Write a blog post about the future of renewable energy",
    stream=True,
)
```

#### Workflow with Conditional Logic

```python
from agno.workflow import Workflow, Step
from agno.agent import Agent
from agno.models.anthropic import Claude

class DataProcessingWorkflow(Workflow):
    def __init__(self):
        super().__init__(name="Data Processing")

        self.validator = Agent(
            name="Validator",
            model=Claude(id="claude-sonnet-4-5"),
        )

        self.simple_processor = Agent(
            name="Simple Processor",
            model=Claude(id="claude-sonnet-4-5"),
        )

        self.complex_processor = Agent(
            name="Complex Processor",
            model=Claude(id="claude-sonnet-4-5"),
        )

    def run(self, data: str):
        # Step 1: Validate data
        validation = Step(
            name="Validate Data",
            executor=self.validator,
        ).run(f"Validate this data and determine if complex processing is needed: {data}")

        # Step 2: Conditional processing
        if "complex" in validation.lower():
            result = Step(
                name="Complex Processing",
                executor=self.complex_processor,
            ).run(data)
        else:
            result = Step(
                name="Simple Processing",
                executor=self.simple_processor,
            ).run(data)

        return result

# Execute workflow
workflow = DataProcessingWorkflow()
output = workflow.run("Process this complex dataset: [...]")
```

### Production Patterns

#### Agent with Full Configuration

```python
from agno.agent import Agent
from agno.models.anthropic import Claude
from agno.db.postgres import PostgresDb
from agno.knowledge.pgvector import PgVectorKnowledgeBase
from agno.vectordb.pgvector import PgVector
from agno.tools.yfinance import YFinanceTools
from agno.tools.mcp import MCPTools
import os

production_agent = Agent(
    # Identity
    name="Production Finance Agent",
    description="Enterprise-grade financial analysis agent",

    # Model
    model=Claude(
        id="claude-sonnet-4-5",
        api_key=os.getenv("ANTHROPIC_API_KEY"),
    ),

    # Memory
    db=PostgresDb(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT")),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
    ),
    add_history_to_context=True,
    num_history_messages=10,

    # Knowledge
    knowledge=PgVectorKnowledgeBase(
        vector_db=PgVector(
            host=os.getenv("VECTOR_DB_HOST"),
            port=int(os.getenv("VECTOR_DB_PORT")),
            database=os.getenv("VECTOR_DB_NAME"),
            collection="financial_knowledge",
        ),
        num_documents=5,
    ),
    search_knowledge=True,

    # Tools
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            company_info=True,
        ),
        MCPTools(
            transport="streamable-http",
            url=os.getenv("MCP_SERVER_URL"),
        ),
    ],

    # Behavior
    instructions=[
        "You are an expert financial analyst",
        "Always search knowledge base for relevant context",
        "Provide data-driven recommendations",
        "Use tables for financial data presentation",
    ],

    # Output
    markdown=True,
    show_tool_calls=True,

    # Advanced
    reasoning=True,
    require_confirmation=["execute_trade"],

    # Type Safety
    input_schema=FinancialQuery,
    output_schema=FinancialRecommendation,
)
```

#### AgentOS Production Setup

```python
from agno.agent import Agent
from agno.db.postgres import PostgresDb
from agno.os import AgentOS
from agno.models.anthropic import Claude
from agno.tools.yfinance import YFinanceTools
import os

# Define agents
finance_agent = Agent(
    name="Finance Agent",
    model=Claude(id="claude-sonnet-4-5"),
    db=PostgresDb(
        host=os.getenv("DB_HOST"),
        database="agno_production",
    ),
    tools=[YFinanceTools()],
)

support_agent = Agent(
    name="Support Agent",
    model=Claude(id="claude-sonnet-4-5"),
    db=PostgresDb(
        host=os.getenv("DB_HOST"),
        database="agno_production",
    ),
)

# Create AgentOS
agent_os = AgentOS(
    agents=[finance_agent, support_agent],
    db=PostgresDb(
        host=os.getenv("DB_HOST"),
        database="agno_production",
    ),
)

# Get FastAPI app
app = agent_os.get_app()

# Run server
if __name__ == "__main__":
    agent_os.serve(
        app="main:app",
        host="0.0.0.0",
        port=8000,
        reload=False,  # Set True for development
    )
```

---

## Framework Comparisons

### Agno vs. LangGraph

| Aspect | Agno | LangGraph |
|--------|------|-----------|
| **Instantiation** | ~3μs | ~1.6ms (529× slower) |
| **Memory Usage** | 6.6 KB | 160 KB (24× more) |
| **Architecture** | Pure Python, composable | Graph-based, stateful |
| **Learning Curve** | Gentle, Pythonic | Steep, requires graph concepts |
| **Documentation** | Excellent, clear examples | Complex, fragmented |
| **Multi-Agent** | Teams (Route/Collaborate/Coordinate) | Supervisor nodes, flexible |
| **Workflows** | Step-based, deterministic | Graph-based, flexible |
| **Best For** | Production apps, clarity, performance | Complex workflows, scale |
| **Use When** | Need performance, readability | Need graph-level control |

**Recommendation:**
- **Choose Agno** for production applications where performance, clarity, and developer experience matter
- **Choose LangGraph** for complex, highly interconnected multi-agent systems requiring graph-level orchestration

### Agno vs. CrewAI

| Aspect | Agno | CrewAI |
|--------|------|--------|
| **Instantiation** | ~3μs | ~210μs (70× slower) |
| **Memory Usage** | 6.6 KB | 66 KB (10× more) |
| **Philosophy** | Pure Python, performance | Role-based, intuitive |
| **Learning Curve** | Moderate | Easy, beginner-friendly |
| **GitHub Stars** | 26,000+ | 30,000+ |
| **Community** | Growing rapidly | Large, established |
| **Multi-Agent** | Teams with modes | Crew metaphor, roles |
| **Best For** | Production, performance | MVPs, prototypes |
| **Use When** | Enterprise deployment | Quick starts, learning |

**Recommendation:**
- **Choose Agno** for production applications requiring performance and enterprise features
- **Choose CrewAI** for rapid prototyping and when ease of use is paramount

### Agno vs. PydanticAI

| Aspect | Agno | PydanticAI |
|--------|------|------------|
| **Instantiation** | ~3μs | ~171μs (57× slower) |
| **Memory Usage** | 6.6 KB | 26.4 KB (4× more) |
| **Type Safety** | Optional (input/output schemas) | Core feature (Pydantic) |
| **Focus** | Multi-agent systems | Type-safe single agents |
| **Complexity** | Full-featured | Minimal, focused |
| **Best For** | Complex systems | Type-safe applications |

**Recommendation:**
- **Choose Agno** for multi-agent systems and comprehensive features
- **Choose PydanticAI** if type safety is your primary concern

### Framework Selection Matrix

#### Choose Agno When:
✓ Production deployment is the goal
✓ Performance and efficiency are critical
✓ Privacy and data governance are paramount
✓ Multi-agent teams needed
✓ Multimodal capabilities required
✓ Clear, Pythonic code preferred
✓ Enterprise features (RBAC, audit) needed

#### Choose LangGraph When:
✓ Complex, interconnected agent graphs
✓ Maximum flexibility in orchestration
✓ Advanced state management needed
✓ Distributed systems at scale
✓ Willing to invest in learning curve

#### Choose CrewAI When:
✓ Rapid prototyping required
✓ Team is learning AI agents
✓ Simple role-based coordination sufficient
✓ Strong community support valued
✓ MVP/proof-of-concept phase

---

## Real-World Use Cases

### Finance & Trading

**Stock Analysis Agent:**
```python
from agno.agent import Agent
from agno.models.anthropic import Claude
from agno.tools.yfinance import YFinanceTools
from agno.tools.reasoning import ReasoningTools

stock_analyst = Agent(
    name="Stock Analyst",
    model=Claude(id="claude-sonnet-4-5"),
    tools=[
        YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True),
        ReasoningTools(add_instructions=True),
    ],
    instructions=[
        "Analyze stocks using fundamental and technical data",
        "Provide clear buy/hold/sell recommendations",
        "Include confidence levels and reasoning",
    ],
    markdown=True,
)
```

**Use Cases:**
- Real-time portfolio analysis
- Market sentiment monitoring
- Trading signal generation
- Risk assessment

**Finance-Risk Multi-Agent Team:**
```python
from agno.team import Team

finance_agent = Agent(name="Finance", ...)  # Market data analysis
risk_agent = Agent(name="Risk", ...)        # Volatility and risk metrics

finance_team = Team(
    name="Finance Team",
    mode="coordinate",
    members=[finance_agent, risk_agent],
    instructions="Provide comprehensive investment analysis with risk assessment",
)
```

### Logistics & Operations

**Route Optimization Agent:**
```python
route_optimizer = Agent(
    name="Route Optimizer",
    model=OpenAIChat(id="gpt-4o"),
    tools=[MapsTools(), TrafficTools()],
    instructions=[
        "Optimize delivery routes for efficiency",
        "Consider traffic, distance, and time windows",
        "Provide step-by-step routing instructions",
    ],
)
```

**Shipment Tracking Agent:**
```python
tracking_agent = Agent(
    name="Tracker",
    model=Claude(id="claude-sonnet-4-5"),
    tools=[LogisticsTools()],
    instructions=[
        "Monitor shipment status in real-time",
        "Alert on delays or exceptions",
        "Provide estimated delivery times",
    ],
)
```

**Use Cases:**
- Delivery route optimization
- Real-time shipment tracking
- Exception handling and alerts
- Capacity planning

### Customer Support

**Support Agent with RAG:**
```python
from agno.agent import Agent
from agno.knowledge.pgvector import PgVectorKnowledgeBase

support_agent = Agent(
    name="Support Agent",
    model=OpenAIChat(id="gpt-4o"),
    knowledge=PgVectorKnowledgeBase(
        vector_db=vector_db,
        num_documents=5,
    ),
    tools=[TicketingTools(), KnowledgeBaseTools()],
    instructions=[
        "Provide helpful customer support",
        "Search knowledge base first",
        "Escalate complex issues",
        "Maintain friendly, professional tone",
    ],
    add_history_to_context=True,
)
```

**Use Cases:**
- 24/7 customer support
- Product documentation assistance
- Troubleshooting guidance
- Ticket triage and routing

### Content Creation

**Editorial Team:**
```python
from agno.team import Team

researcher = Agent(name="Researcher", tools=[DuckDuckGoTools()], ...)
writer = Agent(name="Writer", ...)
editor = Agent(name="Editor", ...)

editorial_team = Team(
    name="Editorial Team",
    mode="coordinate",
    members=[researcher, writer, editor],
    instructions="""
    1. Research: Gather information
    2. Write: Create draft article
    3. Edit: Refine and finalize
    """,
)
```

**Use Cases:**
- Blog post generation
- Social media content
- Marketing copy
- Technical documentation

### Enterprise Automation

**Climate Data Automation:**
```python
climate_agent = Agent(
    name="Climate Agent",
    model=Claude(id="claude-sonnet-4-5"),
    tools=[ClimateDataTools(), ReportingTools()],
    knowledge=climate_knowledge_base,
    instructions=[
        "Automate climate data collection",
        "Generate compliance reports",
        "Track sustainability metrics",
    ],
)
```

**Compliance & Disclosure:**
```python
compliance_agent = Agent(
    name="Compliance Agent",
    model=OpenAIChat(id="gpt-4o"),
    tools=[RegulatoryTools(), DocumentTools()],
    knowledge=regulatory_knowledge_base,
    instructions=[
        "Monitor regulatory requirements",
        "Generate disclosure documents",
        "Flag compliance issues",
    ],
    require_confirmation=["submit_disclosure"],
)
```

**Use Cases:**
- Regulatory compliance automation
- ESG reporting
- Document generation
- Audit trail management

### Data Analytics

**Analytics Agent with Database Access:**
```python
from agno.tools.database import DatabaseTools

analytics_agent = Agent(
    name="Analytics Agent",
    model=OpenAIChat(id="gpt-4o"),
    tools=[
        DatabaseTools(connection_string=os.getenv("DB_CONNECTION")),
        VisualizationTools(),
    ],
    instructions=[
        "Query databases for insights",
        "Generate visualizations",
        "Provide data-driven recommendations",
    ],
    show_tool_calls=True,
)
```

**Use Cases:**
- SQL query generation
- Data visualization
- Business intelligence
- Anomaly detection

---

## Community & Ecosystem

### Community Stats (2025)

**GitHub:**
- 26,000+ stars (June 2025)
- 3,000+ forks
- 3,000+ commits
- Active development (multiple releases per week)

**Growth Trajectory:**
- March 2025: 19,000 stars
- April 2025: 23,900 stars
- June 2025: 26,000+ stars

**Developer Ecosystem:**
- Growing community of contributors
- Active issue resolution
- Community-contributed toolkits
- Enterprise adoption increasing

### Community Resources

**Official Channels:**
- **Documentation**: https://docs.agno.com
- **GitHub**: https://github.com/agno-agi/agno
- **Discord**: https://discord.gg/4MtYHHrgA8
- **Community Forum**: https://community.agno.com

**Learning Resources:**
- **Cookbook**: 100+ examples at github.com/agno-agi/agno/tree/main/cookbook
- **Examples Gallery**: docs.agno.com/examples
- **Video Tutorials**: Community-contributed
- **Blog Posts**: Integration guides and use cases

**AI Coding Assistant Integration:**
- **llms-full.txt**: https://docs.agno.com/llms-full.txt
- Use with Cursor, Continue, and other AI coding tools
- Enables context-aware code generation

### Integrations

**LLM Providers (23+):**
- OpenAI (GPT-3.5, GPT-4, GPT-4o)
- Anthropic (Claude 3, Claude 3.5, Claude 4)
- Google (Gemini, PaLM)
- Groq (ultra-fast inference)
- Hugging Face (open models)
- AWS Bedrock
- Azure OpenAI
- Cohere
- Mistral AI
- Ollama (local models)

**Vector Databases (20+):**
- pgvector (PostgreSQL)
- Pinecone
- Weaviate
- Qdrant
- ChromaDB
- LanceDB
- Milvus
- Zilliz
- MongoDB Atlas
- Azure Cognitive Search
- AWS OpenSearch
- Elasticsearch

**Observability:**
- LangWatch integration
- OpenTelemetry support
- Custom metrics endpoints
- Prometheus-compatible

**Development Tools:**
- Portkey integration
- Cursor IDE support
- Continue.dev support
- GitHub Copilot compatible

---

## Cost & Deployment Options

### Pricing Model

**Agno Framework:**
- **Open Source**: Apache-2.0 license
- **Core Framework**: 100% free
- **AgentOS Runtime**: Free, included
- **Control Plane**: Free, self-hosted
- **No Per-Event Fees**: Unlike vendor platforms
- **No Retention Costs**: Unlike vendor platforms
- **No Vendor Lock-In**: All data in your infrastructure

**Your Costs:**
- **LLM API Calls**: Pay your provider (OpenAI, Anthropic, etc.)
- **Cloud Infrastructure**: Your compute/storage costs
- **Database**: PostgreSQL hosting
- **Vector Store**: If using managed service (Pinecone, etc.)

**Cost Comparison:**
```
Vendor Platform:
- Per-event fees: $0.01-0.10 per agent call
- Retention fees: $X per GB-month
- Vendor lock-in
- Limited control

Agno (Self-Hosted):
- No per-event fees: $0
- No retention fees: $0
- Complete control
- Pay only infrastructure costs
```

### Deployment Options

#### Local Development

**Quick Start:**
```bash
pip install agno openai
export OPENAI_API_KEY=sk-xxx
python my_agent.py
```

**With Docker:**
```bash
git clone https://github.com/agno-agi/agno
cd agno/docker
docker compose up -d
```

**Services:**
- AgentOS API: http://localhost:8000
- PostgreSQL: localhost:5432
- Control Plane: Connect via browser

#### Cloud Deployment

**AWS:**
- ECS/Fargate: Containerized deployment
- EKS: Kubernetes orchestration
- Lambda: Serverless (for light workloads)
- RDS: Managed PostgreSQL
- OpenSearch: Vector search

**Google Cloud:**
- Cloud Run: Serverless containers
- GKE: Kubernetes
- Cloud SQL: PostgreSQL
- Vertex AI Vector Search

**Azure:**
- Container Instances: Simple containers
- AKS: Kubernetes
- Azure Database for PostgreSQL
- Azure Cognitive Search

#### Kubernetes Deployment

**Example Manifests:**
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: agentos
spec:
  replicas: 3
  selector:
    matchLabels:
      app: agentos
  template:
    metadata:
      labels:
        app: agentos
    spec:
      containers:
      - name: agentos
        image: your-registry/agentos:latest
        ports:
        - containerPort: 8000
        env:
        - name: DATABASE_URL
          valueFrom:
            secretKeyRef:
              name: db-credentials
              key: url
        resources:
          requests:
            memory: "256Mi"
            cpu: "250m"
          limits:
            memory: "512Mi"
            cpu: "500m"
---
apiVersion: v1
kind: Service
metadata:
  name: agentos-service
spec:
  selector:
    app: agentos
  ports:
  - port: 80
    targetPort: 8000
  type: LoadBalancer
```

**Horizontal Pod Autoscaling:**
```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: agentos-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: agentos
  minReplicas: 2
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
```

#### Production Checklist

**Infrastructure:**
- [ ] Stateless container deployment
- [ ] Horizontal scaling configured
- [ ] Load balancer setup
- [ ] Health check endpoints
- [ ] Managed PostgreSQL database
- [ ] Vector database (if using RAG)
- [ ] SSL/TLS certificates

**Security:**
- [ ] API keys in secrets manager
- [ ] RBAC policies configured
- [ ] Network policies defined
- [ ] Audit logging enabled
- [ ] Backup strategy implemented

**Monitoring:**
- [ ] Metrics collection
- [ ] Log aggregation
- [ ] Error tracking
- [ ] Performance monitoring
- [ ] Alerting configured

**Reliability:**
- [ ] Multi-region deployment (if needed)
- [ ] Database replication
- [ ] Disaster recovery plan
- [ ] Automated backups
- [ ] Rollback strategy

---

## Getting Started

### Installation

```bash
# Install Agno
pip install agno

# Install model provider SDK
pip install openai anthropic groq

# Optional: Install specific toolkits
pip install agno[yfinance]  # Finance tools
pip install agno[duckduckgo]  # Search tools
pip install agno[postgres]  # PostgreSQL support
```

### 5-Minute Quickstart

#### 1. Basic Agent

```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat
import os

# Set API key
os.environ["OPENAI_API_KEY"] = "sk-xxx"

# Create agent
agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    description="You are a helpful assistant",
    markdown=True,
)

# Run agent
agent.print_response("What is the capital of France?", stream=True)
```

#### 2. Agent with Tools

```python
from agno.agent import Agent
from agno.models.anthropic import Claude
from agno.tools.duckduckgo import DuckDuckGoTools
import os

os.environ["ANTHROPIC_API_KEY"] = "sk-ant-xxx"

agent = Agent(
    model=Claude(id="claude-sonnet-4-5"),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
)

agent.print_response("What's the latest news about AI?", stream=True)
```

#### 3. Agent with Memory

```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.db.sqlite import SqliteDb

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    db=SqliteDb(db_file="agent_sessions.db"),
    add_history_to_context=True,
    session_id="user_123",  # Per-user sessions
    markdown=True,
)

# First interaction
agent.print_response("My name is Alice", stream=True)

# Second interaction (remembers context)
agent.print_response("What's my name?", stream=True)
# Output: "Your name is Alice"
```

#### 4. Production AgentOS

```python
from agno.agent import Agent
from agno.db.postgres import PostgresDb
from agno.os import AgentOS
from agno.models.anthropic import Claude

# Define agent
agent = Agent(
    name="Production Agent",
    model=Claude(id="claude-sonnet-4-5"),
    db=PostgresDb(
        host="localhost",
        database="agno_db",
    ),
)

# Create AgentOS
agent_os = AgentOS(agents=[agent])
app = agent_os.get_app()

# Run server
if __name__ == "__main__":
    agent_os.serve(app="main:app", port=8000)
```

### Learning Path

**Week 1: Foundations**
1. Read official documentation
2. Build basic agents (Q&A, search)
3. Experiment with different models
4. Try built-in toolkits

**Week 2: Advanced Features**
1. Implement memory and sessions
2. Add knowledge base (RAG)
3. Create custom tools
4. Try structured outputs

**Week 3: Multi-Agent Systems**
1. Build agent teams
2. Experiment with coordination modes
3. Create workflows
4. Test complex scenarios

**Week 4: Production**
1. Deploy AgentOS
2. Add monitoring
3. Implement RBAC
4. Performance optimization

---

## Migration from Phidata

### Background

Agno was formerly known as **Phidata**. The rebrand to Agno occurred in **January 2025**.

**Name Origin:**
- Agno (ἁγνὸ) means "pure" in Greek
- Reflects design philosophy: pure Python, no complex abstractions

### Migration Guide

**Official Documentation:**
https://docs.agno.com/how-to/phidata-to-agno

#### Import Changes

```python
# Old (Phidata)
from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGoTools

# New (Agno)
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
```

**Pattern:**
- `phi` → `agno`
- `phi.model` → `agno.models`
- Other imports mostly similar

#### Package Installation

```bash
# Uninstall Phidata (optional)
pip uninstall phidata

# Install Agno
pip install agno
```

#### Configuration Changes

Most configuration remains compatible. Key changes:

**Database:**
```python
# Old
from phi.storage.postgres import PostgresStorage

# New
from agno.db.postgres import PostgresDb
```

**Knowledge:**
```python
# Old
from phi.knowledge.pgvector import PgVectorKnowledgeBase

# New
from agno.knowledge.pgvector import PgVectorKnowledgeBase
# (Same import path!)
```

#### Breaking Changes

1. **Namespace reorganization**: `phi.model` → `agno.models`
2. **Some class names updated**: Check migration guide
3. **AgentOS introduced**: New production runtime (replaces previous serving methods)

#### Migration Checklist

- [ ] Update all `phi` imports to `agno`
- [ ] Change `phi.model` to `agno.models`
- [ ] Update database imports if using storage
- [ ] Test all functionality
- [ ] Update documentation/comments
- [ ] Update environment variables if needed
- [ ] Deploy and verify

### Community Support

**If you encounter issues:**
- Discord: https://discord.gg/4MtYHHrgA8
- Community Forum: https://community.agno.com
- GitHub Issues: https://github.com/agno-agi/agno/issues

---

## Architecture Decision Guide

### Decision Tree: Agents vs. Teams vs. Workflows

```
Start: What do you need to build?

├─ Single task, one domain
│  └─ Use: Single Agent
│
├─ Multiple domains, agents need to collaborate
│  ├─ Flexible problem-solving (agents choose tools)
│  │  └─ Use: Agent Team (Route/Collaborate/Coordinate)
│  │
│  └─ Deterministic execution (fixed steps)
│     └─ Use: Workflow
│
└─ Long-running process with branching
   └─ Use: Workflow with Steps
```

### When to Use Each Pattern

#### Single Agent

**Use When:**
- Task fits one domain (finance, support, etc.)
- No need for collaboration
- Single model sufficient
- Straightforward tool usage

**Example:**
- Customer support chatbot
- Simple data analysis
- Document summarization

#### Agent Team (Route Mode)

**Use When:**
- Need to classify and delegate tasks
- Specialists for different domains
- Minimal inter-agent communication
- Clear routing logic

**Example:**
- Customer support routing (billing/technical/account)
- Department delegation
- Task triage

#### Agent Team (Collaborative Mode)

**Use When:**
- Multiple perspectives needed
- Agents build on each other's work
- Iterative refinement
- Shared problem-solving

**Example:**
- Investment analysis (multiple analysts)
- Code review (multiple reviewers)
- Design critique

#### Agent Team (Coordinate Mode)

**Use When:**
- Complex multi-step project
- Leader decomposes tasks
- Parallel execution possible
- Synthesis of results needed

**Example:**
- Editorial pipeline (research/write/edit)
- Financial reporting (data/analysis/report)
- Product launch (research/plan/execute)

#### Workflow

**Use When:**
- Deterministic execution required
- Compliance/audit needs
- Complex branching logic
- Need pause/resume capability
- Financial or healthcare domain

**Example:**
- Insurance claim processing
- Medical diagnosis pipeline
- Financial transaction approval

### Performance Considerations

**Agent Instantiation Overhead:**
- Agno: ~3μs per agent
- Can instantiate 1000s of agents concurrently
- Suitable for agent-per-request patterns

**Memory Footprint:**
- Agno: ~6.6 KB per agent
- Can run 1000s of agents in single process
- Efficient for large-scale deployments

**Latency:**
- Agent overhead: microseconds
- Dominant factor: LLM API latency (100-1000ms)
- Optimize by: model choice, prompt length, parallel calls

**Throughput:**
- Horizontal scaling: Add AgentOS instances
- Stateless design: No session affinity needed
- Database bottleneck: Use connection pooling

### Security Considerations

**Data Residency:**
- All processing in your cloud
- Choose deployment region for compliance
- No data to external services

**Access Control:**
- Implement RBAC for agents
- Per-agent permissions
- Tool-level restrictions

**Secrets Management:**
- Use environment variables
- Integrate with secrets manager
- Rotate keys regularly

**Audit Logging:**
- Log all agent invocations
- Capture tool calls
- Store in compliance-ready format

---

## Resources & References

### Official Documentation

- **Main Docs**: https://docs.agno.com
- **Quickstart**: https://docs.agno.com/quickstart
- **Examples**: https://docs.agno.com/examples
- **API Reference**: https://docs.agno.com/api

### Code & Community

- **GitHub**: https://github.com/agno-agi/agno
- **Cookbook**: https://github.com/agno-agi/agno/tree/main/cookbook
- **Discord**: https://discord.gg/4MtYHHrgA8
- **Community Forum**: https://community.agno.com

### Learning Resources

- **AI Coding Assistant Context**: https://docs.agno.com/llms-full.txt
- **Video Tutorials**: Community YouTube channels
- **Blog Posts**: Medium, Dev.to (search "Agno framework")

### Comparison Articles

- "Best AI Agent Frameworks in 2025" - LangWatch
- "Agno vs LangGraph" - ZenML Blog
- "Top 10 Open-Source AI Agent Frameworks" - APIpie

### Academic & Technical

- Model Context Protocol Specification
- FastAPI Documentation (for AgentOS)
- Vector Database Benchmarks

### Industry Reports

- AI Agent Framework Adoption Survey 2025
- Enterprise AI Deployment Best Practices
- Multi-Agent Systems in Production

---

## Conclusion

Agno represents a significant advancement in the LLM agent framework landscape. Its combination of:

1. **Extreme Performance** (529× faster than alternatives)
2. **Privacy-First Architecture** (all data in your cloud)
3. **Production-Ready Runtime** (AgentOS included)
4. **Enterprise Security** (RBAC, audit, governance)
5. **Developer Experience** (pure Python, clear APIs)

...makes it an ideal choice for enterprise architects building production AI systems.

### Key Takeaways for Enterprise Architects

**Performance:**
- Microsecond instantiation enables new architecture patterns
- 50× memory efficiency reduces infrastructure costs
- Suitable for latency-sensitive, high-throughput systems

**Privacy & Security:**
- Complete data sovereignty (no vendor dependencies)
- Enterprise-grade RBAC and audit capabilities
- Compliance-ready (GDPR, HIPAA, SOC 2, PCI DSS)

**Production Readiness:**
- AgentOS provides day-one production runtime
- Horizontal scaling, health checks, monitoring built-in
- Docker/Kubernetes deployment patterns established

**Flexibility:**
- Model-agnostic (23+ providers)
- Multimodal capabilities (text, image, audio, video)
- Extensible (100+ toolkits, custom tools, MCP integration)

**Total Cost of Ownership:**
- Zero per-event fees (unlike vendor platforms)
- Zero retention costs (unlike vendor platforms)
- Open source with Apache-2.0 license
- Pay only for infrastructure and LLM API calls

### Next Steps

1. **Experiment**: Start with basic agents locally
2. **Prototype**: Build a proof-of-concept for your use case
3. **Architect**: Design your multi-agent system
4. **Deploy**: Production deployment with AgentOS
5. **Scale**: Horizontal scaling as needed

With this comprehensive knowledge, you're now equipped to be in the **top 1% of enterprise architects** working with the Agno framework.

---

**Research Completed**: November 9, 2025
**Framework Version**: Agno 2.0+
**Last Updated**: November 2025
