# Claude Code Mastery Research Notes

## Original Prompt

> I want to be the best in Toronto at using Claude Code both cli and web. Look at how people are using Claude Code e.g. https://blog.sshh.io/p/how-i-use-every-claude-code-feature, the ways to use both cli and web effectively, how to setup .claude settings, agents and commands so it works on the web. At the end of the research I must be in the 99th percentile Claude code developers

## Research Goals

1. Understand how power users are leveraging Claude Code
2. Master both CLI and Web versions effectively
3. Learn .claude settings configuration (CLAUDE.md, AGENTS.md, etc.)
4. Understand agents and slash commands setup
5. Make configuration work seamlessly across CLI and Web
6. Identify advanced workflows and patterns
7. Become top 1% Claude Code developer in Toronto

## Research Log

### Session Start: 2025-11-07

#### Research Strategy
1. Analyze the referenced blog post on Claude Code usage
2. Study Claude Code documentation
3. Research .claude directory configuration patterns
4. Explore MCP integration capabilities
5. Identify power user workflows
6. Document CLI vs Web differences
7. Create comprehensive mastery guide

---

## Key Findings from Research

### Power User Blog Analysis (blog.sshh.io)

**CLAUDE.md Philosophy:**
- 13KB "constitution" file - documents only tools used by 30%+ of engineers
- Token budgets allocated per tool like "ad space"
- Start with guardrails, not comprehensive manuals
- Avoid @-mentioning extensive docs (creates bloat)
- Never use negative-only constraints - always provide alternatives
- Use simplified docs as forcing function to improve tooling

**Context Management Workflows:**
1. `/clear` + `/catchup` - Default restart; custom command reads all changed files in git branch
2. "Document & Clear" - For complex tasks; dump progress to markdown, clear state, resume
3. Avoid `/compact` - "Opaque, error-prone, not well-optimized"
- Run `/context` mid-session to understand actual usage
- Baseline costs: ~20k tokens (10%) in monorepo

**Custom Commands Philosophy:**
- Minimal setup: `/catchup` (reads changed git files), `/pr` (clean, stage, prepare PR)
- "If you have long list of complex custom commands, you've created anti-pattern"

**Delegation Strategy:**
- AGAINST custom subagents - they "gatekeep context" and force rigid workflows
- Instead: leverage built-in `Task(...)` to spawn clones with dynamic orchestration
- "Master-Clone" architecture

**Hooks Strategy:**
- Use block-at-submit hooks (primary), not block-at-write
- `PreToolUse` hook wraps `Bash(git commit)` commands
- Checks for `/tmp/agent-pre-commit-pass` file (created only if tests pass)
- Forces test-and-fix loops until builds are green
- "Blocking agent mid-plan confuses or even frustrates it"

**Advanced Techniques:**
- Planning Mode: Built-in for large features
- Claude Code SDK: Massive parallel scripting via `claude -p` commands
- GitHub Actions: Operationalization layer with CloudWatch/Slack/Jira triggers
- Historical Analysis: Scripts analyze `~/.claude/projects/` logs for patterns

**Skills vs MCP:**
- Skills = "formal productization" of scripting layer
- Give agents raw environment access (binaries, scripts, docs)
- MCPs = "simple, secure gateways" with few high-level tools
- Only maintains Playwright MCP for stateful environments
- Migrated stateless tools (Jira, AWS, GitHub) to simple CLIs

### CLI Features & Configuration

**Key Commands:**
- `/clear` - Use often; every time you start something new
- `/init` - Key to unlocking full potential
- `/help` - Shows all available commands
- `/install-github-app` - Automated PR reviews
- `/context` - Check token usage mid-session
- `/rewind` or `Esc+Esc` - Restore checkpoints
- `/compact` - Manual compaction with explicit keep instructions

**Headless Mode:**
- `-p` flag with prompt enables non-interactive mode
- `--output-format stream-json` for streaming JSON output
- Use in CI, pre-commit hooks, build scripts, automation

**Skip Permissions Mode:**
- `claude --dangerously-skip-permissions` (like old "yolo mode")
- Power users use this to avoid friction

**Advanced SDK Usage:**
1. Massive parallel scripting via bash scripts calling `claude -p`
2. Building internal chat tools
3. Rapid agent prototyping

