# Claude Agent SDK: Advanced Patterns and Best Practices

## Context Management Strategies

Effective context management is crucial for building agents that can handle complex, long-running tasks without exceeding token limits or losing important information.

### Strategy 1: Agentic Search

**Concept:** Agents actively navigate filesystems and use tools to selectively load information.

**How it works:**
```python
# Agent uses Glob to find relevant files
relevant_files = await agent.tool("Glob", pattern="**/*config*.py")

# Then uses Grep to search within those files
matches = await agent.tool("Grep", pattern="DATABASE_URL", glob="**/*config*.py")

# Finally reads specific sections
for file in priority_files:
    content = await agent.tool("Read", file_path=file, offset=0, limit=50)
```

**Advantages:**
- High accuracy (agent sees actual content)
- Full transparency (clear what was read)
- Flexible navigation
- Works with any file structure

**Disadvantages:**
- Slower than semantic search
- Uses more tool calls
- Requires agent to be strategic

**Best for:**
- Code repositories
- Complex project structures
- When accuracy is critical

### Strategy 2: Semantic Search

**Concept:** Use vector embeddings to quickly find relevant information.

**How it works:**
```python
# Embed all documents
embeddings = create_embeddings(documents)

# When agent needs info, search by similarity
query_embedding = create_embedding(agent_query)
relevant_docs = vector_search(query_embedding, embeddings, top_k=10)

# Provide relevant docs in context
context = "\n\n".join(relevant_docs)
```

**Advantages:**
- Very fast retrieval
- Scales to large document sets
- Good for finding related content

**Disadvantages:**
- May miss relevant information
- Requires embedding infrastructure
- Less transparent to agent

**Best for:**
- Large documentation sets
- FAQ systems
- Knowledge bases
- When speed is critical

**Trade-off recommendation:**
> "Semantic search trades accuracy and transparency for speed—best added only when performance demands justify the tradeoff."

### Strategy 3: Subagents

**Concept:** Spawn isolated agent instances for specific subtasks.

**How it works:**
```python
# Python
from claude_agent_sdk import ClaudeSDKClient, ClaudeAgentOptions

async def analyze_with_subagent(file_path: str):
    # Create subagent with specific tools
    subagent_options = ClaudeAgentOptions(
        custom_allowed_tools=["Read", "Grep"],
        working_directory="/analysis"
    )

    async with ClaudeSDKClient(options=subagent_options) as subagent:
        result = await subagent.send_user_message(
            f"Analyze the file {file_path} for security issues"
        )
        return result

# Main agent coordinates multiple subagents
async def main_agent():
    files = ["auth.py", "api.py", "database.py"]

    # Run subagents in parallel
    results = await asyncio.gather(*[
        analyze_with_subagent(f) for f in files
    ])

    # Aggregate results
    summary = aggregate_findings(results)
    return summary
```

**Advantages:**
- Parallel processing
- Isolated contexts (no interference)
- Configurable permissions per subagent
- Prevents context overload

**Disadvantages:**
- Higher cost (multiple agent instances)
- Need to aggregate results
- More complex orchestration

**Best for:**
- Parallelizable tasks
- Large-scale analysis
- Tasks with different permission requirements
- When main agent's context is filling up

**Real-world example:**
```python
# Analyze a large codebase with subagents
async def analyze_codebase(repo_path: str):
    # Find all Python files
    files = glob(f"{repo_path}/**/*.py")

    # Create subagent for each module
    tasks = []
    for module_files in chunk(files, size=10):
        task = spawn_subagent(
            task=f"Analyze these files for code quality",
            files=module_files,
            tools=["Read", "Grep"]
        )
        tasks.append(task)

    # Wait for all subagents
    results = await asyncio.gather(*tasks)

    # Main agent synthesizes findings
    return synthesize_results(results)
```

### Strategy 4: Automatic Compaction

**Concept:** SDK automatically summarizes older context to make room for new information.

**How it works:**
- SDK monitors context size
- When approaching limits, identifies older information
- Summarizes and compresses older context
- Preserves important details
- Continues agent execution seamlessly

**Advantages:**
- Fully automatic
- Transparent to agent
- Enables long-running tasks
- No manual intervention needed

