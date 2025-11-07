# MCP (Model Context Protocol) Research Notes

## Original Prompt
> I want to be the most knowledgeable techie in Toronto when it comes to MCP - Model Context Protocol so when I have an interview or a discussion with VP, managers or directors, both business and technically I can have clearly speak authoritively at any level. Do indepth research on MCP - what it is, typical uses, comparisons to REST or other tech, comparisons to Skills. Current best practices like code mode (from Cloudflare) and the latest from anthropic on making agents more efficient.

## Research Log

### Session Start: 2025-11-07

#### Initial Setup
- Created research folder: mcp-model-context-protocol-research/
- Starting comprehensive research on Model Context Protocol

#### Research Goals
1. Understand MCP fundamentals and architecture
2. Identify typical use cases and applications
3. Compare MCP to traditional protocols (REST, GraphQL, etc.)
4. Compare MCP to Skills-based approaches
5. Document current best practices (Cloudflare code mode, etc.)
6. Study latest Anthropic agent efficiency guidance
7. Prepare both technical and business-level explanations

---

## Research Findings

### What is MCP? (Fundamentals)

**Definition:**
- Model Context Protocol (MCP) is an open-source standard introduced by Anthropic in November 2024
- Standardizes how AI systems (LLMs) integrate and share data with external tools, systems, and data sources
- Open protocol for connecting AI assistants to systems where data lives
- NOT a replacement for REST/GraphQL but a higher-level orchestration layer built on top

**The Problem It Solves:**
- **N×M Integration Problem**: Before MCP, each AI model + data source required custom integration
- Without MCP: Each combination of model and tool demands custom implementation
- With MCP: Single standard protocol transforms N×M problem into M+N problem
- Eliminates fragmented integrations, data silos, and legacy system isolation

**Timeline:**
- November 2024: Introduced by Anthropic
- March 2025: OpenAI officially adopted MCP (integrated into ChatGPT desktop, Agents SDK, Responses API)
- April 2025: Google DeepMind (Demis Hassabis) confirmed MCP support in Gemini models
- April 2025: Microsoft partnered with Anthropic for official C# SDK
- By February 2025: Over 1,000 open-source connectors created

**Industry Adoption:**
- Block (Square), Apollo, Zed, Replit, Codeium, Sourcegraph
- Claude Desktop, Cursor IDE, Windsurf IDE
- OpenAI, Google DeepMind, Microsoft

---

### Architecture (Technical Deep-Dive)

**Core Components (Client-Host-Server Architecture):**

1. **Host**
   - The LLM application (IDE, Chatbot, etc.)
   - Examples: Claude Desktop, Cursor IDE, Windsurf IDE
   - Can run multiple client instances

2. **Client**
   - Lives within the host
   - Converts user requests into structured format
   - 1:1 relationship with MCP server (but multiple clients per host)
   - Handles tool discovery and invocation

3. **Server**
   - Exposes data through three mechanisms:
     - **Resources**: Information retrieval from databases
     - **Tools**: Operations that perform side effects (calculations, API calls)
     - **Prompts**: Reusable templates and workflows for LLM-server communication

4. **Transport Layer**
   - Handles communication between clients and servers
   - Uses JSON-RPC 2.0 to exchange messages
   - Supports multiple transport mechanisms (stdio, HTTP)

**Protocol Foundation:**

**JSON-RPC 2.0:**
- All messages follow JSON-RPC 2.0 specification
- Provides standardization, simplicity, human-readable format
- Easily parsed across programming languages
- Transport layer converts MCP messages to/from JSON-RPC format

**Transport Mechanisms:**

1. **stdio (Standard Input/Output)**
   - For local communication (same machine)
   - Host launches server as subprocess
   - Messages sent via stdin/stdout
   - Newline-delimited (must not contain embedded newlines)
   - Ideal for local tooling

2. **HTTP with Server-Sent Events (SSE)**
   - Client-to-Server: HTTP POST requests to MCP endpoint
   - Server-to-Client: SSE for streaming responses
   - "Streamable HTTP" allows dynamic upgrade to SSE when needed
   - Compatible with serverless environments

**Message Framing:**
- Simple: Newline separation
- Robust: Content-Length headers (`Content-Length: NNN\r\n\r\n`) followed by JSON payload
- Ensures accurate message delimitation for large messages