### Web Features (October 2025 Release)

**Key Differences from CLI:**
- Cloud-hosted, browser/mobile accessible
- Connects to GitHub repos, runs in isolated containers
- Creates PRs automatically
- Parallel task execution across multiple repos
- "Teleport" feature: copy chat transcript + files to local CLI

**Advantages:**
- Convenience of hosted container managed by Anthropic
- Pleasant web and mobile UI
- No local setup required
- Parallel workflows across different repos

**Architecture:**
- Every task runs in isolated sandbox environment
- Network and filesystem restrictions
- Git interactions through secure proxy service
- Can only access authorized repositories

**PRs Indistinguishable from CLI:**
- Web version PRs identical to CLI PRs
- Seamless transition between web and CLI

### .claude Directory Configuration

**File Hierarchy:**
```
~/.claude/                    # Global user settings
├── settings.json             # User-wide configuration
└── projects/                 # Session logs

project/.claude/              # Project-specific (checked in)
├── settings.json             # Team-shared configuration
├── settings.local.json       # Personal (not checked in)
├── commands/                 # Custom slash commands
│   └── catchup.md
├── agents/                   # Subagent definitions
│   └── architect.md
└── .mcp.json                 # MCP server configuration

project/CLAUDE.md             # Project constitution (most important)
project/AGENTS.md             # Alternative convention
```

**CLAUDE.md Best Practices:**
- Acts as persistent briefing document for every interaction
- Include: Tech stack, repository etiquette, code style, workflows
- Can be hierarchical (project-level + nested directories)
- Most specific/nested takes priority
- Global CLAUDE.md in ~/.claude/ applies to all projects
- Treat as living doc - update frequently
- Contents adhered to MORE strictly than user prompt

**settings.json Advanced Options:**

Sandbox Configuration:
```json
{
  "sandbox": {
    "enabled": true,
    "autoAllowBashIfSandboxed": true,
    "excludedCommands": ["docker", "kubectl"],
    "network": {
      "allowUnixSockets": true,
      "allowLocalBinding": false
    }
  }
}
```

Permissions:
```json
{
  "permissions": {
    "bash": {
      "allow": ["npm", "git"],
      "deny": ["rm -rf /"]
    },
    "read": {
      "deny": [".env", "**/*secret*"]
    }
  }
}
```

Other Options:
- `HTTPS_PROXY`/`HTTP_PROXY` for debugging prompts
- `MCP_TOOL_TIMEOUT`/`BASH_MAX_TIMEOUT_MS` for longer operations
- `apiKeyHelper` for enterprise API keys
- Environment variables configuration
- Custom announcements
- Model selection

### Custom Slash Commands

**Setup:**
- Create markdown files in `.claude/commands/`
- Become available via `/` menu
- Check into git for team sharing
- Use `$ARGUMENTS` keyword for parameters

**Philosophy:**
- Keep minimal - long list = anti-pattern
- Focus on highest-value, repeated workflows
- Examples: `/catchup`, `/pr`

**Best Practices:**
- Document purpose in command file
- Include usage examples
- Keep prompts concise and clear

### MCP (Model Context Protocol) Integration

**Configuration Methods:**
1. CLI Wizard: `claude mcp add --transport http <name> <url>`
2. Direct config file editing (recommended for complex setups)

**Config File Location:**
- Preferred: `~/.claude.json`
- Project-level: `.mcp.json` (checked in, team-wide)

**Transport Types:**
- **stdio**: Local development (via uvx/npx)
- **HTTP**: Remote servers, cloud-based services

**Context Window Impact:**
- Each enabled MCP server adds tool definitions to system prompt
- Toggle servers on/off during session via @mention
- Use `/mcp` command to manage interactively

**Best Practices:**
- Never hardcode secrets
- Always validate inputs
- Implement rate limiting
- Grant minimal directory access
- Use `--mcp-debug` flag for troubleshooting

**Skills vs MCP Philosophy (Updated):**
- Skills: Raw environment access (binaries, scripts, docs)
- MCP: Simple, secure gateways with few high-level tools
- Use Playwright MCP for stateful environments
- Migrate stateless tools to simple CLIs

