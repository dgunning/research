# Agno Framework Research Notes

## Research Goal
Deep dive investigation of the Agno framework to achieve top 1% knowledge for enterprise architecture applications.

## Investigation Started
2025-11-09

## Research Progress

### Initial Research
- Starting with web search to understand what Agno is
- Will investigate documentation, architecture, features, and use cases

### Key Findings So Far

**What is Agno?**
- Multi-agent framework, runtime and control plane
- Built for speed, privacy, and scale
- Formerly known as Phidata (rebranded)
- Released Nov 7, 2025 (latest version)
- Apache-2.0 license

**Performance Metrics (Oct 2025 - M4 MacBook Pro):**
- Instantiation: ~3μs (529× faster than LangGraph, 57× faster than PydanticAI, 70× faster than CrewAI)
- Memory: 6.6 KiB (24× lower than LangGraph, 4× lower than PydanticAI, 10× lower than CrewAI)

**Core Capabilities:**
1. Agents - memory, knowledge, sessions, HITL, guardrails, MCP support
2. Multi-Agent Teams - autonomous operation under team leader
3. Step-based Workflows - deterministic sequential/parallel/conditional execution

**AgentOS Runtime:**
- Production-ready FastAPI application
- Stateless, horizontally scalable
- Integrated control plane (AgentOS UI) for monitoring
- Runs entirely in user infrastructure (privacy-first)
- No external data transmission

**Model Support:**
- Model-agnostic (23+ LLM providers)
- OpenAI, Anthropic, Groq, Google, Hugging Face
- Multimodal (text, images, audio, video, files)

### Memory & Knowledge Management Research

**Memory System:**
- Store user sessions and agent state in databases
- Built-in memory allows agents to recall user-specific context across sessions
- Database persistence (SqliteDb, PostgreSQL, etc.)

**Knowledge & RAG:**
- Agentic RAG by default - agents search knowledge base for specific information
- Knowledge = domain-specific information stored in vector databases
- Searching on demand = Agentic RAG pattern
- 20+ vector stores supported (PgVector, ChromaDB, LanceDB, Qdrant, MongoDB)
- Hybrid search + reranking out of the box
- Dynamic few-shot learning

### Workflows Research

**Workflow Architecture:**
- Step-based workflows for deterministic execution
- Steps can be Agents, Teams, or Python functions
- Execution patterns: sequential, parallel, loops, branches, conditional
- Stateful, multi-agent programs using plain Python

**Key Components:**
- Workflow class: Top-level orchestrator
- Step: Fundamental unit of work (Agent, Team, or function)
- Router: Branching logic specification

**Benefits:**
- Deterministic behavior
- State management
- Can be paused, resumed, and audited
- Easy debugging
- Composable Python-native code

### Multi-Agent Teams Research

**Coordination Modes:**
- Route mode: Simple delegation
- Collaborative mode: Agents work together
- Coordinate mode: Team leader delegates and synthesizes outputs

**Communication Patterns:**
- Team Leader and Team Members roles
- Clear instruction definition
- Context sharing across team
- Sequential processing with inter-agent communication

**Real-world Examples:**
- Finance-Risk teams (finance agent + risk assessment agent)
- Editorial teams (searcher + writer + editor)
- Market analysis teams (multiple domain experts)

### Toolkits & Tools

**Scale:**
- 100+ built-in toolkits
- Thousands of tools ready to use
- Covers data, code, web, and enterprise APIs

**Specific Toolkits:**
- Web: DuckDuckGoTools, ExaTools
- Finance: YFinanceTools
- Development: GithubTools, GiphyTools
- File system, database interaction
- Custom extensions supported

### MCP Integration

**Transport Types:**
- stdio (standard input/output) - default
- streamable HTTP
- SSE (Server-Sent Events)

**Integration Examples:**
- Filesystem agents
- GitHub integration
- Context7 MCP for programming docs
- Supabase, Airtable, and more

**Best Practices:**
- Close MCP connections when done
- Include proper error handling
- Use MCPTools or MultiMCPTools classes

### Framework Comparisons

**Agno vs LangGraph:**
- Agno: 529× faster instantiation, 24× lower memory
- Agno: Better for clarity, readable code, production consistency
- LangGraph: Better for complex stateful workflows at scale
- LangGraph: More flexible for interconnected multi-agent systems
- LangGraph: Steeper learning curve

**Agno vs CrewAI:**
- Agno: Higher performance, less memory usage
- CrewAI: More intuitive for beginners
- CrewAI: 30,000+ GitHub stars, strong community
- CrewAI: Better for simple role-based agent coordination
- Agno: Better for production applications