**Custom Transport:**
- Must implement Transport interface:
  - `start()`: Start processing messages
  - `send(message)`: Send JSON-RPC message
  - `close()`: Close connection
  - Callbacks: `onclose`, `onerror`, `onmessage`

**Design Inspiration:**
- Deliberately reuses message-flow ideas from Language Server Protocol (LSP)
- Stateful session protocol focused on context exchange
- Sampling coordination between clients and servers

---

### MCP vs REST/GraphQL (Protocol Comparison)

**Fundamental Difference:**
- REST/GraphQL: **Low-level web communication patterns** that expose operations on resources
- MCP: **High-level AI orchestration layer** that manages tool usage and maintains context
- They operate at different abstraction layers and serve different purposes

**Key Advantages of MCP:**

1. **AI-Native Design**
   - Built from ground up for LLMs
   - Standardizes how LLMs fetch context and use tools
   - REST designed for software-to-software, not AI-to-software

2. **Context Management**
   - MCP: Preserves conversational context across multiple tool uses
   - REST: Each call isolated, manual context passing required
   - MCP maintains one persistent conversation context

3. **Dynamic Tool Discovery**
   - MCP: Runtime discovery - clients query servers about capabilities
   - REST: Generally lacks dynamic discovery (relies on OpenAPI specs)
   - MCP agents discover tools as needed, not upfront

4. **Solves N×M Problem**
   - REST: Every model + API requires custom integration
   - MCP: Single standardized protocol for all integrations

5. **Context Window Optimization**
   - REST: Dumping OpenAPI spec causes context window bloat
   - MCP: Tools described efficiently with progressive disclosure

**The Relationship:**
- MCP doesn't replace REST - it builds on top of it
- REST excels at providing discrete services
- MCP excels at orchestrating those services for AI agents
- MCP servers frequently wrap REST API endpoints

**Analogy:**
- REST API = Individual roads between cities
- MCP = GPS navigation system that orchestrates route planning across roads

---

### MCP vs Skills (Comparison)

**What Are They?**

**MCP (Model Context Protocol):**
- A **protocol** - set of rules/standards for communication
- An integration standard / communication layer
- Provides AI systems with access to external data and tools
- Does NOT make decisions or plan actions
- Focus: Connecting AI to data in a unified way

**Skills (e.g., edgartools SKILL.md, Claude Skills):**
- A **capability** - pre-written code that agents can execute
- An agent framework feature
- Teaches agents HOW to use specific tools/libraries
- Contains reasoning patterns, workflows, examples
- Focus: Agent autonomy and task execution

**How They Work Together:**

Think of building AI agents like flying a plane:
- **Skills** = The pilot (makes decisions, reasons, adapts to conditions)
- **MCP** = Navigation system (provides maps, communication channels, instrument data)

You need BOTH:
- Skills enable complex, autonomous task execution
- MCP provides standardized access to data/tools that skills use

**Practical Example:**

Scenario: Research Atlanta Braves financial data

**Without MCP (Skills only):**
```python
# Skills guide the agent to use edgartools
from edgar import Company, set_identity
set_identity("Agent agent@example.com")
company = Company("BATRB")
# Skills teach: use to_context() for efficiency
print(company.to_context())
```

**With MCP:**
```
Agent: "Research Atlanta Braves"
→ MCP Server provides edgartools tool
→ Skills guide HOW to use the tool efficiently
→ MCP handles communication/data flow
→ Skills handle reasoning and multi-step workflow
```

**Key Differences:**

| Aspect | MCP | Skills |
|--------|-----|--------|
| Type | Protocol | Capability/Framework |
| Purpose | Data access | Task execution |
| Decision-making | No | Yes |
| Platform | Cross-platform standard | Often platform-specific |
| Examples | Google Drive MCP, GitHub MCP | Edgar research skills, file analysis skills |

**Complementary, Not Competing:**
- Advanced AI solutions use BOTH
- MCP removes custom connector burden (one protocol for all tools)
- Skills enable autonomous, multi-step reasoning
- Many frameworks combine both: LangChain, LlamaIndex, CrewAI use MCP for tool access

**Claude Skills vs MCP Specifically:**
- Claude Skills require Claude environment (agent framework + filesystem)
- Skills unique to Anthropic platform (though SDK open-sourced)
- Skills rely on model having tool execution enabled
- MCP is supplier-neutral, works across platforms