**Disadvantages:**
- Some detail loss in compressed sections
- Agent can't revisit original context
- May need to re-fetch information

**Best for:**
- Long-running agents
- Iterative tasks
- When context naturally grows
- Production agents (set and forget)

**Configuration:**
```python
# Python - compaction is automatic but can be configured
options = ClaudeAgentOptions(
    # Compaction happens automatically when needed
    # No manual configuration required
)
```

### Hybrid Approach

Combine strategies for optimal results:

```python
class SmartContextManager:
    def __init__(self):
        self.semantic_index = None
        self.compaction_enabled = True

    async def gather_context(self, query: str):
        # 1. Quick semantic search for candidates
        candidates = await self.semantic_search(query, top_k=20)

        # 2. Agentic verification - agent reads and confirms relevance
        verified = []
        for candidate in candidates:
            content = await self.read_file(candidate, limit=50)
            if self.agent_confirms_relevant(content, query):
                verified.append(candidate)

        # 3. Load full content of verified files
        context = []
        for file in verified[:5]:  # Top 5 most relevant
            content = await self.read_file(file)
            context.append(content)

        return context

    async def handle_large_task(self, task: str):
        # 4. Break into subtasks for subagents
        subtasks = self.decompose_task(task)

        # 5. Process with subagents in parallel
        results = await asyncio.gather(*[
            self.spawn_subagent(subtask) for subtask in subtasks
        ])

        # 6. Rely on automatic compaction for main agent
        return self.synthesize_results(results)
```

## The Agent Loop in Practice

### Phase 1: Gather Context

**Goal:** Understand the environment and task

**Tools:** Read, Grep, Glob, WebFetch, WebSearch

**Pattern:**
```python
async def gather_context(task: str):
    # 1. Understand project structure
    files = await glob("**/*")
    structure = analyze_structure(files)

    # 2. Read key files
    key_files = ["README.md", "package.json", "requirements.txt"]
    contents = await asyncio.gather(*[
        read(f) for f in key_files if f in files
    ])

    # 3. Search for relevant code
    relevant = await grep(pattern=extract_keywords(task))

    # 4. Fetch external context if needed
    if needs_docs(task):
        docs = await web_fetch(documentation_url(task))

    return consolidate_context(structure, contents, relevant, docs)
```

**Best Practices:**
- Start broad (project structure)
- Narrow down (specific files/sections)
- Search for patterns (keywords, functions)
- Supplement with external sources
- Organize findings logically

### Phase 2: Take Action

**Goal:** Execute the task using appropriate tools

**Tools:** Write, Edit, Bash, custom tools

**Pattern:**
```python
async def take_action(plan: Plan):
    for step in plan.steps:
        try:
            if step.type == "write_code":
                await write(step.file_path, step.content)

            elif step.type == "modify_code":
                await edit(
                    step.file_path,
                    step.old_string,
                    step.new_string
                )

            elif step.type == "run_command":
                result = await bash(step.command, step.description)
                if not result.success:
                    return handle_error(result)

            elif step.type == "custom":
                result = await call_custom_tool(step.tool, step.args)

            # Update progress
            await todo_write(update_step(step, "completed"))

        except Exception as e:
            # Handle errors gracefully
            await todo_write(update_step(step, "failed"))
            return plan_recovery(e, step)
```

**Best Practices:**
- Execute steps sequentially when dependent
- Run independent steps in parallel
- Update progress continuously
- Handle errors gracefully
- Validate each step before proceeding

### Phase 3: Verify Work

**Goal:** Ensure actions achieved desired outcome

**Tools:** Bash (tests), Read (check output), custom validators

