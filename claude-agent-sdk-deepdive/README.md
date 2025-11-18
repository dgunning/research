# Claude Agent SDK: A Deep Dive

## Original Prompt

> Do a deep dive into claude agent sdk

## Executive Summary

The Claude Agent SDK is Anthropic's comprehensive framework for building production-ready AI agents, released September 29, 2025 alongside Claude Sonnet 4.5. Built on the same agent harness that powers Claude Code, it provides developers with powerful tools for creating autonomous agents that can plan, execute, and verify complex tasks.

**Key Findings:**
- The SDK embodies the principle "give agents a computer" - enabling agents to work like humans through file operations, command execution, and web access
- Supports both Python (3.10+) and TypeScript/Node.js (18+) with shared concepts
- Features automatic context management, rich built-in tools, MCP extensibility, and production-ready error handling
- Enables diverse use cases from finance agents to customer support to development automation

**This Research Includes:**
- Comprehensive documentation covering fundamentals, tools, and advanced patterns
- 4 working Python examples demonstrating key concepts
- Best practices for context management, performance, and production deployment
- Deep analysis of the agent loop, tool ecosystem, and extensibility mechanisms

## Table of Contents

1. [What is the Claude Agent SDK?](#what-is-the-claude-agent-sdk)
2. [Core Architecture](#core-architecture)
3. [The Agent Loop](#the-agent-loop)
4. [Tools Ecosystem](#tools-ecosystem)
5. [Context Management](#context-management)
6. [Model Context Protocol (MCP)](#model-context-protocol-mcp)
7. [Advanced Patterns](#advanced-patterns)
8. [Production Best Practices](#production-best-practices)
9. [Example Code](#example-code)
10. [Use Cases](#use-cases)
11. [Getting Started](#getting-started)
12. [Resources](#resources)

---

## What is the Claude Agent SDK?

### Overview

The Claude Agent SDK (formerly "Claude Code SDK") is a collection of tools and APIs that enable developers to build autonomous AI agents powered by Claude. Released alongside Claude Sonnet 4.5 in September 2025, it represents Anthropic's effort to democratize agentic AI development by sharing the building blocks behind Claude Code.

**Core Philosophy:**
> "Give your agents a computer" - Allow agents to work like humans do by providing tools for file operations, command execution, and web interaction.

### Key Capabilities

**1. Autonomous Task Execution**
Agents can break down complex tasks, gather information, take actions, and verify results without constant human guidance.

**2. Rich Tool Ecosystem**
- File operations (Read, Write, Edit, Glob, Grep)
- Command execution (Bash)
- Web interaction (WebFetch, WebSearch)
- Specialized tools (Jupyter notebooks, todo lists)
- Custom tools via MCP

**3. Context Management**
- Automatic context compaction
- Semantic search integration
- Subagent spawning
- Agentic file system navigation

**4. Production-Ready Features**
- Built-in error handling
- Permission systems
- Hook mechanisms
- Session management

### Installation

**Python:**
```bash
pip install claude-agent-sdk
npm install -g @anthropic-ai/claude-code
export ANTHROPIC_API_KEY='your-api-key-here'
```

**TypeScript:**
```bash
npm install @anthropic-ai/claude-agent-sdk
npm install -g @anthropic-ai/claude-code
export ANTHROPIC_API_KEY='your-api-key-here'
```

**Verification:**
```bash
claude-code --version
```

---

## Core Architecture

### System Design

```
┌──────────────────────────────────────────────────────────┐
│                 Your Application                         │
│  ┌─────────────────────────────────────────────────────┐ │
│  │         Claude Agent SDK Client                     │ │
│  │  ┌──────────────┐         ┌──────────────┐          │ │
│  │  │   Context    │◄────────┤    Tools     │          │ │
│  │  │  Management  │         │  (Built-in)  │          │ │
│  │  └──────────────┘         └──────────────┘          │ │
│  │         │                          │                │ │
│  │         │                          │                │ │
│  │         ▼                          ▼                │ │
│  │  ┌──────────────┐         ┌──────────────┐          │ │
│  │  │   Session    │◄────────┤   MCP        │          │ │
│  │  │  Manager     │         │   Servers    │          │ │
│  │  └──────────────┘         └──────────────┘          │ │
│  └────────────┬────────────────────────────────────────┘ │
│               │                                          │
└───────────────┼──────────────────────────────────────────┘
                │
                ▼
    ┌───────────────────────┐
    │    Claude Code CLI    │
    │  (Manages Claude AI)  │
    └───────────────────────┘
                │
                ▼
    ┌───────────────────────┐
    │  Claude Sonnet 4.5    │
    │   (AI Model)          │
    └───────────────────────┘
```

### Message Flow

**1. User Message → SDK Client**
Your application sends a message through the SDK

**2. SDK → Claude Code CLI**
The SDK communicates with the Claude Code CLI process

**3. CLI → Claude AI**
The CLI sends the message to the Claude AI model

**4. Claude AI → Tool Use**
Claude decides which tools to use and returns tool calls

**5. SDK → Tool Execution**
The SDK executes tools (file operations, commands, etc.)

**6. Tool Results → Claude AI**
Results are sent back to Claude for processing

**7. Iteration**
Steps 4-6 repeat until the task is complete

**8. Final Response → Application**
The SDK returns the final result to your application

---

## The Agent Loop

Effective agents operate through a structured cycle:

### Phase 1: Gather Context

**Goal:** Understand the environment and task

**Tools Used:** Read, Grep, Glob, WebFetch, WebSearch

**Process:**
1. Understand project structure (Glob, ls)
2. Read key files (README, config files)
3. Search for relevant code (Grep)
4. Fetch external documentation if needed
5. Organize findings logically

**Example:**
```python
# 1. Find all Python files
files = await agent.tool("Glob", pattern="**/*.py")

# 2. Search for specific patterns
matches = await agent.tool("Grep", pattern="class.*Model", type="py")

# 3. Read relevant files
for file in priority_files:
    content = await agent.tool("Read", file_path=file, limit=50)
```

### Phase 2: Take Action

**Goal:** Execute the task using appropriate tools

**Tools Used:** Write, Edit, Bash, custom tools

**Process:**
1. Create or modify files (Write, Edit)
2. Run commands (Bash)
3. Call custom tools (MCP)
4. Update progress (TodoWrite)
5. Handle errors gracefully

**Example:**
```python
# 1. Create new file
await agent.tool("Write", file_path="new_module.py", content=code)

# 2. Modify existing file
await agent.tool("Edit", file_path="main.py", old_string=old, new_string=new)

# 3. Run tests
result = await agent.tool("Bash", command="pytest", description="Run tests")

# 4. Track progress
await agent.tool("TodoWrite", todos=[...])
```

### Phase 3: Verify Work

**Goal:** Ensure actions achieved desired outcome

**Tools Used:** Bash (tests), Read (check output), custom validators

**Methods:**

**1. Rules-Based Feedback**
```python
# Run linter
await bash("eslint .", "Check code style")

# Run type checker
await bash("mypy src/", "Type check code")

# Run tests
await bash("pytest", "Run test suite")
```

**2. Visual Feedback**
```python
# For UI changes
screenshot = await capture_ui()
validate_design(screenshot)
```

**3. LLM-as-Judge**
```python
# Secondary LLM evaluates quality
evaluation = await secondary_llm(f"Evaluate this code: {code}")
```

### Iteration

The agent repeats the loop until:
- Task is successfully completed
- Maximum iterations reached
- Unrecoverable error occurs
- User cancels

---

## Tools Ecosystem

### File Operations

| Tool | Purpose | Key Parameters |
|------|---------|----------------|
| **Read** | Read file contents | file_path, offset, limit |
| **Write** | Create new files | file_path, content |
| **Edit** | Modify existing files | file_path, old_string, new_string, replace_all |
| **Glob** | Find files by pattern | pattern, path |
| **Grep** | Search file contents | pattern, path, glob, type, output_mode |

**Best Practices:**
- Use Read before Edit or Write on existing files
- Use Edit over Write for modifications
- Use offset/limit for large files
- Prefer Glob over bash `find`
- Prefer Grep over bash `grep`

### Command Execution

| Tool | Purpose | Key Parameters |
|------|---------|----------------|
| **Bash** | Execute shell commands | command, description, timeout, run_in_background |

**Best Practices:**
- Always provide clear descriptions
- Quote paths with spaces
- Chain dependent commands with `&&`
- Run independent commands in parallel
- Never use for file operations (use specialized tools)

### Web Interaction

| Tool | Purpose | Key Parameters |
|------|---------|----------------|
| **WebFetch** | Fetch web pages | url, prompt |
| **WebSearch** | Search the web | query, allowed_domains, blocked_domains |

**Best Practices:**
- Use specific prompts to extract only needed information
- Prefer MCP tools for web fetching if available
- Handle redirects by making new requests

### Specialized Tools

| Tool | Purpose | Use Case |
|------|---------|----------|
| **NotebookRead/Edit** | Jupyter notebooks | Data science workflows |
| **TodoRead/Write** | Task management | Track agent progress |

### Tool Configuration

```python
# Python - Only specific tools
options = ClaudeAgentOptions(
    custom_allowed_tools=["Read", "Write", "Bash"]
)

# Add to defaults
options = ClaudeAgentOptions(
    append_allowed_tools=["CustomTool"]
)

# Block specific tools
options = ClaudeAgentOptions(
    disallowed_tools=["Bash"]
)
```

---

## Context Management

### Strategy 1: Agentic Search

**How it works:** Agents actively navigate filesystems using tools

**Advantages:**
- High accuracy
- Full transparency
- Flexible navigation

**Disadvantages:**
- Slower than semantic search
- More tool calls

**Best for:** Code repositories, complex structures, when accuracy is critical

### Strategy 2: Semantic Search

**How it works:** Use vector embeddings for fast retrieval

**Advantages:**
- Very fast
- Scales to large datasets

**Disadvantages:**
- May miss relevant information
- Less transparent

**Best for:** Large documentation sets, when speed is critical

### Strategy 3: Subagents

**How it works:** Spawn isolated agent instances for subtasks

**Advantages:**
- Parallel processing
- Isolated contexts
- Configurable permissions

**Disadvantages:**
- Higher cost
- Need to aggregate results

**Best for:** Parallelizable tasks, large-scale analysis

**Example:**
```python
async def analyze_with_subagent(file: str):
    options = ClaudeAgentOptions(
        custom_allowed_tools=["Read", "Grep"]
    )
    async with ClaudeSDKClient(options=options) as subagent:
        return await subagent.send_user_message(f"Analyze {file}")

# Run in parallel
results = await asyncio.gather(*[
    analyze_with_subagent(f) for f in files
])
```

### Strategy 4: Automatic Compaction

**How it works:** SDK automatically summarizes older context

**Advantages:**
- Fully automatic
- Enables long-running tasks

**Disadvantages:**
- Some detail loss

**Best for:** Long-running agents, iterative tasks

### Hybrid Approach

Combine strategies for optimal results:
1. Quick semantic search for candidates
2. Agentic verification of relevance
3. Load full content of verified files
4. Break into subtasks for subagents
5. Rely on automatic compaction for main agent

---

## Model Context Protocol (MCP)

### What is MCP?

The Model Context Protocol is an open standard (introduced November 2024) for connecting LLMs to external systems. It standardizes how AI agents integrate with tools, databases, and APIs.

**Adoption:**
- Introduced by Anthropic (November 2024)
- Adopted by OpenAI (March 2025)
- Supported by Zed, Replit, Codeium, Sourcegraph
- Pre-built servers for: GitHub, Slack, Google Drive, Postgres, Puppeteer

### Creating Custom Tools

**In-Process (Recommended):**
```python
from claude_agent_sdk import tool, create_sdk_mcp_server

@tool(
    name="calculate",
    description="Perform calculation",
    input_schema={"a": float, "b": float, "operation": str}
)
async def calculate(args: dict):
    # Your logic here
    return {
        "content": [{
            "type": "text",
            "text": f"Result: {result}"
        }]
    }

server = create_sdk_mcp_server(
    name="math-tools",
    version="1.0.0",
    tools=[calculate]
)

options = ClaudeAgentOptions(custom_mcp_servers=[server])
```

**Advantages of In-Process:**
- ✓ No subprocess management
- ✓ Better performance
- ✓ Simpler deployment
- ✓ Type safety

### External MCP Servers

Configure in `.mcp.json`:
```json
{
    "mcpServers": {
        "github": {
            "command": "npx",
            "args": ["-y", "@modelcontextprotocol/server-github"],
            "env": {
                "GITHUB_TOKEN": "${GITHUB_TOKEN}"
            }
        },
        "database": {
            "url": "http://localhost:3000/mcp",
            "transport": "http"
        }
    }
}
```

**Transport Types:**
- **stdio** - External process via stdin/stdout
- **http** - HTTP endpoint
- **sse** - Server-Sent Events (deprecated)

---

## Advanced Patterns

### Parallel Tool Execution

```python
# Bad: Sequential
result1 = await read("file1.txt")
result2 = await read("file2.txt")

# Good: Parallel
results = await asyncio.gather(
    read("file1.txt"),
    read("file2.txt")
)
```

### Conditional Tool Use

```python
async def smart_read(file_path: str):
    # Check size first
    stat = await bash(f"wc -l {file_path}", "Count lines")
    lines = parse_count(stat)

    if lines > 1000:
        return await read(file_path, limit=100)
    else:
        return await read(file_path)
```

### Tool Chaining

```python
async def analyze_and_fix(file: str):
    content = await read(file)
    issues = analyze(content)

    for issue in issues:
        await edit(file, issue.old, issue.fix)

    return await bash("pytest", "Verify fixes")
```

### Error Recovery

```python
async def resilient_tool_use(tool: str, args: dict, retries: int = 3):
    for attempt in range(retries):
        try:
            return await use_tool(tool, args)
        except ProcessError as e:
            if attempt < retries - 1:
                await asyncio.sleep(2 ** attempt)
                continue
            raise
```

---

## Production Best Practices

### 1. Error Handling

```python
class ProductionAgent:
    async def execute_task(self, task: str):
        try:
            return await self.run_agent(task)
        except CLINotFoundError:
            logger.error("Claude Code not installed")
            return {"error": "setup_required"}
        except ProcessError as e:
            logger.error(f"Tool execution failed: {e}")
            return {"error": "execution_failed"}
        except Exception as e:
            logger.exception("Unexpected error")
            return {"error": "unknown"}
```

### 2. Logging and Monitoring

```python
logger = logging.getLogger("agent")

class MonitoredAgent:
    async def use_tool(self, tool: str, args: dict):
        logger.info(f"Tool: {tool}")
        start = time.time()

        try:
            result = await super().use_tool(tool, args)
            duration = time.time() - start
            logger.info(f"Tool {tool} completed in {duration:.2f}s")
            return result
        except Exception as e:
            logger.error(f"Tool {tool} failed: {e}")
            raise
```

### 3. Rate Limiting

```python
class RateLimitedAgent:
    def __init__(self, max_concurrent: int = 5):
        self.semaphore = Semaphore(max_concurrent)

    async def use_tool(self, tool: str, args: dict):
        async with self.semaphore:
            return await super().use_tool(tool, args)
```

### 4. Graceful Shutdown

```python
class GracefulAgent:
    async def shutdown(self):
        self.shutdown_event.set()
        if self.active_tasks:
            await asyncio.gather(*self.active_tasks, return_exceptions=True)
```

### 5. Performance Optimization

**Context Efficiency:**
```python
# Load smartly - find relevant files first
relevant = await grep("pattern", output_mode="files_with_matches")
for file in relevant[:5]:
    content = await read(file, limit=50)
```

**Caching:**
```python
@lru_cache(maxsize=100)
async def read_cached(file_path: str):
    return await read(file_path)
```

---

## Example Code

This research includes 4 comprehensive Python examples:

### 01_simple_query.py
Basic `query()` function usage for one-off tasks

**Demonstrates:**
- Simple question answering
- Code analysis
- Data processing

### 02_bidirectional_client.py
Interactive conversations with `ClaudeSDKClient`

**Demonstrates:**
- Multi-turn conversations
- Tool restrictions
- Working directory configuration
- Message inspection

### 03_custom_tools.py
Creating custom tools via in-process MCP servers

**Demonstrates:**
- Tool definition with `@tool` decorator
- Calculator tool
- Note-taking tools
- Combining built-in and custom tools

### 04_subagents.py
Parallel processing and context isolation

**Demonstrates:**
- Parallel file analysis
- Data processing with subagents
- Hierarchical agent structures
- Load balancing

**Run examples:**
```bash
cd examples
python 01_simple_query.py
python 02_bidirectional_client.py
python 03_custom_tools.py
python 04_subagents.py
```

---

## Use Cases

### 1. Finance Agents
**Capabilities:**
- Analyze portfolios
- Evaluate investments
- Generate reports
- Monitor market data

**Example:**
```python
prompt = """
Analyze the portfolio in portfolio.csv:
1. Calculate total value
2. Assess risk distribution
3. Suggest rebalancing
"""
```

### 2. Personal Assistants
**Capabilities:**
- Manage calendars
- Book travel
- Handle email
- Research topics

**Example:**
```python
prompt = """
Book a flight from NYC to SFO:
1. Search for flights next week
2. Find best prices
3. Create comparison report
"""
```

### 3. Customer Support Agents
**Capabilities:**
- Handle complex requests
- Search knowledge bases
- Create tickets
- Escalate issues

**Example:**
```python
prompt = """
Help user with issue:
1. Search documentation
2. Find solution
3. Provide step-by-step fix
"""
```

### 4. Development Agents
**Capabilities:**
- Code reviews
- Bug fixes
- Test generation
- Documentation

**Example:**
```python
prompt = """
Review pull request:
1. Analyze code changes
2. Check for issues
3. Run tests
4. Provide feedback
"""
```

### 5. Research Agents
**Capabilities:**
- Synthesize documents
- Web research
- Data analysis
- Report generation

**Example:**
```python
prompt = """
Research topic:
1. Search web and papers
2. Analyze findings
3. Create summary report
"""
```

---

## Getting Started

### Quick Start (5 minutes)

**1. Install:**
```bash
pip install claude-agent-sdk
npm install -g @anthropic-ai/claude-code
export ANTHROPIC_API_KEY='your-key'
```

**2. Create first agent:**
```python
import anyio
from claude_agent_sdk import query

async def main():
    async for message in query(prompt="List files in current directory"):
        print(message)

anyio.run(main)
```

**3. Run it:**
```bash
python first_agent.py
```

### Learning Path

**Week 1: Fundamentals**
- Read [01-fundamentals.md](01-fundamentals.md)
- Run [examples/01_simple_query.py](examples/01_simple_query.py)
- Experiment with basic queries

**Week 2: Tools and Capabilities**
- Read [02-tools-and-capabilities.md](02-tools-and-capabilities.md)
- Run [examples/02_bidirectional_client.py](examples/02_bidirectional_client.py)
- Try different tool combinations

**Week 3: Advanced Patterns**
- Read [03-advanced-patterns.md](03-advanced-patterns.md)
- Run [examples/03_custom_tools.py](examples/03_custom_tools.py)
- Create your own custom tools

**Week 4: Production**
- Run [examples/04_subagents.py](examples/04_subagents.py)
- Implement production best practices
- Build your first production agent

---

## Resources

### Official Documentation
- **Overview:** https://docs.claude.com/en/docs/agent-sdk/overview
- **Python SDK:** https://docs.claude.com/en/docs/agent-sdk/python
- **Engineering Blog:** https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk

### GitHub Repositories
- **Python SDK:** https://github.com/anthropics/claude-agent-sdk-python
- **TypeScript SDK:** https://github.com/anthropics/claude-agent-sdk-typescript
- **Demo Applications:** https://github.com/anthropics/claude-agent-sdk-demos

### Community Resources
- **DataCamp Tutorial:** Complete tutorial on Claude Agent SDK
- **Promptfoo Guide:** Integration guide for testing
- **Skywork.ai Tutorial:** Step-by-step Python & TypeScript guide

### Related Projects
- **Model Context Protocol:** https://github.com/modelcontextprotocol/servers
- **Claude Code:** https://docs.claude.com/en/docs/claude-code/

---

## Project Structure

```
claude-agent-sdk-deepdive/
├── README.md                      # This file
├── notes.md                       # Research notes
├── 01-fundamentals.md             # Core concepts and architecture
├── 02-tools-and-capabilities.md   # Complete tool reference
├── 03-advanced-patterns.md        # Advanced techniques
└── examples/
    ├── README.md                  # Examples overview
    ├── 01_simple_query.py         # Basic query examples
    ├── 02_bidirectional_client.py # Interactive conversations
    ├── 03_custom_tools.py         # Custom tool creation
    └── 04_subagents.py            # Parallel processing
```

---

## Key Takeaways

✅ **The Claude Agent SDK enables autonomous AI agents** that can plan, execute, and verify complex tasks

✅ **"Give agents a computer"** - Core philosophy of providing human-like tool access

✅ **The agent loop** (gather → act → verify) is fundamental to effective agents

✅ **Rich tool ecosystem** with file ops, commands, web access, and MCP extensibility

✅ **Context management is critical** - Multiple strategies (agentic, semantic, subagents, compaction)

✅ **Subagents enable scale** - Parallelize work and isolate contexts

✅ **MCP provides extensibility** - In-process tools are preferred for performance

✅ **Production-ready features** - Error handling, logging, rate limiting, graceful shutdown

✅ **Multi-language support** - Python and TypeScript with shared concepts

✅ **Active ecosystem** - Adopted by OpenAI, multiple integrations, growing community

---

## Conclusion

The Claude Agent SDK represents a significant advancement in making agentic AI accessible to developers. By providing the same building blocks used in Claude Code, Anthropic has enabled developers to create specialized agents for any domain.

**Key Innovations:**
1. **"Computer" paradigm** - Agents work like humans with general-purpose tools
2. **Automatic context management** - Handles complexity of long-running tasks
3. **MCP standard** - Extensible, standardized tool integration
4. **Production-ready** - Built-in features for real-world deployment

**Future Directions:**
- Growing ecosystem of MCP servers
- Improved context management techniques
- Enhanced verification mechanisms
- Broader language support

**Getting Started:**
The examples and documentation in this research provide everything needed to start building agents today. Whether you're creating a finance analyzer, personal assistant, or development tool, the Claude Agent SDK provides the foundation for powerful, autonomous AI agents.

---

*Research compiled: 2025-11-11*
*SDK Version: Python 1.x, TypeScript 1.x*
*Claude Model: Sonnet 4.5 (claude-sonnet-4-5-20250929)*

For questions or contributions, refer to the official documentation and GitHub repositories.