---

### Use Cases (Real-World Applications)

**Top 10 Use Cases:**

1. **Customer Support & Conversational AI**
   - Maintains long-term memory across sessions
   - Remembers order history, preferences, prior issues
   - Context persists between conversations

2. **Cross-Platform Experiences**
   - Context travels with user across devices
   - Example: Book flight on app → manage via voice assistant
   - Seamless experience across web, mobile, voice

3. **Enterprise System Integration**
   - Connects siloed systems (ERPs, CRMs, databases)
   - Example: Sales AI pulls from Salesforce + Oracle ERP
   - Unified view across previously isolated systems

4. **AI-Assisted Software Development**
   - IDEs, coding platforms (Replit, Cursor, Windsurf)
   - Code intelligence tools (Sourcegraph, Codeium)
   - Real-time access to project context, codebase

5. **Personalized Education**
   - Tracks learning state, goals, performance
   - AI tutors adjust lessons based on past interactions
   - Learning context persists across apps/platforms

6. **Data Analysis & Business Intelligence**
   - Connect to multiple data sources simultaneously
   - Query across databases, APIs, spreadsheets
   - Unified analysis without custom ETL pipelines

7. **Content Management & Knowledge Work**
   - Access Google Drive, Slack, Notion, Confluence
   - Cross-platform search and content retrieval
   - Context-aware document generation

8. **DevOps & Infrastructure Management**
   - Interact with Git, Docker, Kubernetes
   - Monitor systems, manage deployments
   - Natural language infrastructure operations

9. **Financial Services & Payments**
   - Stripe integration: invoices, customers, refunds
   - Banking systems, transaction processing
   - Secure, auditable financial operations

10. **Research & Information Retrieval**
    - Web search (Brave Search MCP)
    - Academic databases, arxiv, papers
    - Multi-source research compilation

**Example Implementations:**

**Official Reference Servers:**
- Everything: Test server with prompts, resources, tools
- Fetch: Web content fetching
- Filesystem: Secure file operations
- Git: Repository manipulation tools
- Memory: Knowledge graph-based persistent memory

**Popular Pre-Built Servers:**
- Google Drive, Slack, GitHub, Postgres
- Puppeteer (browser automation)
- Stripe (payments)
- Brave Search (privacy-focused search)

**Real-World Example:**
```
User: "Find distance between office and airport"
→ MCP Google Maps server called
→ Returns: "23.4 miles, 35 minutes"
```

---

### Code Mode / Code Execution (Best Practice)

**What is Code Mode?**

Introduced by Cloudflare, validated by Anthropic as best practice for MCP efficiency.

**Core Concept:**
- Convert MCP tools into **TypeScript API**
- Ask LLM to **write code** that calls the API
- Instead of: Direct tool calls with every intermediate result through LLM
- Provides: Local code execution that filters/transforms before returning to LLM

**Why It Works:**

1. **LLMs Excel at Code**
   - "LLMs are better at writing code to call MCP than at calling MCP directly"
   - Enormous amount of real-world TypeScript in training data
   - vs. Small set of contrived tool-calling examples

2. **Dramatic Efficiency Gains**
   - Example: 150,000 tokens → 2,000 tokens (98.7% savings!)
   - Reduces time and cost massively
   - Improves latency (reduces "time to first token")

**Problems Solved:**

**1. Tool Definition Overload**
- Traditional: All tools loaded upfront → hundreds of thousands of tokens
- Code Mode: Progressive discovery via filesystem navigation
- Load tools on-demand by reading specific files

**2. Intermediate Result Bloat**
- Traditional: Every result flows through LLM context
- Example: 2-hour meeting transcript = 50,000+ redundant tokens
- Code Mode: Filter/transform locally, return only relevant data

**Implementation Pattern:**

**Filesystem Structure:**
```
servers/
├── google-drive/
│   ├── getDocument.ts
│   ├── searchFiles.ts
│   └── index.ts
├── salesforce/
│   ├── updateRecord.ts
│   ├── searchContacts.ts
│   └── index.ts
```

**Agent Workflow:**
1. Explore directories to discover available tools
2. Read specific tool files only when needed
3. Write code that calls multiple tools
4. Execute code locally with access to MCP bindings
5. Return only filtered/transformed results to LLM

