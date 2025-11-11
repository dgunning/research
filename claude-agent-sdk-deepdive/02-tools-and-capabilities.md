# Claude Agent SDK: Tools and Capabilities

## Overview

Tools are the primary mechanism through which Claude agents interact with their environment. The SDK provides a rich set of built-in tools covering file operations, command execution, web interaction, and more. Understanding these tools and how to use them effectively is essential for building powerful agents.

## Built-in Tools

### File Operation Tools

#### Read
Reads file contents from the filesystem.

**Purpose:**
- Load source code for analysis
- Read configuration files
- Access data files
- Review documentation

**Parameters:**
- `file_path` (string, required): Absolute path to the file
- `offset` (number, optional): Line number to start reading from
- `limit` (number, optional): Number of lines to read

**Best Practices:**
```python
# Good: Read specific sections of large files
Read(file_path="/path/to/large.log", offset=1000, limit=100)

# Avoid: Reading entire large files at once
Read(file_path="/path/to/10GB.log")  # Will consume too much context
```

**Example Usage:**
```python
# Python
result = await client.send_tool_result({
    "tool": "Read",
    "input": {"file_path": "/home/user/config.json"}
})
```

**Special Features:**
- Supports images (PNG, JPG, etc.) - returns visual content
- Supports PDFs - extracts text and visual content page by page
- Supports Jupyter notebooks (.ipynb) - returns all cells with outputs
- Returns formatted output with line numbers (cat -n format)
- Truncates lines longer than 2000 characters

#### Write
Creates new files or overwrites existing files.

**Purpose:**
- Generate new code files
- Create documentation
- Save analysis results
- Output data files

**Parameters:**
- `file_path` (string, required): Absolute path where file should be created
- `content` (string, required): Content to write to the file

**Best Practices:**
```python
# Good: Always use Read before Write for existing files
# This ensures the SDK knows you're aware of existing content

# Bad: Writing without reading first
Write(file_path="/existing/file.py", content="new content")  # Will error

# Good: Prefer Edit over Write for modifications
Edit(file_path="/existing/file.py", old_string="old", new_string="new")
```

**Safety Features:**
- Requires prior Read if file exists (prevents accidental overwrites)
- Always prefer Edit over Write for modifications
- Never create documentation files unless explicitly requested

#### Edit
Performs exact string replacements in existing files.

**Purpose:**
- Modify existing code
- Update configuration values
- Fix bugs
- Refactor implementations

**Parameters:**
- `file_path` (string, required): Path to file to modify
- `old_string` (string, required): Exact text to replace
- `new_string` (string, required): Replacement text
- `replace_all` (boolean, optional): Replace all occurrences (default: false)

**Best Practices:**
```python
# Good: Preserve exact indentation from Read output
# Line numbers in Read output are: spaces + line number + tab + content
# Only match the content part after the tab

# Good: Use replace_all for renaming variables
Edit(
    file_path="/home/user/app.py",
    old_string="oldVariableName",
    new_string="newVariableName",
    replace_all=True
)

# Good: Provide enough context for unique matches
Edit(
    file_path="/home/user/app.py",
    old_string="""def calculate(x, y):
    return x + y""",
    new_string="""def calculate(x, y):
    return x * y"""
)

# Bad: Too little context may match multiple locations
Edit(
    file_path="/home/user/app.py",
    old_string="return x",
    new_string="return y"
)  # May fail if not unique
```

**Important Notes:**
- Must use Read before Edit
- Fails if `old_string` is not unique (unless using `replace_all`)
- Must match indentation exactly as it appears after line number prefix
- Never include line number prefix in old_string or new_string

### Search Tools

#### Glob
Fast file pattern matching for finding files.

**Purpose:**
- Find files by name patterns
- Locate specific file types
- Navigate project structure

**Parameters:**
- `pattern` (string, required): Glob pattern (e.g., "**/*.py", "src/**/*.ts")
- `path` (string, optional): Directory to search in (defaults to working directory)

**Pattern Syntax:**
- `*` - Matches any characters within a filename
- `**` - Matches any directories recursively
- `?` - Matches a single character
- `[abc]` - Matches any character in the set
- `{a,b}` - Matches any of the alternatives

**Examples:**
```python
# Find all Python files
Glob(pattern="**/*.py")

# Find test files
Glob(pattern="**/*test*.py")

# Find specific directory contents
Glob(pattern="src/components/**/*.tsx")

# Multiple file types
Glob(pattern="**/*.{js,ts,jsx,tsx}")
```

**Best Practices:**
- Use for finding files by name patterns
- More efficient than listing directories recursively
- Results are sorted by modification time
- When doing open-ended searches that may require multiple rounds, use Task tool with Explore agent instead

#### Grep
Powerful content search tool built on ripgrep.

