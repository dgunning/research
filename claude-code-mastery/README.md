# Claude Code Mastery: The Complete Guide to Top 1% Usage

## Original Prompt

> I want to be the best in Toronto at using Claude Code both cli and web. Look at how people are using Claude Code e.g. https://blog.sshh.io/p/how-i-use-every-claude-code-feature, the ways to use both cli and web effectively, how to setup .claude settings, agents and commands so it works on the web. At the end of the research I must be in the 99th percentile Claude code developers

---

## Table of Contents

1. [The 99th Percentile Mindset](#the-99th-percentile-mindset)
2. [Essential Configuration](#essential-configuration)
3. [CLI Mastery](#cli-mastery)
4. [Web Mastery](#web-mastery)
5. [CLAUDE.md: Your Project Constitution](#claudemd-your-project-constitution)
6. [Custom Commands That Matter](#custom-commands-that-matter)
7. [Subagents Done Right](#subagents-done-right)
8. [MCP Integration Strategy](#mcp-integration-strategy)
9. [Hooks: Test Before Commit](#hooks-test-before-commit)
10. [Context Management Mastery](#context-management-mastery)
11. [Advanced Workflows](#advanced-workflows)
12. [GitHub Integration](#github-integration)
13. [Power User Patterns](#power-user-patterns)
14. [Anti-Patterns to Avoid](#anti-patterns-to-avoid)
15. [Quick Reference](#quick-reference)

---

## The 99th Percentile Mindset

### What Separates Top 1% Users

**They understand the tradeoffs:**
- ✅ Minimal, high-value custom commands (not dozens)
- ✅ CLAUDE.md as guardrails (not encyclopedias)
- ✅ Context management as active practice (not passive hope)
- ✅ Hooks at submission points (not mid-workflow)
- ✅ Just-in-time context loading (not everything upfront)

**They know the costs:**
- Baseline context: ~20k tokens (10%) in monorepos
- Each MCP server: Tool definitions added to system prompt
- @-mentioning extensive docs: Massive context bloat
- Automatic `/compact`: "Opaque, error-prone, not well-optimized"

**They measure obsessively:**
- Run `/context` mid-session
- Analyze `~/.claude/projects/` logs for patterns
- Track permission request frequency
- Monitor error patterns
- Iterate on CLAUDE.md based on data

**Core Philosophy:**
> "If you have a long list of complex, custom slash commands, you've created an anti-pattern." — Power user principle

---

## Essential Configuration

### Directory Structure

```
~/.claude/                           # Global settings
├── settings.json                    # User-wide config
└── projects/                        # Session logs (analyze these!)

your-project/
├── .claude/                         # Project-specific (check into git!)
│   ├── settings.json                # Team-shared config
│   ├── settings.local.json          # Personal (gitignored)
│   ├── commands/                    # Custom slash commands
│   │   ├── catchup.md              # Reads changed git files
│   │   └── pr.md                   # Clean, stage, prepare PR
│   ├── agents/                      # Subagent definitions
│   │   ├── architect.md            # Read-heavy: review architecture
│   │   └── implementer.md          # Write-heavy: implement features
│   └── .mcp.json                    # MCP server configuration
├── CLAUDE.md                        # Project constitution (CRITICAL)
└── .gitignore                       # Exclude settings.local.json
```

### The Three Configuration Levels

**1. User Settings (`~/.claude/settings.json`)**
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
  },
  "permissions": {
    "bash": {
      "deny": ["rm -rf /", "sudo"]
    },
    "read": {
      "deny": [".env", "**/*secret*", "**/*.key"]
    }
  },
  "MCP_TOOL_TIMEOUT": 60000,
  "BASH_MAX_TIMEOUT_MS": 300000
}
```

**2. Project Settings (`.claude/settings.json`)** — Check into git
```json
{
  "HTTPS_PROXY": "http://localhost:8888",
  "permissions": {
    "bash": {
      "allow": ["npm", "git", "pytest", "cargo"]
    }
  },
  "announcements": {
    "message": "Remember: Always run tests before committing!"
  }
}
```

**3. Local Settings (`.claude/settings.local.json`)** — Gitignored
```json
{
  "apiKeyHelper": "/path/to/custom-auth-script.sh",
  "ANTHROPIC_API_KEY": "sk-ant-..."
}
```

### What Syncs Between CLI and Web

✅ **Syncs (if in project):**
- `CLAUDE.md`
- `.claude/commands/`
- `.claude/agents/`
- `.mcp.json` ⚠️ **BUT with critical limitation (see below)**
- `.claude/settings.json`

❌ **Doesn't sync:**
- `~/.claude/settings.json` (user-level)
- `.claude/settings.local.json` (personal)
- Global CLAUDE.md
- `~/.claude.json` (user MCP servers)

**Strategy:** Check `.claude/` into git for team consistency.

### ⚠️ MCP Configuration: The Critical Sync Limitation

**The Architecture Constraint:**

```
CLI (Your Machine)                    Web (Anthropic Cloud)
├── Can spawn local processes  ✅     ├── Isolated sandbox       ⚠️
├── Access local filesystem    ✅     ├── No local access        ❌
├── Run stdio MCP servers      ✅     ├── stdio servers          ❌
└── Connect HTTP MCP servers   ✅     └── HTTP servers only      ✅
```

**MCP Transport Support:**

| Transport | CLI | Web | Example Use Case |
|-----------|-----|-----|------------------|
| **stdio** (local processes) | ✅ | ❌ | Filesystem, Playwright, local DB |
| **HTTP** (remote servers) | ✅ | ✅ | Company APIs, cloud services |

**What This Means:**

While `.mcp.json` **file syncs via git**, **stdio servers won't work on web!**

```json
// ❌ PROBLEM: This syncs but breaks web version
// .mcp.json (checked into git)
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",  // ❌ Web can't spawn local processes!
      "args": ["-y", "@modelcontextprotocol/server-filesystem"]
    }
  }
}
```

**The Solution: Separate Concerns**

**For cross-platform teams (.mcp.json - checked in):**
```json
{
  "mcpServers": {
    "company-api": {
      "transport": "http",
      "url": "https://mcp.company.com",
      "env": {
        "API_KEY": "${COMPANY_API_KEY}"
      }
    }
  }
}
```
✅ Works on CLI ✅ Works on Web ✅ Team consistency

**For CLI power users (~/.claude.json - local only):**
```json
{
  "mcpServers": {
    "local-filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "."]
    },
    "playwright": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-playwright"]
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
✅ CLI gets full power (HTTP + stdio)
❌ Never syncs to web (and shouldn't!)

**Configuration Scope Priority:**

```
1. Local (.claude/settings.json)    ❌ Never syncs
2. Project (.mcp.json)              ✅ Syncs via git (but stdio breaks web)
3. User (~/.claude.json)            ❌ Never syncs

Sync Mechanism: Git (not automatic cloud sync)
```

---

## CLI Mastery

### Essential Commands

**Context Management:**
```bash
/clear              # Hard reset - use often!
/context            # Check token usage mid-session
/compact keep X     # Manual compaction with instructions
```

**Development Flow:**
```bash
/init               # Initialize project understanding
/catchup            # Custom: Read changed git files
/pr                 # Custom: Clean, stage, prepare PR
```

**Version Control:**
```bash
Esc + Esc           # Rewind to checkpoint (or /rewind)
/rewind             # Choose: code, conversation, or both
```

**Tools & Debug:**
```bash
/help               # Show all commands
/permissions        # Manage domain allowlist
/mcp                # Manage MCP servers
```

### Headless Mode (Power User Feature)

**Non-interactive automation:**
```bash
# Single prompt execution
claude -p "Run tests and fix any failures"

# Streaming JSON output (for parsing)
claude -p "Analyze codebase" --output-format stream-json

# Use in CI/CD, pre-commit hooks, build scripts
```

**Parallel scripting pattern:**
```bash
#!/bin/bash
# Massive parallel automation

# Spawn multiple Claude instances in parallel
claude -p "Test backend" &
claude -p "Test frontend" &
claude -p "Test integration" &

wait  # Wait for all to complete
```

### Skip Permissions Mode

**For experienced users:**
```bash
# Every session:
claude --dangerously-skip-permissions

# Not as dangerous as it sounds - like old "yolo mode"
# Eliminates friction for power users
# Still respects settings.json permissions
```

### Configuration File Location

**Preferred:** `~/.claude.json` (most consistent)
```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/workspace"]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN}"
      }
    }
  }
}
```

### Advanced Debugging

```bash
# Debug MCP connections
claude --mcp-debug

# Proxy for prompt inspection
export HTTPS_PROXY=http://localhost:8888
claude

# Analyze session logs
ls -lht ~/.claude/projects/
cat ~/.claude/projects/[latest]/transcript.json | jq '.messages[] | select(.type == "error")'
```

---

## Web Mastery

### When to Use Web vs CLI

**Use Web When:**
- 🌐 No local setup available
- 📱 Working from mobile/tablet
- 🔄 Need parallel tasks across multiple repos
- ⚡ Quick prototyping without environment setup
- 👥 Collaborating on cloud-hosted tasks
- 🐳 Want Anthropic-managed containers

**Use CLI When:**
- 💻 Local development with existing setup
- 🎛️ Need full control over environment
- 📁 Working with local files and tools
- 🔧 Using custom hooks and scripts
- ⚙️ Maximum customization required
- 🔒 Sensitive codebases (on-premise)

### Web-Specific Features

**Parallel Execution:**
- Run multiple tasks simultaneously across different repos
- Each in isolated sandbox environment
- Web UI shows all in progress

**Teleport Feature:**
- Copy chat transcript + edited files to local CLI
- Seamless transition: Web exploration → CLI detailed work
- Command: Click "Teleport to CLI" in web interface

**Mobile Access:**
- Full Claude Code functionality via iOS app
- Navigate to claude.ai → "Code" tab
- Great for code reviews on-the-go

### Making Settings Work on Web

**Project-level configuration (`.claude/` directory):**
1. Create `.claude/` in project root
2. Add `settings.json`, `commands/`, `agents/`
3. Check into git
4. Push to GitHub
5. Open project on claude.ai/code
6. Settings automatically loaded

**Example project setup:**
```bash
cd your-project

# Create .claude directory structure
mkdir -p .claude/{commands,agents}

# Add custom commands
cat > .claude/commands/catchup.md << 'EOF'
Read all files changed in the current git branch compared to main.
Focus on understanding what changed and why.
EOF

# Add settings
cat > .claude/settings.json << 'EOF'
{
  "permissions": {
    "bash": {
      "allow": ["npm", "git", "pytest"]
    }
  }
}
EOF

# Check into git
git add .claude/
git commit -m "Add Claude Code configuration"
git push

# Now works on both CLI and Web!
```

### MCP Configuration for Web: Critical Limitations

**⚠️ Remember:** Web version **cannot run stdio MCP servers** (local processes)

**❌ This will NOT work on web:**
```json
// .mcp.json (don't do this if team uses web!)
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",  // ❌ Web can't spawn local processes
      "args": ["-y", "@modelcontextprotocol/server-filesystem"]
    }
  }
}
```

**✅ This WILL work on both CLI and web:**
```json
// .mcp.json (cross-platform compatible)
{
  "mcpServers": {
    "company-api": {
      "transport": "http",  // ✅ Works everywhere
      "url": "https://mcp.company.com",
      "env": {
        "API_KEY": "${COMPANY_API_KEY}"
      }
    }
  }
}
```

**Best Practice: Hybrid Approach**

```bash
# 1. Project config (.mcp.json) - HTTP only, for team
cat > .mcp.json << 'EOF'
{
  "mcpServers": {
    "prod-api": {
      "transport": "http",
      "url": "https://api.example.com/mcp"
    }
  }
}
EOF

# 2. Local config (~/.claude.json) - stdio servers, for CLI power
cat > ~/.claude.json << 'EOF'
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
EOF

# Result:
# - CLI gets both HTTP + stdio (full power)
# - Web gets HTTP only (still functional)
# - Team members using web won't see errors
```

**Decision Guide:**

| Your Team Uses | .mcp.json Should Contain | ~/.claude.json Can Contain |
|----------------|-------------------------|---------------------------|
| CLI only | HTTP or stdio (your choice) | Additional stdio servers |
| Web only | **HTTP servers ONLY** | N/A (doesn't sync) |
| Both CLI and Web | **HTTP servers ONLY** | stdio servers (CLI bonus) |

### Security on Web

**Isolated Sandboxes:**
- Every task runs in separate container
- Network restrictions enforced
- Filesystem access limited
- Git via secure proxy only

**Repository Access:**
- Must explicitly authorize repos
- Can only access what you've granted
- Revoke access anytime via GitHub settings

---

## CLAUDE.md: Your Project Constitution

### The Power User Approach

**Philosophy (from top 1% user):**
- 13KB maximum - "token budget like ad space"
- Document only tools used by 30%+ of engineers
- Start with guardrails, not comprehensive manuals
- Avoid @-mentioning extensive docs (creates bloat)
- Never use negative-only constraints
- Always provide alternatives

**What Claude prioritizes:**
> "The contents of CLAUDE.md are adhered to MUCH MORE strictly than the user prompt."

### Template: Professional Projects

```markdown
# Project: [Name]

## Tech Stack
- **Framework**: Next.js 14.2.3 with App Router
- **Language**: TypeScript 5.4
- **Styling**: Tailwind CSS 3.4
- **Database**: PostgreSQL 16 + Prisma 5.12
- **Testing**: Vitest + Playwright
- **Deployment**: Vercel

## Critical Rules

### Code Style
- Use functional components with hooks
- Prefer `const` over `let`
- Max line length: 100 characters
- Max file size: 300 lines (suggest split if exceeded)

### Testing Requirements
- All new features require unit tests
- Coverage threshold: 80%
- Run `npm test` before committing
- Integration tests for API routes

### Git Workflow
- Branch naming: `feature/`, `fix/`, `refactor/`
- Commit after each logical unit of work
- Never commit directly to main
- Always create PR for review

### File Organization
```
src/
├── app/           # Next.js app directory
├── components/    # React components (max 200 lines each)
├── lib/           # Utility functions
├── hooks/         # Custom React hooks
└── types/         # TypeScript type definitions
```

### Common Pitfalls
- ❌ Don't use `any` type (use `unknown` or proper types)
- ❌ Don't mutate props or state directly
- ✅ Do use server components by default
- ✅ Do validate all user inputs with Zod

### When Stuck
1. Check existing similar components first
2. Read docs at: /docs/architecture.md
3. Ask for help (don't guess at patterns)

## Project-Specific Context
- Authentication via NextAuth.js with GitHub provider
- Database schema changes require migration: `npx prisma migrate dev`
- Environment variables in .env.local (never commit!)
- API routes use server actions (not traditional REST)
```

### Template: Minimalist (Anti-Pattern Avoidance)

```markdown
# Project Guardrails

## Stack
TypeScript + React + PostgreSQL

## Non-Negotiables
1. Tests must pass before commit
2. TypeScript strict mode (no `any`)
3. Files < 300 lines

## Patterns
- Server components by default
- Zod for validation
- Prisma for database

## Resources
Don't @-mention full docs.
Instead: "Check docs/patterns.md for [specific topic]"

## Why This Matters
Concise CLAUDE.md = more tokens for actual code context.
```

### Global CLAUDE.md

**Location:** `~/.claude/CLAUDE.md`

**Purpose:** Apply to all projects

```markdown
# Global Development Preferences

## General Principles
- Write clear, self-documenting code
- Prefer explicit over clever
- Comments explain WHY, not WHAT

## Language Preferences
- **Python**: Type hints, dataclasses, pytest
- **TypeScript**: Strict mode, functional style
- **Rust**: Idiomatic, use clippy suggestions

## Before Committing
Always:
1. Run linter
2. Run tests
3. Check git diff

## Communication Style
- Be concise but thorough
- Explain tradeoffs when suggesting alternatives
- If uncertain, ask rather than guess
```

### Hierarchical CLAUDE.md

**Power feature:** Nested CLAUDE.md files

```
project/
├── CLAUDE.md                    # Project-wide rules
├── frontend/
│   └── CLAUDE.md               # Frontend-specific (React patterns)
└── backend/
    └── CLAUDE.md               # Backend-specific (API patterns)
```

**Priority:** Most specific (nested) > General (root)

---

## Custom Commands That Matter

### The Minimal Philosophy

> "If you have a long list of complex custom commands, you've created an anti-pattern."

**Top 1% users maintain 2-3 commands maximum:**
1. `/catchup` - Read changed git files
2. `/pr` - Prepare pull request
3. Maybe one project-specific

### Example: /catchup

**File:** `.claude/commands/catchup.md`

```markdown
Read all files that have changed in the current git branch compared to main.

Steps:
1. Run: `git diff main...HEAD --name-only`
2. Read each changed file in full
3. Summarize what changed and why (infer from diffs)
4. Ask if I want details on any specific changes

Focus on understanding the overall direction, not line-by-line analysis.
```

### Example: /pr

**File:** `.claude/commands/pr.md`

```markdown
Prepare a pull request for the current branch.

Steps:
1. Run linter and fix any issues
2. Run tests (must pass!)
3. Review git diff for any debug code or TODOs
4. Clean up: Remove console.logs, commented code
5. Stage all changes: `git add .`
6. Generate commit message summarizing changes
7. Commit with descriptive message
8. Ask if ready to push and create PR

If tests fail: Fix them before proceeding. No commits with failing tests.
```

### Example: /review (Project-Specific)

**File:** `.claude/commands/review.md`

```markdown
Code review checklist for this project.

Check:
- [ ] TypeScript: No `any` types
- [ ] Tests: Coverage > 80%
- [ ] Security: All inputs validated with Zod
- [ ] Performance: No unnecessary re-renders
- [ ] Accessibility: ARIA labels on interactive elements
- [ ] Error handling: All async functions have try/catch
- [ ] Documentation: Complex logic has comments

Provide pass/fail for each item with file:line references.
```

### Using $ARGUMENTS

**File:** `.claude/commands/test.md`

```markdown
Run tests for specific file or pattern.

Usage: `/test $ARGUMENTS`

Examples:
- `/test src/components/Button.test.ts`
- `/test "**/*.integration.test.ts"`

Steps:
1. Parse arguments as file pattern
2. Run: `npm test $ARGUMENTS`
3. If failures, analyze and suggest fixes
4. Re-run until passing
```

### Team Sharing

```bash
# Commands in .claude/commands/ are checked into git
cd your-project
git add .claude/commands/
git commit -m "Add custom Claude Code commands"
git push

# Team members automatically get them!
```

---

## Subagents Done Right

### The Master-Clone Pattern

**Top 1% approach:**
- ❌ **Don't:** Create custom subagents that gatekeep context
- ✅ **Do:** Use built-in `Task(...)` to spawn dynamic clones

**Why:**
> "Custom subagents force rigid human-defined workflows. Built-in Task(...) lets Claude orchestrate dynamically."

### When to Use Subagents

**Good use cases:**
1. **Parallelizable tasks** - Search multiple sources simultaneously
2. **Scoped investigation** - Research API docs without polluting main context
3. **Early verification** - Check assumptions before main work
4. **Context preservation** - Prevent pollution in long conversations

**Bad use cases:**
1. Sequential workflows (just use main agent)
2. Simple single-purpose tasks (overhead not worth it)
3. When you need full context (subagents have independent windows)

### Subagent Definition Format

**File:** `.claude/agents/architect.md`

```yaml
---
name: architect
description: Reviews code architecture and design patterns
tools: [Read, Glob, Grep]
---

You are an experienced software architect focused on:

## Your Role
- Review overall code structure and organization
- Identify architectural anti-patterns
- Suggest design improvements
- Check for separation of concerns

## What You Check
1. **Module organization**: Logical grouping, clear boundaries
2. **Dependencies**: Circular deps, tight coupling
3. **Scalability**: Can this grow without rewrite?
4. **Testability**: Is code structured for easy testing?

## Output Format
Provide:
- Overall architecture assessment (1-5 score)
- Top 3 issues (with file:line references)
- Top 3 improvements (specific, actionable)
- Estimated refactor effort (hours)

## Constraints
- You have READ-ONLY access (no edits)
- Focus on structure, not style
- Reference design patterns by name
- Explain WHY changes help
```

**File:** `.claude/agents/implementer.md`

```yaml
---
name: implementer
description: Implements features with tests
tools: [Read, Write, Edit, Bash, Glob, Grep]
---

You are an implementation specialist focused on:

## Your Role
- Implement features according to specs
- Write comprehensive tests
- Follow project conventions
- Ensure code quality

## Workflow
1. Read relevant existing code
2. Understand patterns and conventions
3. Implement feature
4. Write unit tests
5. Run tests (must pass!)
6. Clean up (no debug code)

## Quality Checklist
Before marking done:
- [ ] Tests written and passing
- [ ] No TypeScript errors
- [ ] Follows project style (check CLAUDE.md)
- [ ] Error handling in place
- [ ] No console.logs or TODOs

## Constraints
- Always run tests before finishing
- If tests fail, fix before proceeding
- Match existing code style exactly
- Ask if unclear about requirements
```

### Tool Scoping Strategy

**Principle:** "If omit tools = grant all. Be intentional."

```yaml
# Architect: Read-only
tools: [Read, Glob, Grep]

# Implementer: Full power
tools: [Read, Write, Edit, Bash, Glob, Grep]

# Reviewer: Read + limited bash
tools: [Read, Glob, Grep, Bash]  # Bash for running tests only

# Researcher: Read + web
tools: [Read, WebFetch, WebSearch]
```

### Parallel Subagent Pattern

**Example:** Email research agent

```yaml
---
name: email-researcher
description: Researches email history for relevant information
---

When given a research query:

1. Spawn multiple search subagents in parallel
2. Each runs different query against email history
3. Each returns only relevant excerpts (not full emails)
4. Synthesize results into coherent summary

Pattern:
- Search subagent 1: Recent emails (last 30 days)
- Search subagent 2: Specific sender
- Search subagent 3: Specific keywords
- Search subagent 4: Related threads

Return: Consolidated findings with references
```

### Interactive Creation

```bash
# Build agents interactively
claude
> /agents

# Follow prompts to create agent definition
# Saved to .claude/agents/[name].md
```

---

## MCP Integration Strategy

### The Philosophy Shift

**Old thinking:** Wrap every REST endpoint as MCP tool
**New thinking (from top 1%):**
> "MCPs are simple, secure gateways with FEW high-level tools. Migrate stateless tools to CLIs."

**Keep as MCP:**
- Playwright (stateful browser automation)
- Database connections (persistent state)
- File watchers (continuous monitoring)

**Migrate to simple CLIs:**
- Jira operations (stateless HTTP)
- AWS commands (stateless API calls)
- GitHub operations (stateless API)

### Transport Types: stdio vs HTTP

**Critical distinction for CLI vs Web:**

**stdio Transport (Local Processes):**
```json
{
  "command": "npx",
  "args": ["-y", "@modelcontextprotocol/server-filesystem", "/workspace"]
}
```
- ✅ CLI: Full support
- ❌ Web: **Not supported** (no local process execution)
- Use for: Local development tools (filesystem, Playwright, local DB)

**HTTP Transport (Remote Servers):**
```json
{
  "transport": "http",
  "url": "https://mcp.example.com"
}
```
- ✅ CLI: Full support
- ✅ Web: **Full support**
- Use for: Cloud services, company APIs, production integrations

### Configuration

**Global:** `~/.claude.json`

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/workspace"],
      "env": {}
    },
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        "DATABASE_URL": "${POSTGRES_URL}"
      }
    },
    "playwright": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-playwright"],
      "env": {}
    }
  }
}
```

**Project:** `.mcp.json` (checked into git)

```json
{
  "mcpServers": {
    "project-db": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        "DATABASE_URL": "postgresql://localhost:5432/myproject"
      }
    }
  }
}
```

### Context Window Management

**Problem:** Each MCP server adds tool definitions to system prompt

**Solution:** Toggle servers dynamically

```bash
# Check which servers are enabled
claude
> /mcp

# @-mention to toggle
> @filesystem  # Toggles filesystem MCP on/off

# Only enable what you need for current task
```

### Adding MCP Servers

**Method 1: CLI Wizard (Recommended)**

```bash
# HTTP server
claude mcp add --transport http my-api https://api.example.com

# Local stdio server
claude mcp add my-tool npx -y my-mcp-package
```

**Method 2: Direct Edit (For Complex Configs)**

```bash
# Edit ~/.claude.json directly
vim ~/.claude.json

# Add server configuration
# Useful when many env vars or complex args
```

### Debugging MCP

```bash
# Enable MCP debug logging
claude --mcp-debug

# Check server health
claude
> /mcp
# Shows status of all configured servers
```

### Security Best Practices

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/workspace"  // ✅ Restricted to specific directory
        // ❌ Never use "/" root access
      ]
    },
    "database": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        // ✅ Use environment variable reference
        "DATABASE_URL": "${POSTGRES_URL}"
        // ❌ Never hardcode: "postgresql://user:pass@host/db"
      }
    }
  }
}
```

---

## Hooks: Test Before Commit

### The Power User Strategy

> "Block at submit, not mid-plan. Blocking agent mid-plan confuses or even frustrates it."

**PreToolUse Hook Pattern:**

**File:** `.claude/hooks/pre-tool-use.sh`

```bash
#!/bin/bash
# Block git commits unless tests pass

TOOL_NAME=$1
TOOL_ARGS=$2

# Only intercept git commit commands
if [[ $TOOL_NAME == "Bash" ]] && echo "$TOOL_ARGS" | grep -q "git commit"; then
  # Check if tests have passed
  if [[ ! -f /tmp/agent-pre-commit-pass ]]; then
    echo "❌ Tests must pass before committing!"
    echo "Run tests first, then retry commit."
    exit 1  # Block the tool execution
  fi

  # Tests passed, allow commit
  rm /tmp/agent-pre-commit-pass  # Clean up flag
  exit 0  # Allow tool execution
fi

# Allow all other tools
exit 0
```

**Workflow:**
1. Claude attempts to commit
2. Hook checks for `/tmp/agent-pre-commit-pass` file
3. If not exists: Block commit, force test-and-fix loop
4. Claude runs tests, fixes failures
5. Tests pass → creates flag file
6. Retry commit → succeeds

**File:** `.claude/hooks/post-tool-use.sh`

```bash
#!/bin/bash
# Create pass flag after successful test run

TOOL_NAME=$1
TOOL_ARGS=$2
EXIT_CODE=$3

# If pytest passed, create flag
if [[ $TOOL_NAME == "Bash" ]] && echo "$TOOL_ARGS" | grep -q "pytest"; then
  if [[ $EXIT_CODE == "0" ]]; then
    touch /tmp/agent-pre-commit-pass
    echo "✅ Tests passed! Ready to commit."
  fi
fi
```

### Hook Types

**PreToolUse:**
- Runs before tool executes
- Can block execution (exit 1)
- Can modify arguments
- Use for: Validation, checks, guards

**PostToolUse:**
- Runs after tool completes
- Receives exit code
- Can trigger follow-up actions
- Use for: Cleanup, notifications, logging

**UserPromptSubmit:**
- Runs when user submits prompt
- Can modify prompt
- Can add context
- Use for: Auto-injecting context, prompt enhancement

### Hint Hooks (Non-Blocking)

**File:** `.claude/hooks/user-prompt-submit.sh`

```bash
#!/bin/bash
# Non-blocking hint to remind about best practices

USER_PROMPT=$1

# If asking to write code, hint about testing
if echo "$USER_PROMPT" | grep -qi "implement\|create\|add feature"; then
  echo "💡 Hint: Don't forget to write tests!"
  echo "💡 Hint: Check CLAUDE.md for coding standards"
fi

# Always allow prompt (exit 0)
exit 0
```

### Configuration

**File:** `.claude/settings.json`

```json
{
  "hooks": {
    "preToolUse": ".claude/hooks/pre-tool-use.sh",
    "postToolUse": ".claude/hooks/post-tool-use.sh",
    "userPromptSubmit": ".claude/hooks/user-prompt-submit.sh"
  },
  "permissions": {
    "bash": {
      "allow": ["pytest", "npm test", "cargo test", "git"]
    }
  }
}
```

### Real-World Example: Formatter Hook

**File:** `.claude/hooks/post-tool-use.sh`

```bash
#!/bin/bash
# Auto-format after file edits

TOOL_NAME=$1
EXIT_CODE=$3

# If file was edited successfully, format it
if [[ $TOOL_NAME == "Edit" || $TOOL_NAME == "Write" ]] && [[ $EXIT_CODE == "0" ]]; then
  # Extract file path from tool output (you'd parse this properly)
  # For demo: assume edited files are staged

  # Run formatter
  npx prettier --write $(git diff --cached --name-only)

  echo "✅ Files auto-formatted"
fi
```

---

## Context Management Mastery

### The Three Strategies

**1. `/clear` + `/catchup` (Default)**
```bash
# Hard reset when starting new feature
/clear

# Custom command reads all changed files in branch
/catchup

# Clean slate with only relevant changes loaded
```

**2. Document & Clear (Complex Tasks)**
```markdown
# When context getting unwieldy:

1. Ask Claude to document progress:
   "Document current state: what's done, what's left, key decisions"

2. Save documentation to file

3. /clear (hard reset)

4. Resume from documentation:
   "Read progress.md and continue from where we left off"
```

**3. Manual Compaction (Pivot Points)**
```bash
# When changing focus but keeping some context
/compact keep the authentication implementation and database schema

# Compacts context but preserves specified items
# Better than automatic /compact (which is "opaque, error-prone")
```

### Token Budget Awareness

**Check usage mid-session:**
```bash
/context

# Output shows:
# - Total tokens used
# - Breakdown by category
# - % of window consumed

# Baseline in monorepos: ~20k tokens (10%)
# If > 50%: Consider /clear or /compact
```

### Just-in-Time Context Loading

**Bad (loads everything upfront):**
```markdown
@-mention docs/api-reference.md
@-mention docs/architecture.md
@-mention docs/contributing.md

Now implement feature X
```

**Good (loads on-demand):**
```markdown
Implement feature X

# Claude discovers it needs API info
# Uses tools to read docs/api-reference.md
# Only loads what's needed, when needed
```

**CLAUDE.md strategy:**
```markdown
## Documentation

Don't @-mention full docs.

Instead:
- "API reference at docs/api-reference.md"
- "Architecture explained in docs/architecture.md"
- "For auth patterns, check docs/auth-guide.md"

Let Claude read only what it needs for current task.
```

### Avoiding Context Bloat

**❌ Anti-patterns:**
```markdown
# Dumps entire API spec into context
@-mention openapi.yaml

# Forces reading of huge files
Read all files in src/

# Loads irrelevant documentation
@-mention docs/ (recursive)
```

**✅ Best practices:**
```markdown
# Specific file mentions
Look at src/auth/login.ts for the login pattern

# Targeted documentation
Check docs/auth-guide.md section on JWT handling

# Lazy loading
# (Let Claude discover files via Glob/Grep when needed)
```

### The /clear Discipline

**When to /clear:**
- Starting new feature
- Switching context significantly
- After completing major milestone
- When context > 50% capacity
- Feeling "context drift" (Claude seems confused)

**Frequency (top 1% users):**
- Every 30-60 minutes of active work
- After every major task completion
- "Use /clear often. Every time you start something new."

### Multi-Context Window Workflows

**For large, complex features:**

```markdown
# Session 1: Research & Planning
Task: Research authentication best practices
Output: Save to docs/auth-plan.md

# /clear

# Session 2: Database Schema
Task: Design user tables based on auth-plan.md
Output: Save migration to db/migrations/

# /clear

# Session 3: Implementation
Task: Implement auth based on auth-plan.md and migration
Output: Working authentication system

# /clear

# Session 4: Testing
Task: Write comprehensive auth tests
```

**Why it works:**
- Claude 4.5 has exceptional state tracking
- Can save/resume across sessions
- Each session starts with clean context
- Make steady advances on few things at a time

---

## Advanced Workflows

### Master-Clone Architecture

**Pattern:**
```markdown
Main agent (you interact with):
  ↓
  Spawns Task(...) clones dynamically:
    - Clone 1: Research API docs
    - Clone 2: Review existing code
    - Clone 3: Search for examples
  ↓
  Clones return distilled results
  ↓
  Main agent synthesizes and implements
```

**Example:**
```markdown
You: "Implement OAuth authentication"

Claude (main agent):
"I'll spawn subagents to research:
- Task 1: Review our current auth implementation
- Task 2: Research OAuth 2.0 best practices
- Task 3: Find example implementations in our stack

(Spawns 3 clones in parallel)

(Clones return findings)

Based on research:
- Current: Simple JWT auth
- Best practice: OAuth 2.0 with PKCE
- Example: next-auth library

Proceeding with implementation..."
```

**Why it works:**
- No rigid human-defined workflows
- Claude orchestrates dynamically
- Clones don't gatekeep context
- Main agent has full decision-making power

### Planning Mode

**For large features:**
```bash
/plan

# Claude enters planning mode
# Breaks down feature into steps
# Identifies dependencies
# Creates checklist
# Asks for approval before proceeding
```

**Custom planning (production):**
```markdown
# In CLAUDE.md:

## Planning Process
For features estimated > 4 hours:

1. Create design document in docs/designs/
2. Include:
   - Problem statement
   - Proposed solution
   - Alternatives considered
   - Security implications
   - Performance impact
   - Testing strategy
3. Get approval before implementation
4. Reference design doc in PR
```

### GitHub Actions as Operationalization Layer

**Pattern:** AI-driven PR generation

```yaml
# .github/workflows/claude-automation.yml
name: Claude Automation

on:
  issues:
    types: [labeled]

jobs:
  claude-fix:
    if: github.event.label.name == 'claude-fix'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Run Claude Code
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          # Install Claude CLI
          curl -fsSL https://claude.ai/install.sh | bash

          # Run headless with issue as prompt
          claude -p "Fix issue #${{ github.event.issue.number }}: ${{ github.event.issue.title }}"

      - name: Create Pull Request
        uses: peter-evans/create-pull-request@v5
        with:
          title: "Fix: ${{ github.event.issue.title }}"
          body: "Automated fix by Claude Code for #${{ github.event.issue.number }}"
          branch: claude/fix-${{ github.event.issue.number }}
```

**Triggers:**
- Issue labeled with "claude-fix"
- Slack alert → webhook → GitHub Action → Claude
- CloudWatch alarm → SNS → GitHub Action → Claude
- Jira ticket created → webhook → GitHub Action → Claude

**Data flywheel:**
```
Bug reported
  ↓
Claude generates fix
  ↓
PR reviewed (logs captured)
  ↓
Analyze logs for patterns
  ↓
Update CLAUDE.md with learnings
  ↓
Next fix is better
```

### Parallel Scripting

**Massive automation:**
```bash
#!/bin/bash
# parallel-refactor.sh

# Array of directories to refactor
DIRS=(
  "src/auth"
  "src/api"
  "src/components"
  "src/utils"
)

# Spawn Claude instance for each
for dir in "${DIRS[@]}"; do
  (
    claude -p "Refactor $dir to TypeScript strict mode" \
      --output-format stream-json > "logs/$dir.json"
  ) &
done

# Wait for all to complete
wait

echo "All refactorings complete!"
```

**Use cases:**
- Migrating large codebase
- Running different test suites in parallel
- Generating documentation for multiple modules
- Analyzing different parts of system

### Historical Analysis

**Analyze your Claude usage:**
```bash
# Session logs location
ls -lht ~/.claude/projects/

# Analyze common errors
cat ~/.claude/projects/*/transcript.json | \
  jq '.messages[] | select(.type == "error") | .content' | \
  sort | uniq -c | sort -rn

# Analyze permission requests
cat ~/.claude/projects/*/transcript.json | \
  jq '.messages[] | select(.content | contains("permission")) | .content' | \
  sort | uniq -c

# Find common patterns
grep -r "Failed to" ~/.claude/projects/*/transcript.json | \
  cut -d: -f2 | sort | uniq -c | sort -rn
```

**Data-driven improvements:**
1. Identify most common errors
2. Add guardrails to CLAUDE.md
3. Create custom commands for repeated tasks
4. Adjust permissions in settings.json
5. Improve CLIs/tools based on failure patterns

---

## GitHub Integration

### Quick Setup

```bash
# In your project
claude
> /install-github-app

# Follow prompts to:
# 1. Install GitHub App on your repos
# 2. Grant necessary permissions
# 3. Configure repository access

# Done! Claude can now:
# - Review PRs automatically
# - Create PRs
# - Respond to @claude mentions
```

### Automated PR Review

**Configuration:** `.github/workflows/claude-review.yml`

```yaml
name: Claude PR Review

on:
  pull_request:
    types: [opened, synchronize]

jobs:
  review:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      pull-requests: write

    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0  # Get full history for better context

      - name: Claude Review
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          # Review focuses on CLAUDE.md criteria
          claude -p "Review this PR according to CLAUDE.md standards. Focus on:
          - Code style compliance
          - Test coverage
          - Security issues
          - Performance concerns

          Provide specific file:line feedback."
```

### On-Demand Review

**Configuration:** `.github/workflows/claude-on-demand.yml`

```yaml
name: Claude On-Demand Review

on:
  issue_comment:
    types: [created]

jobs:
  review:
    if: contains(github.event.comment.body, '@claude')
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Extract Request
        id: parse
        run: |
          # Parse @claude request
          REQUEST=$(echo "${{ github.event.comment.body }}" | sed 's/@claude //')
          echo "request=$REQUEST" >> $GITHUB_OUTPUT

      - name: Claude Response
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          claude -p "${{ steps.parse.outputs.request }}"

      - name: Post Response
        uses: actions/github-script@v7
        with:
          script: |
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: process.env.CLAUDE_RESPONSE
            })
```

### Security Best Practices

**Minimal permissions:**
```yaml
permissions:
  contents: read        # ✅ Read codebase
  pull-requests: write  # ✅ Comment on PRs
  # contents: write     # ❌ Only if Claude should push commits
```

**Secret management:**
```bash
# Add via GitHub UI: Settings → Secrets and variables → Actions
ANTHROPIC_API_KEY  # Your Claude API key

# Rotate periodically (quarterly recommended)
```

**Branch protection:**
```yaml
# .github/branch-protection.yml
main:
  required_reviews: 1  # Human approval required
  required_checks:
    - claude-review    # AI review must pass
    - tests           # Tests must pass
  no_force_push: true
```

### CLAUDE.md for PR Reviews

```markdown
# PR Review Criteria

## Code Style
- TypeScript strict mode (no `any`)
- Functional components with hooks
- Max file size: 300 lines
- Max line length: 100 characters

## Testing
- Unit tests for all new functions
- Integration tests for API routes
- Coverage threshold: 80%
- All tests must pass

## Security
- All user inputs validated with Zod
- No hardcoded secrets (check for API keys)
- SQL queries use parameterized statements
- XSS prevention (sanitize all outputs)

## Performance
- No unnecessary re-renders
- Lazy load large components
- Optimize images (use Next.js Image)
- Database queries have proper indexes

## What to Ignore
- Formatting (Prettier handles this)
- Import order (ESLint handles this)
- Minor style preferences

## Tone
- Be constructive, not critical
- Explain WHY changes help
- Suggest specific improvements
- Note good patterns when you see them
```

---

## Power User Patterns

### 1. Proxy-Driven Prompt Inspection

```bash
# In settings.json:
{
  "HTTPS_PROXY": "http://localhost:8888"
}

# Run mitmproxy or similar
mitmproxy -p 8888

# See exactly what prompts Claude receives
# Useful for debugging context issues
# Analyze token usage patterns
# Optimize CLAUDE.md based on real data
```

### 2. Skip Permissions for Speed

```bash
# Power users start every session:
claude --dangerously-skip-permissions

# Eliminates permission prompts
# Still respects settings.json rules
# Like old "yolo mode" but controlled
```

### 3. Project Template

```bash
# Create template with ideal .claude/ setup
~/templates/claude-project/
├── .claude/
│   ├── settings.json
│   ├── commands/
│   │   ├── catchup.md
│   │   └── pr.md
│   └── agents/
│       ├── architect.md
│       └── implementer.md
└── CLAUDE.md

# New project:
cp -r ~/templates/claude-project/.claude .
cp ~/templates/claude-project/CLAUDE.md .
# Edit CLAUDE.md for project specifics
```

### 4. Context Budget Calculator

```bash
#!/bin/bash
# check-context-budget.sh

echo "Checking context budget..."

# CLAUDE.md size
CLAUDE_SIZE=$(wc -c < CLAUDE.md)
CLAUDE_TOKENS=$((CLAUDE_SIZE / 4))  # Rough estimate: 1 token ≈ 4 chars

echo "CLAUDE.md: ~$CLAUDE_TOKENS tokens"

# MCP servers
MCP_COUNT=$(jq '.mcpServers | length' ~/.claude.json 2>/dev/null || echo 0)
MCP_TOKENS=$((MCP_COUNT * 500))  # Rough: 500 tokens per server

echo "MCP servers ($MCP_COUNT): ~$MCP_TOKENS tokens"

# Baseline
BASELINE=20000

TOTAL=$((CLAUDE_TOKENS + MCP_TOKENS + BASELINE))
PERCENTAGE=$((TOTAL * 100 / 200000))

echo "Estimated baseline: $TOTAL tokens ($PERCENTAGE%)"
echo "Remaining for code: $((200000 - TOTAL)) tokens"

if [ $PERCENTAGE -gt 15 ]; then
  echo "⚠️  Warning: High baseline usage. Consider:"
  echo "  - Reduce CLAUDE.md size"
  echo "  - Disable unused MCP servers"
fi
```

### 5. Daily Session Review

```bash
#!/bin/bash
# review-sessions.sh

# Today's sessions
TODAY=$(date +%Y-%m-%d)
SESSIONS=~/.claude/projects/*$TODAY*

for session in $SESSIONS; do
  echo "Session: $(basename $session)"

  # Count errors
  ERRORS=$(cat $session/transcript.json | jq '[.messages[] | select(.type == "error")] | length')
  echo "  Errors: $ERRORS"

  # Count permission requests
  PERMS=$(cat $session/transcript.json | grep -c "permission")
  echo "  Permission requests: $PERMS"

  # Estimate tokens
  TOKENS=$(cat $session/transcript.json | jq '[.messages[].content | length] | add')
  TOKENS=$((TOKENS / 4))
  echo "  Est. tokens: ~$TOKENS"

  echo ""
done

# Aggregate learnings
echo "Common errors today:"
cat $SESSIONS/transcript.json 2>/dev/null | \
  jq -r '.messages[] | select(.type == "error") | .content' | \
  sort | uniq -c | sort -rn | head -5
```

### 6. Test-Driven Hook Workflow

```bash
# .claude/hooks/pre-tool-use.sh
#!/bin/bash

TOOL=$1
ARGS=$2

# Block commits without passing tests
if [[ $TOOL == "Bash" ]] && echo "$ARGS" | grep -q "git commit"; then
  # Run tests
  npm test

  if [ $? -ne 0 ]; then
    echo "❌ Tests failed! Fix before committing."
    exit 1
  fi

  echo "✅ Tests passed! Proceeding with commit."
fi

exit 0
```

### 7. Multi-Repo Workflow Script

```bash
#!/bin/bash
# sync-claude-config.sh

# Sync .claude/ configuration across all your repos

SOURCE=~/templates/claude-project/.claude
REPOS=(
  ~/projects/frontend
  ~/projects/backend
  ~/projects/mobile
)

for repo in "${REPOS[@]}"; do
  echo "Syncing to $repo..."

  # Copy base configuration
  rsync -av --exclude='settings.local.json' $SOURCE/ $repo/.claude/

  # Keep project-specific settings if they exist
  if [ -f $repo/.claude/settings.local.json ]; then
    echo "  Preserving local settings"
  fi

  echo "  ✓ Synced"
done

echo "All repos synced!"
```

---

## Anti-Patterns to Avoid

### ❌ The Anti-Pattern Hall of Shame

**1. Command Proliferation**
```bash
# DON'T create dozens of commands:
.claude/commands/
├── test-backend.md
├── test-frontend.md
├── test-integration.md
├── test-e2e.md
├── build-prod.md
├── build-dev.md
├── deploy-staging.md
├── deploy-prod.md
├── lint-fix.md
├── format-code.md
... (20 more)

# DO keep it minimal:
.claude/commands/
├── catchup.md
└── pr.md
```

**Why:** Long command lists = anti-pattern. Each adds cognitive load.

**2. Encyclopedia CLAUDE.md**
```markdown
# DON'T write a novel:

# API Documentation (2000 lines)
## Every endpoint explained in detail...
## Request formats...
## Response formats...
## Error codes...
## Rate limiting...
... (continues for pages)

# DO write guardrails:

# API Documentation
Located at docs/api-reference.md
Use when you need specific endpoint details.

Key principles:
- All endpoints require authentication
- Rate limit: 1000/hour
- Use pagination for lists (max 100 items)
```

**Why:** CLAUDE.md should be < 13KB. Token budget is limited.

**3. Custom Subagent Rigidity**
```yaml
# DON'T create rigid workflows:
---
name: feature-implementer
description: Must follow exact 10-step process
---

Step 1: Read requirements
Step 2: Check existing code
Step 3: Create design doc
Step 4: Get approval
Step 5: Write tests
Step 6: Implement feature
Step 7: Run tests
Step 8: Fix failures
Step 9: Create PR
Step 10: Deploy

# DO use flexible delegation:
Use built-in Task(...) to spawn clones dynamically.
Let Claude figure out the right workflow for the task.
```

**Why:** Rigid workflows gatekeep context and prevent adaptation.

**4. @-Mention Spam**
```markdown
# DON'T dump everything:
@-mention docs/api.md
@-mention docs/architecture.md
@-mention docs/deployment.md
@-mention README.md
@-mention CONTRIBUTING.md

Now implement feature X

# DO load selectively:
Implement feature X

(Let Claude discover what docs it needs)
(It will read only relevant sections)
```

**Why:** Wastes tokens on irrelevant context.

**5. Automatic /compact Dependence**
```bash
# DON'T rely on automatic compaction:
# (Just keep coding until context overflows)
# (Let /compact happen automatically)

# DO manage proactively:
/context  # Check usage
# At 50%: Consider /clear or manual /compact
/compact keep authentication logic and database schema
```

**Why:** Automatic compact is "opaque, error-prone, not well-optimized."

**6. Mid-Plan Blocking Hooks**
```bash
# DON'T block during planning:
# PreToolUse: Block every file edit for review

# DO block at commit time:
# PreToolUse: Block git commit until tests pass
```

**Why:** Blocking mid-plan "confuses or even frustrates" the agent.

**7. Negative-Only Constraints**
```markdown
# DON'T say what not to do:
## Code Style
- Don't use var
- Don't use any
- Don't mutate props
- Don't use inline styles

# DO provide alternatives:
## Code Style
- Use const/let (not var)
- Use proper types (not any)
- Keep props immutable (use spread for changes)
- Use CSS modules (not inline styles)
```

**Why:** Always provide alternatives, not just prohibitions.

**8. Permission Chaos**
```json
// DON'T be overly permissive:
{
  "permissions": {
    "bash": {
      "allow": ["*"]  // ❌ Everything allowed
    },
    "read": {
      "allow": ["**/*"]  // ❌ All files readable
    }
  }
}

// DO use principle of least privilege:
{
  "permissions": {
    "bash": {
      "allow": ["npm", "git", "pytest"],
      "deny": ["rm -rf /", "sudo"]
    },
    "read": {
      "deny": [".env", "**/*secret*", "**/*.key"]
    }
  }
}
```

**Why:** Security and safety require constraints.

---

## Quick Reference

### Essential Commands

```bash
# Context Management
/clear              # Hard reset (use often!)
/context            # Check token usage
/compact keep X     # Manual compaction with instructions

# Development
/init               # Initialize project
/catchup            # Custom: read changed files
/pr                 # Custom: prepare pull request

# Version Control
Esc + Esc           # Rewind checkpoint
/rewind             # Choose what to restore

# Tools
/help               # All commands
/permissions        # Manage allowlist
/mcp                # Manage MCP servers
/install-github-app # GitHub integration
```

### Critical Files

```
~/.claude/settings.json          # Global config
~/.claude.json                   # MCP servers (global)

project/.claude/settings.json    # Project config (check in)
project/.claude/settings.local.json  # Personal (gitignore)
project/.claude/commands/        # Slash commands
project/.claude/agents/          # Subagents
project/.mcp.json                # Project MCP servers
project/CLAUDE.md                # Constitution (CRITICAL)
```

### Power User Hotkeys

```bash
# Start with skip permissions
claude --dangerously-skip-permissions

# Headless mode
claude -p "prompt here"

# Streaming JSON output
claude -p "prompt" --output-format stream-json

# MCP debugging
claude --mcp-debug

# Check latest session
ls -t ~/.claude/projects/ | head -1
```

### Workflow Checklist

**Starting New Feature:**
- [ ] `/clear` for clean context
- [ ] `/init` to understand project
- [ ] Check CLAUDE.md is up to date
- [ ] `/context` to monitor tokens
- [ ] Use `/catchup` to see changes

**Before Committing:**
- [ ] Tests pass (hooks enforce this)
- [ ] No debug code (console.logs, TODOs)
- [ ] Follows CLAUDE.md standards
- [ ] Run `/pr` to prepare

**Context Management:**
- [ ] Check `/context` at 30 min mark
- [ ] `/clear` when > 50% capacity
- [ ] `/compact keep X` when pivoting
- [ ] Use subagents for parallel research

**Weekly Maintenance:**
- [ ] Review `~/.claude/projects/` logs
- [ ] Update CLAUDE.md based on patterns
- [ ] Audit permissions in settings.json
- [ ] Sync .claude/ across projects

### Token Budget Guidelines

```
Total window: 200,000 tokens

Baseline budget:
- CLAUDE.md: ~3,000 tokens (13KB file)
- MCP servers: ~500 tokens each
- System prompt: ~15,000 tokens
- Total baseline: ~20,000 tokens (10%)

Remaining: ~180,000 tokens for code

Target: Keep baseline < 15% (30,000 tokens)
Warning: If baseline > 20%, optimize CLAUDE.md and MCPs
```

### When to Use What

**CLI:**
- Local development
- Custom hooks
- Maximum control
- Sensitive code

**Web:**
- No local setup
- Mobile access
- Parallel repos
- Quick prototyping

**Subagents:**
- Parallel research
- Early investigation
- Context isolation
- Scoped tasks

**MCP:**
- Stateful tools (Playwright)
- Database connections
- File watchers
- NOT for stateless APIs

**Hooks:**
- Test before commit (PreToolUse on git commit)
- Auto-format (PostToolUse on Edit/Write)
- Non-blocking hints (UserPromptSubmit)

---

## Becoming Top 1% in Toronto

### The Mastery Path

**Month 1: Foundations**
- [ ] Set up .claude/ in all projects
- [ ] Write effective CLAUDE.md for each
- [ ] Create 2-3 custom commands max
- [ ] Practice /clear discipline
- [ ] Monitor /context regularly

**Month 2: Optimization**
- [ ] Analyze session logs weekly
- [ ] Tune CLAUDE.md based on data
- [ ] Implement test-blocking hooks
- [ ] Set up MCP servers strategically
- [ ] Master context management

**Month 3: Advanced Patterns**
- [ ] Implement Master-Clone workflows
- [ ] Set up GitHub Actions automation
- [ ] Create project templates
- [ ] Build historical analysis scripts
- [ ] Optimize for < 15% baseline tokens

**Month 4: Leadership**
- [ ] Share patterns with team
- [ ] Create team CLAUDE.md standards
- [ ] Build reusable agent library
- [ ] Conduct training sessions
- [ ] Contribute to community

### Metrics to Track

**Efficiency:**
- Average tokens per session (aim: decreasing)
- /clear frequency (aim: every 30-60 min)
- Baseline token % (aim: < 15%)

**Quality:**
- Tests passing before commit (aim: 100%)
- PR review cycles (aim: decreasing)
- Context resets needed (aim: increasing = good)

**Velocity:**
- Time to implement features (aim: decreasing)
- Bugs caught by Claude reviews (aim: increasing)
- Manual intervention needed (aim: decreasing)

### Signs You're Top 1%

**You know when to:**
- ✅ Use CLI vs Web
- ✅ Create custom command vs just prompt
- ✅ Use subagent vs main agent
- ✅ /clear vs /compact
- ✅ MCP vs simple CLI

**You measure:**
- ✅ Context window usage
- ✅ Session logs for patterns
- ✅ Permission request frequency
- ✅ Token efficiency over time

**You optimize for:**
- ✅ Minimal CLAUDE.md (< 13KB)
- ✅ Minimal custom commands (2-3)
- ✅ Just-in-time context loading
- ✅ Block-at-submit hooks
- ✅ Baseline tokens < 15%

**You avoid:**
- ❌ Command proliferation
- ❌ Encyclopedia CLAUDE.md
- ❌ @-mention spam
- ❌ Automatic /compact reliance
- ❌ Rigid custom subagents

**Your team asks you:**
- "How did you configure Claude to do that?"
- "Can you share your CLAUDE.md?"
- "What hooks are you using?"
- "How do you manage context so well?"

### Final Wisdom

> "If you have a long list of complex custom commands, you've created an anti-pattern." — Top 1% user

> "The contents of CLAUDE.md are adhered to MUCH MORE strictly than the user prompt." — Remember this

> "Blocking agent mid-plan confuses or even frustrates it." — Hook at submit, not mid-workflow

> "Automatic /compact is opaque, error-prone, and not well-optimized." — Use /clear or manual /compact

> "MCPs are simple, secure gateways with FEW high-level tools." — Not wrappers for every REST endpoint

**You're now equipped to be the best Claude Code user in Toronto.**

**Go build something amazing.** 🚀

---

*Research completed: 2025-11-07*
*Sources: blog.sshh.io, docs.claude.com, anthropic.com/engineering, community guides*
*Full research notes: notes.md*