**Key Benefits:**

1. **Progressive Disclosure**
   - Navigate filesystem naturally
   - `search_tools` function with detail levels (name only, name+description, full schema)
   - Load definitions incrementally

2. **Context-Efficient Data Processing**
   ```typescript
   const pendingOrders = allRows.filter(row =>
     row["Status"] === 'pending'
   );
   // Instead of flowing 10,000 rows through context
   ```

3. **Control Flow Efficiency**
   - Loops, conditionals, error handling execute locally
   - No LLM round-trip for each step
   - Reduced latency

4. **Privacy-Preserving Operations**
   - Sensitive data stays in execution environment
   - Automatic PII tokenization
   - Data flows source→destination without model exposure

5. **State Persistence & Skills**
   - Save intermediate results to files
   - Build reusable function library
   - Resume work across sessions

**Cloudflare Implementation:**

**Agents SDK with Code Mode:**
- Automatically fetches MCP schemas
- Generates TypeScript interfaces from schemas
- Provides sandboxed V8 isolate execution

**Security:**
- Each code execution in isolated V8 environment
- No internet access from sandbox
- Secure API bindings restrict to MCP-backed APIs only
- Millisecond startup times (not containers)
- Minimal memory footprint (megabytes)

**Worker Loader API:**
- Dynamic isolate creation
- Code executes with restricted connectivity
- Network requests throw errors except through MCP bindings
- Prevents API key leakage
- Clear authorization boundaries

**Critical Trade-offs:**
- Introduces complexity
- Requires secure sandboxing infrastructure
- Resource limits and monitoring needed
- Benefits must outweigh implementation costs
- Not suitable for all use cases

---

### Anthropic Agent Efficiency Best Practices

**Context Management & Token Efficiency:**

1. **Load Tools On-Demand**
   - Don't load all tool definitions upfront
   - Use progressive disclosure
   - `search_tools` with detail level parameter (name only, name+description, full schema)

2. **Filter Data Locally**
   - Use code execution to filter before returning to model
   - Return only relevant results, not raw dumps
   - Example: Filter 10,000 rows → return 50 matching records

3. **Token Usage = 80% of Performance**
   - "Token usage by itself explains 80% of variance in agent performance on complex tasks"
   - Latest Claude models = large efficiency multipliers
   - Claude Sonnet 4 upgrade > doubling token budget on Sonnet 3.7

**Tool Design Best Practices:**

1. **Fewer, Better Tools**
   - Too many tools distract agents
   - Consolidate multi-step workflows into single tools
   - Example: `schedule_event` instead of separate `list_users`, `list_events`, `create_event`

2. **Namespacing**
   - Group related tools with common prefixes
   - By service: `asana_search`, `jira_search`
   - By resource: `asana_projects_search`, `asana_users_search`
   - Helps agents select right tools at right time

3. **Targeted Search > List All**
   - Implement `search_contacts` not `list_contacts`
   - Respect limited context windows
   - Avoid forcing agents to read through all results

4. **Semantic Over Technical**
   - Return `name` and `image_url` not `uuid` and `256px_image_url`
   - Resolving UUIDs to meaningful language improves precision
   - Prioritize semantic meaning over technical identifiers

5. **Response Format Control**
   - Expose `response_format` enum: "concise" or "detailed"
   - Let agents request appropriate level based on needs
   - Balance flexibility with token efficiency

6. **Helpful Error Messages**
   - Communicate specific, actionable improvements
   - Not opaque error codes
   - Encourage targeted searches over broad queries

7. **Thorough Descriptions**
   - Tool descriptions loaded into agent context
   - Make implicit context explicit
   - Define specialized query formats, terminology
   - Small refinements = dramatic performance improvements

**Multi-Agent Architectures:**

Scale complexity with agent count:
- **Simple fact-finding**: 1 agent, 3-10 tool calls
- **Direct comparisons**: 2-4 subagents, 10-15 calls each
- **Complex research**: 10+ subagents, clearly divided responsibilities

**Search Strategy:**
- Mirror expert human research
- Start with short, broad queries
- Evaluate what's available
- Progressively narrow focus

**Agent Skills for Reusability:**

- Pre-written code executes without loading into context
- Operations better suited for traditional code (sorting, calculations)
- Improves efficiency AND reliability
- Builds persistent toolkit over time