**Pattern:**
```python
async def verify_work(action_results: ActionResults):
    verification_results = []

    # 1. Run tests
    test_result = await bash("npm test", "Run unit tests")
    verification_results.append({
        "type": "tests",
        "passed": test_result.exit_code == 0,
        "output": test_result.stdout
    })

    # 2. Check output files
    if action_results.created_files:
        for file in action_results.created_files:
            exists = await file_exists(file)
            verification_results.append({
                "type": "file_created",
                "file": file,
                "success": exists
            })

    # 3. Validate with rules
    if action_results.modified_code:
        lint_result = await bash("npm run lint", "Run linter")
        verification_results.append({
            "type": "linting",
            "passed": lint_result.exit_code == 0
        })

    # 4. Visual verification if UI changes
    if action_results.ui_changes:
        screenshot = await capture_screenshot()
        verification_results.append({
            "type": "visual",
            "screenshot": screenshot
        })

    # 5. LLM-as-judge for quality (optional)
    if needs_quality_check(action_results):
        quality_score = await llm_evaluate(action_results)
        verification_results.append({
            "type": "quality",
            "score": quality_score
        })

    # Decide if iteration needed
    if all(v["passed"] or v["success"] for v in verification_results):
        return VerificationResult.SUCCESS
    else:
        return VerificationResult.NEEDS_ITERATION
```

**Verification Methods:**

1. **Rules-based feedback**
   ```python
   # Linting
   await bash("eslint .", "Check code style")

   # Type checking
   await bash("mypy src/", "Run type checker")

   # Unit tests
   await bash("pytest", "Run test suite")
   ```

2. **Visual feedback**
   ```python
   # For UI changes
   screenshot = await capture_ui()
   if not meets_requirements(screenshot):
       return "Iterate: UI doesn't match design"
   ```

3. **LLM-as-judge**
   ```python
   # Secondary LLM evaluates quality
   quality_prompt = f"""
   Evaluate this code for:
   - Correctness
   - Readability
   - Best practices
   - Performance

   Code:
   {code}
   """
   evaluation = await secondary_llm(quality_prompt)
   ```

### Iteration Loop

```python
async def agent_loop(task: str, max_iterations: int = 5):
    for iteration in range(max_iterations):
        print(f"Iteration {iteration + 1}")

        # Phase 1: Gather
        context = await gather_context(task)

        # Phase 2: Act
        action_results = await take_action(create_plan(context, task))

        # Phase 3: Verify
        verification = await verify_work(action_results)

        if verification == VerificationResult.SUCCESS:
            return action_results

        # Learn from verification
        task = refine_task(task, verification.feedback)

    return AgentResult.MAX_ITERATIONS_REACHED
```

## Advanced Tool Patterns

### Parallel Tool Execution

```python
# Bad: Sequential
result1 = await read("file1.txt")
result2 = await read("file2.txt")
result3 = await read("file3.txt")

# Good: Parallel
results = await asyncio.gather(
    read("file1.txt"),
    read("file2.txt"),
    read("file3.txt")
)
```

### Conditional Tool Use

```python
async def smart_file_read(file_path: str):
    # Check file size first
    stat = await bash(f"wc -l {file_path}", "Count file lines")
    line_count = parse_line_count(stat.stdout)

    if line_count > 1000:
        # Large file: read in chunks
        return await read(file_path, offset=0, limit=100)
    else:
        # Small file: read all
        return await read(file_path)
```

### Tool Chaining

```python
async def analyze_and_fix(file_path: str):
    # Chain: Read → Analyze → Edit → Verify

    # 1. Read
    content = await read(file_path)

    # 2. Analyze
    issues = analyze_code(content)

    # 3. Edit
    for issue in issues:
        await edit(
            file_path,
            old_string=issue.problematic_code,
            new_string=issue.fix
        )

    # 4. Verify
    test_result = await bash("pytest", "Run tests")

    return test_result.exit_code == 0
```

### Error Recovery

```python
async def resilient_tool_use(tool: str, args: dict, retries: int = 3):
    for attempt in range(retries):
        try:
            return await use_tool(tool, args)
        except ProcessError as e:
            if attempt < retries - 1:
                # Wait and retry
                await asyncio.sleep(2 ** attempt)
                continue
            else:
                # Final attempt failed
                raise

        except CLIConnectionError:
            # CLI connection issues - try to reconnect
            await reconnect_cli()
            continue

        except Exception as e:
            # Unexpected error - don't retry
            raise
```

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
            return {"error": "execution_failed", "details": str(e)}

        except Exception as e:
            logger.exception("Unexpected error")
            return {"error": "unknown", "details": str(e)}
```

### 2. Logging and Monitoring

```python
import logging