### Subagents & Autonomous Operation

**Definition:**
- Specialized mini-agents with own system prompt
- Independent context window
- Specific tool permissions
- Defined in `.claude/agents/` directory

**When to Use:**
- Large goals that can be parallelized
- Scoped tasks with clear interfaces
- Preventing context pollution in long conversations
- Early investigation without consuming main context

**Best Practices:**
- Scope tools per agent (PM/Architect: read-heavy; Implementer: edit/write/bash)
- If omit tools = grants access to all (be intentional)
- Use for verification and investigation early in conversation
- Each operates in own context (prevents pollution)

**Architecture Patterns:**
- Email agent spawns multiple search subagents in parallel
- Each runs different queries, returns relevant excerpts
- Main agent coordinates results

**Markdown Format:**
```yaml
---
name: architect
description: Reviews code architecture and suggests improvements
tools: [Read, Glob, Grep]
---

You are an experienced software architect...
```

### Checkpointing & Version Control

**Core Feature:**
- Automatically saves code state before each change
- Instant rollback with `Esc+Esc` or `/rewind`
- Choose to restore: code, conversation, or both
- Persists across sessions

**Limitations:**
- Only tracks direct file edits through Claude's tools
- Bash commands (rm, mv, cp) cannot be undone
- Not a Git replacement

**When to Use:**
- Before exploratory or high-impact edits
- Fearless experimentation during active sessions
- Quick rollback without git overhead

**Relationship with Git:**
- Checkpoints: Quick rollback during agent sessions
- Git: Permanent version control
- Use both together - "rollback without ritual"

### VS Code Extension (September 2025)

**Key Features:**
- Native extension in beta
- Real-time code change display in sidebar panel
- Inline diff view
- Extended thinking toggle
- File management with @-mentions
- MCP server usage within IDE
- Conversation history
- Multiple simultaneous sessions

**Keyboard Shortcuts:**
- Most CLI shortcuts work in extension
- Access CLI slash commands directly

**Compatibility:**
- VS Code 1.98.0 or higher
- Also works with Cursor, Windsurf, VSCodium

**Default Model:**
- Claude Sonnet 4.5

### GitHub Integration & Automation

**Setup:**
- Quick: Installer + API key (minutes)
- Enterprise: Own cloud infrastructure

**Triggering Workflows:**
1. Comment-triggered: Reviewers @claude in PR
2. Auto-review: Runs on PR open/synchronize

**Configuration:**
```yaml
# On-demand via comments
issue_comment:
  types: [created]
  # Filter for @claude

# Automated on PR events
pull_request:
  types: [opened, synchronize]
```

**Security Practices:**
- Start with least privilege: `contents: read`, `pull-requests: write`
- Store `ANTHROPIC_API_KEY` as secret
- Rotate keys periodically
- Maintain branch protection and CODEOWNERS
- Require human approval for merges

**CLAUDE.md for PR Reviews:**
- Define code style guidelines
- Review criteria
- Project-specific rules
- Preferred patterns

**Best Practices:**
- Scope by file globs
- Keep prompts precise
- Be specific and clear in requests
- Iterate with feedback in follow-up comments
- AI reviews don't replace human reviews
- Think of AI as "extremely fast junior developer"

**Capabilities:**
- Subjective reviews beyond linting
- Identifies: typos, stale comments, misleading names
- Security vulnerabilities and logic errors
- Instant feedback aligned with guidelines

### Context Management Strategies

**Token Budget Awareness:**
- Run `/context` mid-session to check usage
- Baseline: ~20k tokens (10%) in monorepos
- Context gathering consumes time and tokens

**Three Restart Strategies:**
1. **`/clear` + `/catchup`**: Default restart
2. **Document & Clear**: Complex tasks - dump to markdown, clear, resume
3. **Avoid `/compact`**: Opaque, error-prone, not well-optimized

**Just-in-Time Context:**
- Maintain lightweight identifiers (file paths, queries, links)
- Dynamically load data at runtime using tools
- Don't load everything upfront

**Manual Compaction:**
- Use `/compact keep <instructions>`
- Proactive compaction as you pivot features
- Think "version control for chat states"

**Hard Resets:**
- Starting new feature? Use `/clear`
- Wipes cruft, signals focus shift
- Context drift is real - hard resets preserve quality