---

### Security Concerns (Critical Awareness)

**Major Vulnerabilities Identified (2025):**

1. **Prompt Injection**
   - LLMs trust anything sending convincing tokens
   - Extremely vulnerable to "confused deputy" attacks
   - Malicious inputs manipulate AI behavior
   - Results: Unauthorized transactions, data leaks, system compromises

2. **Command Injection & RCE**
   - **43% of open-source MCP servers** suffer from command injection
   - Fundamental vulnerabilities resurfacing in modern tech
   - Security researchers "surprised RCE still emerging in 2025"

3. **Critical CVEs:**
   - **CVE-2025-6514**: 437,000+ downloads affected (single npm package)
   - **CVE-2025-49596**: RCE in Anthropic's MCP Inspector (browser-based attacks)
   - **CVE-2025-53967**: Figma MCP arbitrary code execution

4. **File System Vulnerabilities**
   - 33% allow unrestricted URL fetches
   - 22% leak files outside intended directories
   - Path traversal attacks

5. **Tool Poisoning**
   - Adversaries exploit trust in MCP tool metadata
   - Harmful commands embedded in metadata
   - Difficult to detect through routine inspection
   - Lookalike tools silently replace trusted ones

6. **Exploit Probability:**
   - **10 MCP plugins = 92% probability of exploitation**
   - 3 interconnected servers = 50%+ risk
   - Even single MCP plugin = 9% exploit probability

**Real-World Incidents:**

- **Mid-2025**: Supabase Cursor agent (privileged access) breached via prompt injection in support tickets
- Multiple CVEs with hundreds of thousands of downloads affected

**Mitigation Recommendations:**

1. **Human in the Loop (CRITICAL)**
   - MCP spec says "SHOULD always have human in loop"
   - Experts: Treat "SHOULD" as "MUST"
   - Require approval for tool invocations

2. **Strict Input Validation**
   - Enforce validation on all inputs
   - Use parameterized queries
   - Prevent injection attacks

3. **Sandboxing**
   - Run local MCP servers in sandboxes
   - Only allow explicitly permitted actions/access
   - Restrict file system access

4. **Principle of Least Privilege**
   - Deploy focused MCP servers with narrow permissions
   - Reduces over-privileged access risk
   - Easier to manage and audit

5. **Security Patches**
   - Apply patches promptly
   - Monitor security advisories
   - Keep dependencies updated

6. **Audit & Monitoring**
   - Log all tool invocations
   - Monitor for suspicious patterns
   - Regular security reviews

**State of MCP Security:**
- "MCP security remains significant concern as adoption accelerates"
- Regression in security fundamentals
- Critical need for security-first development

---

### Technical Implementation Details

**SDKs Available:**
- Python, TypeScript/JavaScript, C#, Go, Rust
- Community-built SDKs for additional languages
- Microsoft official C# SDK (April 2025)

**Building MCP Servers:**

**Minimal Server Structure:**
```typescript
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";

const server = new Server({
  name: "my-mcp-server",
  version: "1.0.0"
}, {
  capabilities: {
    resources: {},
    tools: {},
    prompts: {}
  }
});

// Define tools
server.setRequestHandler(ListToolsRequestSchema, async () => ({
  tools: [{ name: "my_tool", description: "...", inputSchema: {...} }]
}));

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  // Handle tool execution
});

const transport = new StdioServerTransport();
await server.connect(transport);
```

**Custom Transport Implementation:**
```typescript
interface Transport {
  start(): Promise<void>;
  send(message: JSONRPCMessage): Promise<void>;
  close(): Promise<void>;
  onclose?: () => void;
  onerror?: (error: Error) => void;
  onmessage?: (message: JSONRPCMessage) => void;
}
```

**Tool Definition Best Practices:**
```typescript
{
  name: "search_contacts",  // Not "list_contacts"
  description: "Search contacts by name, email, or company. Returns matching contacts only.",
  inputSchema: {
    type: "object",
    properties: {
      query: {
        type: "string",
        description: "Search term to match against contact name, email, or company"
      },
      limit: {
        type: "number",
        description: "Maximum results to return (default: 10, max: 50)",
        default: 10
      },
      response_format: {
        type: "string",
        enum: ["concise", "detailed"],
        description: "concise: names and emails only; detailed: includes all fields"
      }
    },
    required: ["query"]
  }
}
```

