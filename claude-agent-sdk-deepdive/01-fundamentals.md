# Claude Agent SDK: Fundamentals

## What is the Claude Agent SDK?

The Claude Agent SDK is a comprehensive framework released by Anthropic on September 29, 2025, designed to help developers build production-ready AI agents. Previously known as the "Claude Code SDK," it was renamed to better reflect its broader capabilities and purpose.

The SDK is built on the same agent harness that powers **Claude Code**, Anthropic's flagship agentic AI system for software development. By open-sourcing the core building blocks of Claude Code, Anthropic enables developers to create their own specialized AI agents for any domain.

### Core Philosophy: "Give Your Agents a Computer"

The fundamental design principle behind the Claude Agent SDK is elegantly simple yet powerful:

> **Give your agents a computer, allowing them to work like humans do.**

Instead of constraining AI agents to a rigid set of predefined actions, the SDK provides tools that mirror how humans work with computers:
- Execute bash commands
- Read and write files
- Search through code and documents
- Browse and fetch web content
- Run and test code

This approach enables general-purpose agents that can tackle open-ended problems rather than just executing scripted workflows.

## Why the Claude Agent SDK Matters

### The Evolution from Assistants to Agents

Traditional AI assistants follow a simple pattern:
1. User asks a question
2. AI provides an answer
3. Conversation ends or continues with more questions

AI agents, by contrast, operate autonomously:
1. User defines a goal or problem
2. Agent breaks down the problem
3. Agent gathers information
4. Agent takes actions using tools
5. Agent verifies its work
6. Agent iterates until the goal is achieved

The Claude Agent SDK provides the infrastructure for building agents that can:
- **Think** about complex problems
- **Plan** multi-step solutions
- **Act** using diverse tools
- **Learn** from feedback
- **Iterate** until successful

### Key Advantages

**1. Built on Production Experience**
The SDK isn't theoretical—it's battle-tested through Claude Code, which is used by thousands of developers for real software engineering tasks.

**2. Context Management at Scale**
The SDK handles the complexity of maintaining context across long-running tasks, automatically compacting information to prevent token exhaustion.

**3. Rich Tool Ecosystem**
Out-of-the-box support for file operations, command execution, web interaction, and extensibility through the Model Context Protocol (MCP).

**4. Production-Ready Features**
Built-in error handling, permission systems, session management, and hooks for custom control flow.

**5. Multi-Language Support**
First-class support for both Python and TypeScript/Node.js, with shared concepts that enable code reuse across languages.

## Key Concepts

### 1. The Agent Loop

Effective agents operate through a continuous cycle:

```
┌─────────────────────────────────────┐
│       1. GATHER CONTEXT             │
│  • Search for information           │
│  • Read relevant files              │
│  • Fetch external data              │
│  • Organize findings                │
└──────────┬──────────────────────────┘
           │
           ▼
┌─────────────────────────────────────┐
│       2. TAKE ACTION                │
│  • Execute commands                 │
│  • Write code                       │
│  • Call APIs                        │
│  • Create/modify files              │
└──────────┬──────────────────────────┘
           │
           ▼
┌─────────────────────────────────────┐
│       3. VERIFY WORK                │
│  • Check output                     │
│  • Run tests                        │
│  • Validate results                 │
│  • Iterate if needed                │
└──────────┬──────────────────────────┘
           │
           │ Success? ──No──► (loop back to step 1)
           │
           Yes
           │
           ▼
         Done!
```

### 2. Context Management

Context is how agents understand their environment and tasks. The SDK provides multiple strategies:

**Agentic Search**
Agents actively navigate directory structures, using tools like `grep` and `tail` to load relevant information. The filesystem becomes "a form of context engineering."

**Semantic Search**
Fast vector-based search for quick information retrieval. Trades some accuracy for speed.

**Subagents**
Isolated agent instances that handle specific subtasks, preventing context overload and enabling parallelization.

**Automatic Compaction**
When context grows too large, the SDK automatically summarizes older information to make room for new data.

### 3. Tools

Tools are the primary way agents interact with their environment. The SDK includes:

**File Operations**
- `Read` - Read file contents
- `Write` - Create new files
- `Edit` - Modify existing files
- `Glob` - Find files matching patterns
- `Grep` - Search file contents

**Command Execution**
- `Bash` - Run shell commands and scripts

**Web Interaction**
- `WebFetch` - Fetch and parse web pages
- `WebSearch` - Search the web

**Specialized Tools**
- `NotebookRead/Edit` - Work with Jupyter notebooks
- `TodoRead/Write` - Manage task lists

**Custom Tools via MCP**
The Model Context Protocol allows you to create custom tools that agents can use.

### 4. Hooks

Hooks provide fine-grained control over agent behavior:

**Pre-Tool Hooks**
Execute before a tool is called, allowing you to:
- Validate parameters
- Log actions
- Block dangerous operations
- Transform inputs

**Post-Tool Hooks**
Execute after a tool completes, enabling you to:
- Process results
- Trigger side effects
- Update application state
- Provide feedback to the agent

### 5. Permissions

The SDK includes a permission system to control what agents can do:
- Restrict file access to specific directories
- Limit command execution
- Control network access
- Require approval for sensitive operations

### 6. Subagents

Subagents are independent agent instances that can:
- Work on subtasks in parallel
- Maintain isolated context
- Use different tool configurations
- Report results back to the parent agent