### Prompt Engineering Patterns

**For Claude 4.x Models:**
- Clear, explicit instructions
- Be specific about desired output
- Provide context/motivation behind instructions
- Explain why behavior is important

**Multi-Context Window Workflows:**
- Claude 4.5 excels at long-horizon reasoning
- Make steady advances on few things at a time
- Save state, continue with fresh context window
- Exceptional state tracking capabilities

**Practical Tips:**
- Tab-completion for file/folder references
- Paste URLs alongside prompts
- Use `/permissions` to allowlist domains
- Modularize large objectives with subagents
- Delegate API research, security review, planning to specialists
- Main session stays lean and focused

**Research and Planning:**
- Ask Claude to read relevant files/images/URLs first
- Give general pointers or specific filenames
- Explicitly tell it NOT to write code yet
- Research and plan first = significantly better performance
- Without planning, Claude jumps straight to coding

### Advanced Configuration Tips

**Environment Tuning:**
- settings.json: Company announcements
- Custom AWS credential scripts
- Proxy configuration for network debugging
- Timeout adjustments for long operations

**Permission Audits:**
- Regular self-audits of permitted commands
- Review bash command allowlist
- Check file read/write permissions
- Monitor MCP server access

**Hooks Strategy:**
- PreToolUse: Wrap Bash(git commit)
- Check test pass files before allowing commits
- Force test-and-fix loops
- Hint hooks provide non-blocking feedback

**Historical Analysis:**
- Analyze `~/.claude/projects/` session logs
- Identify common exceptions
- Track permission request patterns
- Find error patterns
- Improve CLAUDE.md and CLIs based on data

### CLI vs Web Decision Matrix

**Use CLI When:**
- Local development with existing setup
- Need full control over environment
- Working with local files and tools
- Integrating with local git workflow
- Using custom hooks and scripts
- Maximum customization required

**Use Web When:**
- No local setup available
- Working from mobile/tablet
- Need parallel tasks across multiple repos
- Quick prototyping without environment setup
- Collaborating with team on cloud-hosted tasks
- Want Anthropic-managed containers

**Hybrid Workflow:**
- Start on Web for exploration
- "Teleport" to CLI for detailed work
- PRs are identical from both
- Settings sync via .claude directory

### Power User Patterns

**Master-Clone Architecture:**
- Main agent stays in control
- Spawns clones via Task(...) for subtasks
- Clones manage own orchestration dynamically
- No rigid human-defined workflows

**Planning Mode Usage:**
- Built-in planning for large features
- Custom planning tools for production
- Align with internal design formats
- Enforce security/privacy best practices

**GitHub Actions as Operationalization:**
- CloudWatch alerts trigger PR generation
- Slack/Jira integration for workflows
- Logs enable data-driven flywheel
- Bugs → improved CLAUDE.md/CLIs → better agents

**Parallel Scripting:**
- Bash scripts calling `claude -p` in parallel
- Massive parallel automation
- Building internal chat tools
- Rapid agent prototyping

### Anti-Patterns to Avoid

❌ **Don't:**
- Create long lists of complex custom commands
- Use custom subagents that gatekeep context
- Block agent mid-plan (confuses/frustrates it)
- @-mention extensive docs (creates bloat)
- Use negative-only constraints
- Rely on automatic /compact
- Hardcode secrets in config
- Grant overly broad permissions
- Ignore context window usage
- Wait for context to overflow

✅ **Do:**
- Keep commands minimal and high-value
- Use built-in Task(...) for delegation
- Use block-at-submit hooks instead
- Pitch WHY to read docs, don't dump them
- Always provide alternatives
- Manual /compact with explicit keep instructions
- Use environment variables and secrets management
- Apply principle of least privilege
- Monitor with /context mid-session
- Proactively /clear and restart

### Settings Synchronization (CLI ↔ Web)

**What Syncs:**
- CLAUDE.md (if in project root)
- .claude/commands/ (custom slash commands)
- .claude/agents/ (subagent definitions)
- .mcp.json (MCP server configuration) - **BUT with critical limitation**
- settings.json (if in project .claude/)