**Integration Example (Claude Desktop):**
```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/allowed/path"]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "your-token"
      }
    }
  }
}
```

---

### Business Value Propositions

**For Executive-Level Discussions:**

**The Problem:**
"Every new AI integration requires custom development. With 50 data sources and 10 AI models, that's 500 custom integrations to build and maintain. MCP transforms this into 60 integrations (50 + 10)."

**The Solution:**
"MCP is like USB for AI - one standard connector that works everywhere. Just as USB eliminated the need for different cables for every device, MCP eliminates custom AI integrations."

**Business Impact:**

1. **Reduced Development Costs**
   - 90%+ reduction in integration development
   - One MCP server serves all AI applications
   - No custom connector per model/tool combination

2. **Faster Time to Market**
   - New AI features deploy in days, not months
   - Reuse existing MCP servers
   - Plug-and-play AI capabilities

3. **Vendor Independence**
   - Not locked into single AI provider
   - OpenAI, Anthropic, Google all support MCP
   - Switch providers without rewriting integrations

4. **Future-Proof Architecture**
   - Industry-wide standard (not proprietary)
   - 1,000+ open-source servers available
   - Community innovation benefits entire ecosystem

5. **Security & Governance**
   - Centralized permission management
   - Audit all AI data access
   - Fine-grained control over capabilities

**ROI Example:**
```
Traditional Approach:
- 5 AI tools × 20 data sources = 100 custom integrations
- 2 weeks per integration × $150/hour × 40 hours = $300,000
- Annual maintenance: $100,000

MCP Approach:
- 20 MCP servers (one per data source) = 20 integrations
- 2 weeks × $150/hour × 40 hours × 20 = $120,000
- Annual maintenance: $20,000
- SAVINGS: $180,000 first year, $80,000 annually
```

**Competitive Advantage:**
- Faster AI feature deployment than competitors
- Lower cost per AI capability
- More robust and maintainable architecture
- Attracts AI talent (modern, standard approach)

**Risk Mitigation:**
- Reduces technical debt
- Eliminates integration complexity
- Industry-standard approach (not experimental)
- Major vendors already committed (OpenAI, Google, Microsoft, Anthropic)

---

### For Different Audience Levels

**For VPs & Directors (Business Focus):**

"MCP solves the AI integration problem. Instead of building custom connectors for every combination of AI model and data source, MCP provides a universal standard—like USB for AI. This reduces development costs by 90%, accelerates time to market, and future-proofs our architecture as the industry consolidates around this standard. OpenAI, Google, and Microsoft have all committed to MCP."

**For Technical Managers:**

"MCP is an open protocol built on JSON-RPC 2.0 that standardizes how AI agents access tools and data. It uses a client-server architecture where MCP servers expose resources, tools, and prompts through a unified interface. The key innovation is code execution mode - instead of direct tool calls that bloat context, agents write TypeScript code that executes locally, achieving 98% token savings. We can deploy MCP servers via stdio for local tools or HTTP+SSE for cloud services."

**For Senior Engineers:**

"MCP implements a stateful session protocol over JSON-RPC 2.0, deliberately mirroring LSP's message-flow patterns. Transport layer abstracts stdio vs HTTP+SSE, enabling local subprocesses or distributed deployments. The real efficiency comes from progressive disclosure—tools organized in filesystem hierarchy, agents navigate and load definitions on-demand. Code execution mode runs agent-generated TypeScript in sandboxed V8 isolates with secure bindings, filtering/transforming data locally before context injection. Critical implementation details: implement Transport interface with proper lifecycle management, namespace tools by service/resource, expose response_format params for context optimization."

**For Security Teams:**

"MCP introduces attack vectors: prompt injection (43% of servers vulnerable to command injection), tool poisoning via metadata manipulation, path traversal (22% leak files outside intended directories). CVE-2025-6514 affected 437k+ downloads. Mitigation requires: mandatory human-in-the-loop approvals (treat spec SHOULDs as MUSTs), sandboxed execution with explicit allowlists, principle of least privilege per server, strict input validation, and comprehensive audit logging. 10 MCP plugins = 92% exploit probability—deploy narrowly-scoped servers only."

---