**Purpose:**
- Search for code patterns
- Find specific functions or classes
- Locate usage of variables or imports
- Discover configuration values

**Parameters:**
- `pattern` (string, required): Regular expression pattern
- `path` (string, optional): File or directory to search
- `glob` (string, optional): Filter files by glob pattern
- `type` (string, optional): Filter by file type (e.g., "py", "js", "rust")
- `output_mode` (string, optional): "content", "files_with_matches", "count"
- `-i` (boolean, optional): Case insensitive search
- `-A`, `-B`, `-C` (number, optional): Context lines after/before/both
- `-n` (boolean, optional): Show line numbers (default: true)
- `multiline` (boolean, optional): Enable multiline matching
- `head_limit` (number, optional): Limit output lines
- `offset` (number, optional): Skip first N results

**Pattern Syntax:**
- Uses ripgrep syntax (not grep)
- Literal braces need escaping: `interface\\{\\}` to find `interface{}`
- Multiline patterns require `multiline: true`

**Output Modes:**
```python
# Show matching lines with context (default)
Grep(pattern="def.*main", output_mode="content")

# Show only file paths
Grep(pattern="import React", output_mode="files_with_matches")

# Show match counts per file
Grep(pattern="TODO", output_mode="count")
```

**Examples:**
```python
# Find function definitions
Grep(pattern="def\\s+\\w+", type="py", output_mode="content")

# Find all TODO comments
Grep(pattern="TODO:", glob="**/*.py", output_mode="files_with_matches")

# Case-insensitive search with context
Grep(pattern="error", "-i": True, "-C": 3, output_mode="content")

# Search in specific files
Grep(pattern="api_key", glob="**/*.{json,yaml,env}")

# Multiline pattern matching
Grep(
    pattern="struct \\{[\\s\\S]*?field",
    multiline=True,
    type="go"
)
```

**Best Practices:**
- Always use Grep tool, never invoke `grep` or `rg` via Bash
- Use `type` parameter for known file types (more efficient than `glob`)
- Limit output with `head_limit` for large result sets
- Use Task tool with Explore agent for complex multi-round searches
- Enable `multiline` only when patterns need to span lines

### Command Execution Tools

#### Bash
Executes shell commands in a persistent session.

**Purpose:**
- Run build systems
- Execute tests
- Perform git operations
- Install dependencies
- Process data

**Parameters:**
- `command` (string, required): Shell command to execute
- `description` (string, required): Clear description of what command does (5-10 words)
- `timeout` (number, optional): Timeout in milliseconds (default: 120000, max: 600000)
- `run_in_background` (boolean, optional): Run command in background

**Best Practices:**
```python
# Good: Always provide clear descriptions
Bash(
    command="npm install",
    description="Install Node.js package dependencies"
)

# Good: Quote paths with spaces
Bash(
    command='cd "/Users/name/My Documents"',
    description="Change to documents directory"
)

# Good: Chain dependent commands with &&
Bash(
    command="git add . && git commit -m 'Update' && git push",
    description="Stage, commit and push changes"
)

# Good: Run multiple independent commands in parallel
# Use multiple Bash tool calls in a single turn

# Bad: Don't use bash for file operations
Bash(command="cat file.txt")  # Use Read tool instead
Bash(command="echo 'content' > file.txt")  # Use Write tool instead
```

**Special Features:**
- Persistent shell session (working directory maintained)
- Background execution with monitoring via BashOutput tool
- Automatic retry logic for network operations (git push/pull/fetch)
- Supports command chaining with `&&` (stop on failure) or `;` (continue regardless)

**Network Operation Retries:**
For `git push`, `git pull`, `git fetch`:
- Retry up to 4 times on network failures
- Exponential backoff: 2s, 4s, 8s, 16s
- Example:
  ```python
  # Automatically retries on network errors
  Bash(
      command="git push -u origin main",
      description="Push commits to remote repository"
  )
  ```

**Background Execution:**
```python
# Start long-running command in background
Bash(
    command="npm run dev",
    description="Start development server",
    run_in_background=True
)

# Later, check output
BashOutput(bash_id="bash_12345")
```

**Important Limitations:**
- Never use for file operations (use Read, Write, Edit instead)
- Never use for searching (use Grep, Glob instead)
- Never use for communication (output text directly to user)
- Avoid `find`, `grep`, `cat`, `echo`, `sed`, `awk` commands
- Don't use interactive commands (`-i` flag not supported)

### Web Interaction Tools

#### WebFetch
Fetches and processes web page content.

**Purpose:**
- Read documentation
- Fetch API responses
- Scrape web data
- Access online resources

**Parameters:**
- `url` (string, required): URL to fetch
- `prompt` (string, required): Instructions for processing the content

**Features:**
- Converts HTML to markdown automatically
- Processes content with AI for summarization
- Handles redirects
- Self-cleaning 15-minute cache