**What Doesn't Sync:**
- Local settings (~/.claude/settings.json)
- User-specific configurations
- settings.local.json
- Global CLAUDE.md

**Making It Work:**
- Check .claude/ directory into git
- Include CLAUDE.md in repository
- Use project-level configs, not global
- Document setup in README
- Team gets consistent experience

### MCP Configuration: CLI vs Web (Critical Differences)

**Architecture Constraint:**
- CLI: Runs on your machine, can spawn local processes
- Web: Runs in Anthropic's cloud sandbox, NO local process access

**MCP Transport Support:**

| Transport | CLI | Web | Use Case |
|-----------|-----|-----|----------|
| **stdio** (local processes) | ✅ | ❌ | Filesystem, Playwright, local DB |
| **HTTP** (remote servers) | ✅ | ✅ | Company APIs, cloud services |

**Project Config (.mcp.json) - Syncs BUT...**

✅ **File syncs via git**
❌ **stdio servers won't work on web!**

```json
// .mcp.json (checked into git)
{
  "mcpServers": {
    "remote-api": {
      "transport": "http",           // ✅ Works on CLI + Web
      "url": "https://api.example.com/mcp"
    },
    "local-filesystem": {
      "command": "npx",               // ❌ CLI only (web can't spawn processes)
      "args": ["-y", "@modelcontextprotocol/server-filesystem"]
    }
  }
}
```

**User Config (~/.claude.json) - Never Syncs**

```json
// ~/.claude.json (local machine only)
{
  "mcpServers": {
    "dev-filesystem": {
      "command": "npx",               // CLI-only power features
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "."]
    },
    "local-postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        "DATABASE_URL": "postgresql://localhost:5432/dev"
      }
    }
  }
}
```

**Recommended Strategy:**

**For Cross-Platform Teams:**
```json
// .mcp.json - ONLY HTTP servers
{
  "mcpServers": {
    "company-api": {
      "transport": "http",
      "url": "https://mcp.company.com"
    }
  }
}

// Result: Works everywhere (CLI + Web)
```

**For CLI Power Users:**
```json
// .mcp.json - HTTP servers (team-wide)
{
  "mcpServers": {
    "prod-api": {
      "transport": "http",
      "url": "https://api.example.com"
    }
  }
}

// ~/.claude.json - stdio servers (personal, CLI-only)
{
  "mcpServers": {
    "local-filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "."]
    },
    "playwright": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-playwright"]
    }
  }
}

// Result:
// - CLI gets both HTTP + stdio (full power)
// - Web gets HTTP only (still functional)
// - No conflicts
```

**Configuration Scopes:**

```
Priority Order:
1. Local (.claude/settings.json)     ❌ Never syncs
2. Project (.mcp.json)               ✅ Syncs (but stdio won't work on web)
3. User (~/.claude.json)             ❌ Never syncs

Sync Mechanism: Git (not automatic cloud sync)
```

**Common Gotchas:**

❌ **Don't check stdio servers into .mcp.json**
- They'll be in git but won't work on web
- Team members using web will see errors

❌ **Don't expect local filesystem access on web**
- Web runs in isolated cloud sandbox
- No access to your machine's files

✅ **Do use HTTP servers for cross-platform**
- Works everywhere
- Better for production integrations

✅ **Do keep stdio servers in ~/.claude.json**
- CLI-only power features
- Not checked into git
- Personal development enhancements

**Decision Matrix:**

| Need | Solution | CLI | Web |
|------|----------|-----|-----|
| Team API access | HTTP in .mcp.json | ✅ | ✅ |
| Local file access | stdio in ~/.claude.json | ✅ | ❌ |
| Browser automation | stdio in ~/.claude.json | ✅ | ❌ |
| Local database | stdio in ~/.claude.json | ✅ | ❌ |
| Cloud service | HTTP in .mcp.json | ✅ | ✅ |

---

## Research Sources

1. https://blog.sshh.io/p/how-i-use-every-claude-code-feature
2. docs.claude.com (official documentation)
3. anthropic.com/engineering (best practices blog)
4. Community guides on eesel.ai, Medium, Dev.to
5. GitHub repos with Claude Code configurations
6. ClaudeLog.com (comprehensive guides)
7. Various technical blogs and guides

---

