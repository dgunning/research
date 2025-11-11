# Research Notes: Claude Agent SDK Deep Dive

## Project Start: 2025-11-11

### Initial Prompt
Do a deep dive into claude agent sdk

### Research Plan
1. Understand what the Claude Agent SDK is and its purpose
2. Explore architecture, design patterns, and core concepts
3. Investigate the agentic framework and tool use
4. Analyze practical use cases and implementation patterns
5. Create examples and templates
6. Document best practices and advanced techniques

---

## Session Notes

### Initial Research Findings

**What is the Claude Agent SDK?**
- Released September 29, 2025 alongside Claude Sonnet 4.5
- Renamed from "Claude Code SDK" to "Claude Agent SDK"
- Built on the agent harness that powers Claude Code
- Provides building blocks for production-ready AI agents
- Available for Python (3.10+) and TypeScript/Node (18+)

**Core Design Principle:**
"Give your agents a computer" - allows agents to work like humans do by providing:
- Bash command execution
- File operations (read, write, edit, search)
- Web search capabilities
- Custom tool integration via MCP

**Key Features:**
1. **Context Management** - Automatic compaction, semantic search, subagents
2. **Rich Tool Ecosystem** - File operations, code execution, web search, MCP extensibility
3. **Advanced Permissions** - Fine-grained control over agent actions
4. **Production Essentials** - Built-in error handling, session management

**The Agent Loop:**
1. Gather context (search, read files, organize information)
2. Take action (execute commands, call tools, write code)
3. Verify work (validate output, check results, iterate)

**Available Tools:**
- Bash - Run shell commands
- Glob - Pattern matching for files
- Grep - Search file contents (uses ripgrep)
- Read - Read file contents
- Write - Create new files
- Edit/MultiEdit - Modify existing files
- NotebookRead/NotebookEdit - Jupyter notebook operations
- WebFetch - Fetch web content
- WebSearch - Search the web
- TodoRead/TodoWrite - Task management

**Model Context Protocol (MCP):**
- Open standard for connecting LLMs to external systems
- Introduced November 2024
- Adopted by OpenAI in March 2025
- Pre-built servers for: Google Drive, Slack, GitHub, Git, Postgres, Puppeteer
- Three connection types: stdin/stdout, HTTP, SSE (deprecated)
- Configuration via .mcp.json

**Use Cases:**
- Finance agents analyzing portfolios
- Personal assistants managing calendars and travel
- Customer support handling complex requests
- Research agents synthesizing documents
- Development tools and automation

**Context Management Strategies:**
1. **Agentic search** - Agents navigate folder structures with grep, tail
2. **Semantic search** - Fast but trades accuracy for speed
3. **Subagents** - Parallel processing, context compartmentalization
4. **Compaction** - Automatic summarization to prevent token exhaustion

**Verification Methods:**
1. **Rules-based feedback** - Linting, validation criteria
2. **Visual feedback** - Screenshots for UI verification
3. **LLM-as-judge** - Secondary models evaluate quality

---

### Documentation Created

**1. 01-fundamentals.md** (~9,000 words)
- What is the Claude Agent SDK
- Core philosophy and design principles
- Key concepts (agent loop, context management, tools, hooks)
- Architecture overview
- Installation and setup
- Quick start examples
- Understanding messages

**2. 02-tools-and-capabilities.md** (~12,000 words)
- Complete built-in tools reference
  - File operations (Read, Write, Edit, Glob, Grep)
  - Command execution (Bash)
  - Web interaction (WebFetch, WebSearch)
  - Specialized tools (Notebooks, Todos)
- Tool configuration and permissions
- Creating custom tools (in-process MCP)
- External MCP servers
- Tool best practices
- Performance optimization
- Error handling

**3. 03-advanced-patterns.md** (~9,000 words)
- Context management strategies in detail
  - Agentic search
  - Semantic search
  - Subagents
  - Automatic compaction
  - Hybrid approaches
- The agent loop in practice (gather, act, verify)
- Advanced tool patterns
  - Parallel execution
  - Conditional use
  - Tool chaining
  - Error recovery
- Production best practices
  - Error handling
  - Logging and monitoring
  - Rate limiting
  - Timeouts
  - Graceful shutdown
- Performance optimization techniques

### Example Code Created

**examples/01_simple_query.py**
- Simple query() function usage
- Code analysis example
- Data processing example
- Demonstrates the easiest way to use the SDK

**examples/02_bidirectional_client.py**
- Basic conversation patterns
- Multi-turn tasks
- Constrained agents (tool restrictions)
- Working directory configuration
- Message inspection

**examples/03_custom_tools.py**
- Custom tool definition with @tool decorator
- Creating MCP servers
- Calculator tool
- Note-taking tools (store/list notes)
- Combining built-in and custom tools

**examples/04_subagents.py**
- Parallel file analysis with subagents
- Data processing with subagents
- Hierarchical agent structures
- Load-balanced subagents
- Real-world parallelization patterns

**examples/README.md**
- Overview of all examples
- Prerequisites and setup
- Running instructions
- Common patterns reference
- Troubleshooting guide

### Comprehensive README Created

**README.md** (~15,000 words)
- Executive summary
- Complete overview of Claude Agent SDK
- Core architecture and message flow
- The agent loop (detailed)
- Tools ecosystem summary
- Context management strategies
- Model Context Protocol (MCP)
- Advanced patterns
- Production best practices
- Example code overview
- Use cases (finance, personal assistant, customer support, dev, research)
- Getting started guide
- Learning path
- Resources and links

### Key Insights from Research

**Architecture:**
- SDK acts as bridge between application and Claude Code CLI
- Claude Code CLI manages communication with Claude AI model
- Message-based communication (user, assistant, system, result)
- Tools executed by SDK, results fed back to Claude
- Iterative process until task completion

**Core Design Decisions:**
- "Give agents a computer" - general-purpose tools vs. rigid actions
- In-process MCP servers preferred (performance, simplicity)
- Automatic context management (compaction)
- Subagents for parallelization and context isolation
- Built on production-tested Claude Code harness

**Tool Ecosystem Design:**
- Specialized tools preferred over Bash for common operations
- Read before Write/Edit pattern for safety
- Grep uses ripgrep (all users have it pre-installed)
- Bash for actual shell operations only
- Web tools integrated directly (WebFetch, WebSearch)

**Context Management Philosophy:**
- Multiple strategies for different use cases
- Agentic search = accuracy, transparency
- Semantic search = speed, scale
- Subagents = parallelization, isolation
- Automatic compaction = long-running tasks
- Hybrid approaches often optimal

**Production Considerations:**
- Error handling crucial (CLINotFoundError, ProcessError, etc.)
- Logging and monitoring essential
- Rate limiting prevents overwhelming systems
- Graceful shutdown for long-running agents
- Performance optimization through parallelization

**MCP Adoption:**
- Introduced by Anthropic November 2024
- Adopted by OpenAI March 2025
- Growing ecosystem of pre-built servers
- Standardizes LLM-to-tool integration
- In-process preferred for performance

### Research Methodology

1. Web searches for official documentation and blog posts
2. Fetched content from Anthropic's engineering blog
3. Analyzed GitHub repositories (Python SDK)
4. Studied tutorials and community resources
5. Synthesized information into comprehensive documentation
6. Created practical examples demonstrating key concepts
7. Organized findings into actionable guides

### Files Generated

Total: 9 files
- 1 notes file (this file)
- 3 comprehensive documentation files (~30,000 words)
- 4 working Python examples (~1,000 lines)
- 1 examples README
- 1 project README (comprehensive research report)

All examples are executable and demonstrate real SDK usage patterns.