**Examples:**
```python
# Fetch documentation
WebFetch(
    url="https://docs.python.org/3/library/asyncio.html",
    prompt="Summarize the main concepts of asyncio"
)

# Extract specific information
WebFetch(
    url="https://api.github.com/repos/owner/repo",
    prompt="Extract the star count, fork count, and last update date"
)

# Scrape data
WebFetch(
    url="https://example.com/products",
    prompt="List all product names and prices"
)
```

**Best Practices:**
- Prefer MCP tools for web fetching if available
- Use specific prompts to extract only needed information
- Handle redirects by making new request with redirect URL
- URLs must be fully-formed and valid

#### WebSearch
Searches the web and returns results.

**Purpose:**
- Find current information
- Research topics
- Discover resources
- Verify facts

**Parameters:**
- `query` (string, required): Search query
- `allowed_domains` (array, optional): Only search these domains
- `blocked_domains` (array, optional): Exclude these domains

**Examples:**
```python
# General search
WebSearch(query="Claude Agent SDK best practices")

# Domain-specific search
WebSearch(
    query="async/await tutorial",
    allowed_domains=["docs.python.org", "realpython.com"]
)

# Exclude domains
WebSearch(
    query="machine learning",
    blocked_domains=["medium.com"]
)
```

**Notes:**
- Only available in the US
- Returns formatted search result blocks
- Account for current date when searching (don't use outdated years in queries)

### Specialized Tools

#### NotebookRead / NotebookEdit
Work with Jupyter notebooks (.ipynb files).

**NotebookRead:**
- Reads all cells with outputs
- Returns code, text, and visualizations
- Preserves cell structure

**NotebookEdit:**
- Replaces specific cell contents
- Supports insert and delete modes
- Works with cell IDs or indices

**Parameters:**
```python
# NotebookEdit parameters
{
    "notebook_path": "/path/to/notebook.ipynb",  # required
    "cell_id": "cell-123",  # optional, prefer over cell_number
    "cell_number": 0,  # optional, 0-indexed
    "new_source": "print('Hello')",  # required
    "cell_type": "code",  # required for insert, optional otherwise
    "edit_mode": "replace"  # replace, insert, or delete
}
```

**Examples:**
```python
# Read notebook
NotebookRead(notebook_path="/home/user/analysis.ipynb")

# Replace a cell
NotebookEdit(
    notebook_path="/home/user/analysis.ipynb",
    cell_id="cell-123",
    new_source="import pandas as pd\ndf = pd.read_csv('data.csv')"
)

# Insert new cell
NotebookEdit(
    notebook_path="/home/user/analysis.ipynb",
    cell_id="cell-123",
    new_source="# Data analysis section",
    cell_type="markdown",
    edit_mode="insert"
)
```

#### TodoRead / TodoWrite
Manage task lists and track progress.

**Purpose:**
- Track agent tasks
- Show progress to users
- Organize complex workflows
- Demonstrate thoroughness

**TodoWrite Parameters:**
```python
{
    "todos": [
        {
            "content": "Task description (imperative form)",
            "activeForm": "Present continuous form (e.g., 'Running tests')",
            "status": "pending" | "in_progress" | "completed"
        }
    ]
}
```

**Best Practices:**
```python
# Good: Update immediately after completing tasks
TodoWrite(todos=[
    {"content": "Run tests", "activeForm": "Running tests", "status": "completed"},
    {"content": "Fix errors", "activeForm": "Fixing errors", "status": "in_progress"}
])

# Good: Only one task in_progress at a time
# Good: Mark completed immediately, don't batch

# Bad: Multiple tasks in_progress
# Bad: Not updating after completion
```

**When to Use:**
- Complex multi-step tasks (3+ steps)
- Non-trivial tasks requiring planning
- User explicitly requests tracking
- Multiple related tasks
- After receiving new instructions

**When Not to Use:**
- Single straightforward tasks
- Trivial operations
- Purely conversational tasks

## Tool Configuration

### Specifying Allowed Tools

```python
# Python
from claude_agent_sdk import ClaudeAgentOptions

# Only specific tools
options = ClaudeAgentOptions(
    custom_allowed_tools=["Read", "Write", "Bash"]
)

# Add to default tools
options = ClaudeAgentOptions(
    append_allowed_tools=["CustomTool"]
)

# Block specific tools
options = ClaudeAgentOptions(
    disallowed_tools=["Bash"]
)
```

```typescript
// TypeScript
const options = {
    customAllowedTools: ["Read", "Write", "Bash"],
    // or
    appendAllowedTools: ["CustomTool"],
    // or
    disallowedTools: ["Bash"]
};
```

### Tool Permissions

The SDK provides fine-grained permission control:

```python
# Python - restrict file access
options = ClaudeAgentOptions(
    working_directory="/safe/directory",
    # Tools will be restricted to this directory
)
```

**Permission Strategies:**
1. **Allowlist** - Only permit specific tools
2. **Blocklist** - Allow all except specific tools
3. **Directory restrictions** - Limit file access scope
4. **Hook-based validation** - Custom permission logic

## Creating Custom Tools

### In-Process Tools (Recommended)

Custom tools can be created as Python functions or TypeScript methods:

**Python:**
```python
from claude_agent_sdk import tool, create_sdk_mcp_server

@tool(
    name="calculate_sum",
    description="Add two numbers",
    input_schema={"a": int, "b": int}
)
async def calculate_sum(args):
    result = args["a"] + args["b"]
    return {
        "content": [{
            "type": "text",
            "text": f"The sum is {result}"
        }]
    }

# Create MCP server with custom tools
server = create_sdk_mcp_server(
    name="math-tools",
    version="1.0.0",
    tools=[calculate_sum]
)

# Use in agent
options = ClaudeAgentOptions(
    custom_mcp_servers=[server]
)
```

**TypeScript:**
```typescript
import { tool, createSDKMCPServer } from '@anthropic-ai/claude-agent-sdk';

const calculateSum = tool({
    name: "calculate_sum",
    description: "Add two numbers",
    inputSchema: {
        type: "object",
        properties: {
            a: { type: "number" },
            b: { type: "number" }
        },
        required: ["a", "b"]
    },
    handler: async (args) => {
        const result = args.a + args.b;
        return {
            content: [{
                type: "text",
                text: `The sum is ${result}`
            }]
        };
    }
});

const server = createSDKMCPServer({
    name: "math-tools",
    version: "1.0.0",
    tools: [calculateSum]
});
```

**Advantages of In-Process Tools:**
- ✓ No subprocess management
- ✓ Better performance (no IPC overhead)
- ✓ Simpler deployment
- ✓ Easier debugging
- ✓ Type safety

### External MCP Servers

For complex integrations, use external MCP servers via `.mcp.json`:

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

## Tool Best Practices

### General Guidelines

1. **Use the right tool for the job**
   - File operations → Read, Write, Edit
   - Searching → Grep, Glob
   - Commands → Bash (only for actual shell operations)
   - Web → WebFetch, WebSearch

2. **Minimize context usage**
   - Use `offset` and `limit` for large files
   - Use Grep with `head_limit` for large result sets
   - Prefer Glob over listing directories

3. **Prefer specialized tools**
   - Use Edit over Write for modifications
   - Use Grep over Bash grep
   - Use Glob over Bash find

4. **Run tools in parallel when possible**
   - Multiple independent Read calls
   - Multiple Grep searches
   - Multiple WebFetch requests

5. **Provide clear descriptions**
   - Bash commands need 5-10 word descriptions
   - Help with debugging and logging

### Performance Optimization

```python
# Bad: Sequential file reads
for file in files:
    content = await read_file(file)

# Good: Parallel file reads
results = await asyncio.gather(*[read_file(f) for f in files])

# Bad: Reading entire large file
Read(file_path="large.log")

# Good: Reading specific section
Read(file_path="large.log", offset=1000, limit=100)

# Bad: Multiple grep searches sequentially
Grep(pattern="error")
Grep(pattern="warning")

# Good: Broader pattern with post-processing
Grep(pattern="error|warning")
```

### Error Handling

```python
# Python
try:
    result = await client.send_tool_use({
        "tool": "Read",
        "input": {"file_path": "/path/to/file"}
    })
except ProcessError as e:
    # Handle process failures
    logger.error(f"Tool execution failed: {e}")
except CLIConnectionError as e:
    # Handle connection issues
    logger.error(f"Cannot connect to Claude Code: {e}")
```

## Next Steps

Now that you understand the tool ecosystem:

1. **Learn about context management** - [03-context-management.md](03-context-management.md)
2. **Explore MCP integration** - [04-mcp-integration.md](04-mcp-integration.md)
3. **Study hooks and customization** - [05-hooks-and-customization.md](05-hooks-and-customization.md)
4. **Build practical agents** - [06-practical-examples.md](06-practical-examples.md)

## Key Takeaways

✓ **Built-in tools cover most common needs** - File ops, search, commands, web interaction

✓ **Use specialized tools over Bash** - Read instead of cat, Grep instead of grep

✓ **Tools can run in parallel** - Maximize efficiency with concurrent operations

✓ **Custom tools via MCP** - Extend functionality with in-process or external tools

✓ **Permission system provides safety** - Control what agents can access and do

✓ **Configuration is flexible** - Allow/block specific tools, restrict directories

✓ **In-process tools are preferred** - Better performance and simpler deployment

---

*Next: [03-context-management.md](03-context-management.md) - Strategies for managing agent context*
