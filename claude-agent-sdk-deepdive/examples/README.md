# Claude Agent SDK Examples

This directory contains practical examples demonstrating various features and patterns of the Claude Agent SDK.

## Prerequisites

1. **Install Claude Agent SDK:**
   ```bash
   pip install claude-agent-sdk
   ```

2. **Install Claude Code:**
   ```bash
   npm install -g @anthropic-ai/claude-code
   ```

3. **Set API Key:**
   ```bash
   export ANTHROPIC_API_KEY='your-api-key-here'
   ```

4. **Verify Installation:**
   ```bash
   claude-code --version
   ```

## Examples

### 01_simple_query.py
**Demonstrates:** Basic `query()` function for one-off tasks

**Key concepts:**
- Simple question answering
- Code analysis requests
- Data processing tasks

**Run:**
```bash
python 01_simple_query.py
```

---

### 02_bidirectional_client.py
**Demonstrates:** Interactive conversations with `ClaudeSDKClient`

**Key concepts:**
- Multi-turn conversations
- Tool restrictions
- Working directory configuration
- Message inspection

**Run:**
```bash
python 02_bidirectional_client.py
```

---

### 03_custom_tools.py
**Demonstrates:** Creating and using custom tools via MCP

**Key concepts:**
- In-process tool definition with `@tool` decorator
- Custom MCP servers
- Combining built-in and custom tools
- Practical tool examples (calculator, note-taking)

**Run:**
```bash
python 03_custom_tools.py
```

---

### 04_subagents.py
**Demonstrates:** Parallel processing and context isolation with subagents

**Key concepts:**
- Parallel file analysis
- Data processing with subagents
- Hierarchical agent structures
- Load balancing across subagents

**Run:**
```bash
python 04_subagents.py
```

## Running All Examples

```bash
# Run each example
for example in examples/*.py; do
    echo "Running $example..."
    python "$example"
    echo "---"
done
```

## Example Output Structure

Each example follows this pattern:

```
=== Example Name ===

User: [user message]
Assistant: [agent response]

---
```

## Common Patterns

### Basic Query Pattern
```python
import anyio
from claude_agent_sdk import query

async def main():
    async for message in query(prompt="Your task here"):
        print(message)

anyio.run(main)
```

### Interactive Client Pattern
```python
import anyio
from claude_agent_sdk import ClaudeSDKClient

async def main():
    async with ClaudeSDKClient() as client:
        response = await client.send_user_message("Your message")
        async for message in response:
            if message.type == "assistant":
                print(message.content)

anyio.run(main)
```

### Custom Tool Pattern
```python
from claude_agent_sdk import tool, create_sdk_mcp_server, ClaudeAgentOptions

@tool(name="tool_name", description="Tool description", input_schema={"param": type})
async def my_tool(args: dict):
    # Your logic here
    return {
        "content": [{"type": "text", "text": "Result"}]
    }

server = create_sdk_mcp_server(name="my-server", version="1.0.0", tools=[my_tool])
options = ClaudeAgentOptions(custom_mcp_servers=[server])
```

### Subagent Pattern
```python
import asyncio

async def task_with_subagent(task: str):
    options = ClaudeAgentOptions(
        custom_allowed_tools=["Read", "Grep"],
        system_prompt="Specific instructions"
    )

    async with ClaudeSDKClient(options=options) as subagent:
        response = await subagent.send_user_message(task)
        # Process response
        return result

# Run subagents in parallel
results = await asyncio.gather(*[
    task_with_subagent(task) for task in tasks
])
```

## Troubleshooting

### "Claude Code not installed"
```bash
npm install -g @anthropic-ai/claude-code
```

### "CLIConnectionError"
Ensure Claude Code is properly installed and the API key is set:
```bash
export ANTHROPIC_API_KEY='your-key'
```

### "ProcessError"
Check that the working directory exists and is accessible:
```python
options = ClaudeAgentOptions(working_directory="/existing/path")
```

### Import Errors
Ensure the SDK is installed:
```bash
pip install claude-agent-sdk
```

## Next Steps

After running these examples:

1. **Modify the examples** - Experiment with different prompts and configurations
2. **Combine patterns** - Mix and match techniques for your use case
3. **Add custom tools** - Create tools specific to your domain
4. **Build production agents** - Apply these patterns to real applications

## Additional Resources

- **Official Documentation:** https://docs.claude.com/en/docs/agent-sdk/overview
- **GitHub Repository:** https://github.com/anthropics/claude-agent-sdk-python
- **Demo Applications:** https://github.com/anthropics/claude-agent-sdk-demos

## License

These examples are provided for educational purposes. The Claude Agent SDK is provided by Anthropic under its own license terms.