**When to Use:**
- Agno: Production apps, performance-critical, multimodal, clarity needed
- LangGraph: Complex workflows, scale, distributed systems
- CrewAI: Quick MVPs, beginners, simple role-based coordination

### AgentOS & Deployment Research

**AgentOS Overview:**
- Production-ready FastAPI application
- Stateless, horizontally scalable
- Async by default with minimal memory footprint
- SSE compatible endpoints
- Pre-built, ready for production on day 1

**Control Plane:**
- Integrated interface for visualization, monitoring, debugging
- Real-time agent activity monitoring
- Connects from browser directly to AgentOS in user's cloud
- No external data transmission

**Deployment:**
- Docker-based deployment
- Dockerized FastAPI application
- Postgres for session storage
- Port 8000 for API, 5432 for Postgres
- docker compose up -d for quick launch

**Performance:**
- Handles parallel/batch embedding generation
- Background task metrics collection
- Memory leak prevention focus
- Horizontal scaling support

### Enterprise & Security Research

**Privacy Architecture:**
- Runs entirely in user's cloud
- No data leaves the system
- Complete data privacy
- Ideal for security-conscious enterprises

**RBAC & Permissions:**
- Role-based access control (RBAC)
- Per-agent permissions
- Protect sensitive contexts and tools

**Data Governance:**
- User controls all data in agent databases
- No vendor lock-in
- Infinite retention with no retention costs
- Usage, logs, metrics stored in user environment

### Advanced Features Research

**Reasoning Capabilities:**
- Reasoning as first-class citizen
- ReasoningTools class available
- Separate Reasoning Agent for chain-of-thought
- Requires models with structured output support (GPT-4o, Claude-3.7-Sonnet, Gemini)

**Structured Outputs:**
- input_schema and output_schema enforcement
- Fully-typed responses
- Model-provided structured outputs
- JSON mode support

**Multimodal:**
- Text, image, audio, video input
- Text, image, audio, video output
- Native multimodal support

**Dynamic Context:**
- Runtime variable injection
- Context engineering
- Human-in-the-loop confirmations
- Lifecycle hooks for I/O transformation

### Code Examples Research

**Basic Agent:**
```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    description="You are a concise and helpful assistant.",
    markdown=True
)
agent.print_response("Your question here", stream=True)
```

**Finance Agent with Tools:**
```python
from agno.agent import Agent
from agno.models.anthropic import Claude
from agno.tools.reasoning import ReasoningTools
from agno.tools.yfinance import YFinanceTools

agent = Agent(
    model=Claude(id="claude-sonnet-4-20250514"),
    tools=[
        ReasoningTools(add_instructions=True),
        YFinanceTools(stock_price=True, analyst_recommendations=True),
    ],
    instructions="Use tables to display data.",
    markdown=True,
)
```

**MCP Integration:**
```python
from agno.agent import Agent
from agno.models.anthropic import Claude
from agno.tools.mcp import MCPTools

agno_agent = Agent(
    name="Agno Agent",
    model=Claude(id="claude-sonnet-4-5"),
    tools=[MCPTools(transport="streamable-http",
                    url="https://docs.agno.com/mcp")],
)
```

### Community & Ecosystem Research

**GitHub Stats (2025):**
- 26,000+ stars (June 2025)
- 3,000+ forks
- 3,000+ commits
- Rapid development pace

**Community Resources:**
- Discord server: discord.gg/4MtYHHrgA8
- Community forum: community.agno.com
- GitHub: github.com/agno-agi/agno
- Documentation: docs.agno.com
- Cookbook: 100+ examples

**History:**
- Formerly known as Phidata
- Rebranded to Agno in January 2025
- Agno (ἁγνὸ) means "pure" in Greek
- Migration guide available: docs.agno.com/how-to/phidata-to-agno

### Pricing & Hosting Research

**Cost:**
- Open-source and free
- No per-event fees
- No retention costs
- No external service fees
- Pay only for your cloud resources

**Hosting:**
- Self-hosted in user's cloud
- User controls all data
- AWS, GCP, Azure compatible
- Local development supported

### Real-World Use Cases

**Finance:**
- Real-time financial data access
- Trading agents
- Market analysis

**Logistics:**
- Route optimization
- Shipment tracking
- Operations automation

**Enterprise:**
- Climate data automation
- Compliance and disclosures
- AI-powered analytics
- Document processing

**Research Complete - Ready for README Compilation**