logger = logging.getLogger("agent")

class MonitoredAgent:
    async def use_tool(self, tool: str, args: dict):
        logger.info(f"Tool: {tool}, Args: {args}")

        start = time.time()
        try:
            result = await super().use_tool(tool, args)
            duration = time.time() - start

            logger.info(f"Tool {tool} completed in {duration:.2f}s")
            self.metrics.record_tool_use(tool, duration, success=True)

            return result

        except Exception as e:
            duration = time.time() - start
            logger.error(f"Tool {tool} failed after {duration:.2f}s: {e}")
            self.metrics.record_tool_use(tool, duration, success=False)
            raise
```

### 3. Rate Limiting

```python
from asyncio import Semaphore

class RateLimitedAgent:
    def __init__(self, max_concurrent_tools: int = 5):
        self.semaphore = Semaphore(max_concurrent_tools)

    async def use_tool(self, tool: str, args: dict):
        async with self.semaphore:
            return await super().use_tool(tool, args)
```

### 4. Timeouts

```python
async def use_tool_with_timeout(tool: str, args: dict, timeout: int = 300):
    try:
        return await asyncio.wait_for(
            use_tool(tool, args),
            timeout=timeout
        )
    except asyncio.TimeoutError:
        logger.error(f"Tool {tool} timed out after {timeout}s")
        raise
```

### 5. Graceful Shutdown

```python
class GracefulAgent:
    def __init__(self):
        self.shutdown_event = asyncio.Event()
        self.active_tasks = set()

    async def execute_task(self, task: str):
        task_future = asyncio.create_task(self.run_agent(task))
        self.active_tasks.add(task_future)

        try:
            # Wait for either completion or shutdown
            done, pending = await asyncio.wait(
                [task_future, self.shutdown_event.wait()],
                return_when=asyncio.FIRST_COMPLETED
            )

            if self.shutdown_event.is_set():
                # Shutdown requested
                task_future.cancel()
                return {"status": "cancelled"}

            return task_future.result()

        finally:
            self.active_tasks.discard(task_future)

    async def shutdown(self):
        self.shutdown_event.set()

        # Wait for active tasks
        if self.active_tasks:
            await asyncio.gather(*self.active_tasks, return_exceptions=True)
```

## Performance Optimization

### 1. Context Efficiency

```python
# Bad: Load entire files
for file in all_files:
    content = await read(file)

# Good: Load smartly
# First, find relevant files
relevant = await grep(pattern="search_term", output_mode="files_with_matches")

# Then, read only relevant sections
for file in relevant[:5]:  # Top 5 most relevant
    content = await read(file, limit=50)  # First 50 lines
```

### 2. Parallel Execution

```python
# Bad: Sequential
issues = []
for file in files:
    issue = await analyze_file(file)
    issues.append(issue)

# Good: Parallel
issues = await asyncio.gather(*[
    analyze_file(file) for file in files
])
```

### 3. Caching

```python
from functools import lru_cache

class CachedAgent:
    @lru_cache(maxsize=100)
    async def read_file_cached(self, file_path: str):
        return await self.read(file_path)

    def invalidate_cache(self, file_path: str):
        self.read_file_cached.cache_clear()
```

### 4. Lazy Loading

```python
class LazyContextLoader:
    def __init__(self):
        self._file_contents = {}

    async def get_file(self, file_path: str):
        if file_path not in self._file_contents:
            self._file_contents[file_path] = await read(file_path)
        return self._file_contents[file_path]
```

## Key Takeaways

✓ **Context management is critical** - Choose strategies based on your use case

✓ **The agent loop** (gather → act → verify) is the foundation of reliable agents

✓ **Combine strategies** - Hybrid approaches often work best

✓ **Subagents enable scale** - Parallelize work and isolate contexts

✓ **Automatic compaction enables long-running tasks** - No manual intervention needed

✓ **Production agents need robust error handling** - Plan for failures

✓ **Performance optimization matters** - Parallel execution, caching, lazy loading

✓ **Monitoring and logging are essential** - Track agent behavior and performance

---

*Next: [04-practical-examples.md](04-practical-examples.md) - Real-world agent implementations*