## Architecture Overview

```
┌─────────────────────────────────────────────────────────┐
│                     Your Application                     │
│  ┌────────────────────────────────────────────────────┐ │
│  │         Claude Agent SDK Client                    │ │
│  │  ┌──────────────┐         ┌──────────────┐        │ │
│  │  │   Context    │◄────────┤    Tools     │        │ │
│  │  │  Management  │         │  (Built-in)  │        │ │
│  │  └──────────────┘         └──────────────┘        │ │
│  │         │                          │               │ │
│  │         │                          │               │ │
│  │         ▼                          ▼               │ │
│  │  ┌──────────────┐         ┌──────────────┐        │ │
│  │  │   Session    │◄────────┤   MCP        │        │ │
│  │  │  Manager     │         │   Servers    │        │ │
│  │  └──────────────┘         └──────────────┘        │ │
│  └────────────┬───────────────────────────────────────┘ │
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

The SDK acts as a bridge between your application and the Claude Code CLI, which in turn communicates with the Claude AI model. Your application controls the agent through the SDK's API, while the SDK handles the complexity of context management, tool execution, and conversation flow.

## Installation & Setup

### Python

**Requirements:**
- Python 3.10 or higher
- Node.js (for Claude Code CLI)

**Installation:**
```bash
# Install the SDK
pip install claude-agent-sdk

# Install Claude Code globally
npm install -g @anthropic-ai/claude-code
```

**Verify installation:**
```bash
# Check Claude Code version
claude-code --version
```

### TypeScript/Node.js

**Requirements:**
- Node.js 18 or higher

**Installation:**
```bash
# Install the SDK
npm install @anthropic-ai/claude-agent-sdk

# Install Claude Code globally
npm install -g @anthropic-ai/claude-code
```

### Environment Setup

**API Key:**
The Claude Agent SDK requires an Anthropic API key:

```bash
export ANTHROPIC_API_KEY='your-api-key-here'
```

Or create a `.env` file:
```
ANTHROPIC_API_KEY=your-api-key-here
```

**Working Directory:**
Agents operate within a working directory. By default, this is the current directory, but you can specify a different one:

```python
# Python
options = ClaudeAgentOptions(working_directory="/path/to/project")
```

```typescript
// TypeScript
const options = { workingDirectory: "/path/to/project" };
```

## Quick Start Examples

### Python: Simple Query

The simplest way to use the SDK is with the `query()` function:

```python
import anyio
from claude_agent_sdk import query

async def main():
    async for message in query(prompt="What files are in the current directory?"):
        print(message)

anyio.run(main)
```

### Python: Interactive Conversation

For more control, use `ClaudeSDKClient`:

```python
import anyio
from claude_agent_sdk import ClaudeSDKClient

async def main():
    async with ClaudeSDKClient() as client:
        # Send a message
        response = await client.send_user_message("List all Python files")

        # Process responses
        async for message in response:
            if message.type == "assistant":
                print(message.content)

anyio.run(main)
```

### TypeScript: Basic Usage

```typescript
import { ClaudeAgentSDK } from '@anthropic-ai/claude-agent-sdk';

async function main() {
    const sdk = new ClaudeAgentSDK();

    const response = await sdk.query({
        prompt: "What files are in the current directory?"
    });

    for await (const message of response) {
        console.log(message);
    }
}

main();
```

## Understanding Messages

The SDK uses a message-based communication model:

### Message Types

**User Messages**
Messages from you (or your application) to the agent:
```python
{
    "type": "user",
    "content": [{"type": "text", "text": "Analyze this repository"}]
}
```

**Assistant Messages**
Messages from the agent to you:
```python
{
    "type": "assistant",
    "content": [
        {"type": "text", "text": "I'll analyze the repository..."},
        {"type": "tool_use", "tool": "Bash", "input": {"command": "git log"}}
    ]
}
```

**System Messages**
Configuration and instructions for the agent:
```python
{
    "type": "system",
    "content": "You are a helpful code review assistant."
}
```

**Result Messages**
Results from tool executions:
```python
{
    "type": "result",
    "tool_use_id": "tool_12345",
    "content": [{"type": "text", "text": "Command output here"}]
}
```

## Next Steps

Now that you understand the fundamentals, you can:

1. **Learn about tools** - Explore the built-in tools and how to create custom ones
2. **Study context management** - Understand strategies for managing information
3. **Implement hooks** - Add custom logic to control agent behavior
4. **Build with MCP** - Integrate external services using the Model Context Protocol
5. **Deploy to production** - Learn best practices for production agents

## Key Takeaways

✓ **The Claude Agent SDK enables building autonomous AI agents** that can plan, execute, and verify complex tasks

✓ **"Give agents a computer"** - Agents work like humans using tools for file operations, commands, and web access

✓ **The agent loop** (gather context → take action → verify) is the foundation of effective agent behavior

✓ **Context management is crucial** - The SDK provides multiple strategies to handle information at scale

✓ **Tools are extensible** - Built-in tools cover common needs, MCP enables custom integrations

✓ **Production-ready features** - Hooks, permissions, error handling, and session management included

✓ **Multi-language support** - Python and TypeScript/Node.js with shared concepts

---

*Next: [02-tools-and-capabilities.md](02-tools-and-capabilities.md) - Deep dive into the tool ecosystem*
