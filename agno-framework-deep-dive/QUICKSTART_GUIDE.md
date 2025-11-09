# Agno Framework: Developer Quick-Start Guide

**For: Company Developers**
**Purpose: Get productive with Agno in 30 minutes**
**Last Updated: November 2025**

---

## Why Agno?

As your Head of AI, I've selected Agno for our AI agent development because it provides:

- **Speed**: 529× faster than alternatives, production-ready performance
- **Privacy**: All data stays in our infrastructure (compliance-ready)
- **Simplicity**: Pure Python, no complex abstractions
- **Production-Ready**: Built-in runtime (AgentOS) for immediate deployment
- **Cost-Effective**: Open source, zero vendor fees

---

## Table of Contents

1. [15-Minute Setup](#15-minute-setup)
2. [Your First Agent (5 minutes)](#your-first-agent-5-minutes)
3. [Essential Patterns](#essential-patterns)
4. [Common Use Cases](#common-use-cases)
5. [Production Checklist](#production-checklist)
6. [Best Practices](#best-practices)
7. [Troubleshooting](#troubleshooting)
8. [Next Steps](#next-steps)

---

## 15-Minute Setup

### Step 1: Install Agno (2 minutes)

```bash
# Basic installation
pip install agno

# With specific integrations (recommended)
pip install agno[openai,anthropic,postgres,pgvector]

# Or install everything
pip install agno[all]
```

### Step 2: Set Up API Keys (3 minutes)

Create a `.env` file in your project root:

```bash
# .env file
OPENAI_API_KEY=sk-proj-xxx
ANTHROPIC_API_KEY=sk-ant-xxx

# Database (for production)
DATABASE_URL=postgresql://user:pass@localhost:5432/agno_db

# Optional: Disable telemetry
AGNO_TELEMETRY=false
```

**Load environment variables:**

```python
# At the top of your main file
from dotenv import load_dotenv
import os

load_dotenv()
```

### Step 3: Verify Installation (2 minutes)

```python
# test_agno.py
from agno.agent import Agent
from agno.models.openai import OpenAIChat
import os

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    description="You are a helpful assistant",
)

response = agent.run("Say 'Agno is working!'")
print(response.content)
```

Run it:
```bash
python test_agno.py
```

✅ If you see "Agno is working!" - you're ready to go!

---

## Your First Agent (5 minutes)

### Pattern 1: Simple Q&A Agent

```python
# agents/qa_agent.py
from agno.agent import Agent
from agno.models.openai import OpenAIChat
import os

def create_qa_agent():
    return Agent(
        name="QA Agent",
        model=OpenAIChat(
            id="gpt-4o",
            api_key=os.getenv("OPENAI_API_KEY")
        ),
        description="You are a helpful assistant",
        markdown=True,  # Enable formatted output
    )

if __name__ == "__main__":
    agent = create_qa_agent()
    agent.print_response("What is Agno?", stream=True)
```

### Pattern 2: Agent with Web Search

```python
# agents/research_agent.py
from agno.agent import Agent
from agno.models.anthropic import Claude
from agno.tools.duckduckgo import DuckDuckGoTools
import os

def create_research_agent():
    return Agent(
        name="Research Agent",
        model=Claude(
            id="claude-sonnet-4-5",
            api_key=os.getenv("ANTHROPIC_API_KEY")
        ),
        tools=[DuckDuckGoTools()],
        description="You are a research specialist",
        show_tool_calls=True,  # Show which tools are being used
        markdown=True,
    )

if __name__ == "__main__":
    agent = create_research_agent()
    agent.print_response(
        "What are the latest developments in quantum computing?",
        stream=True
    )
```

### Pattern 3: Agent with Memory (Conversational)

```python
# agents/conversational_agent.py
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.db.sqlite import SqliteDb
import os

def create_conversational_agent(session_id: str):
    return Agent(
        name="Conversational Agent",
        model=OpenAIChat(id="gpt-4o"),
        db=SqliteDb(db_file="agent_memory.db"),  # Persistent memory
        session_id=session_id,  # Unique per user/conversation
        add_history_to_context=True,  # Remember conversation
        num_history_messages=10,  # Last 10 messages
        markdown=True,
    )

if __name__ == "__main__":
    agent = create_conversational_agent(session_id="user_123")

    # First interaction
    agent.print_response("My name is Alice and I work in engineering", stream=True)

    # Second interaction - agent remembers
    agent.print_response("What's my name and department?", stream=True)
```

---

## Essential Patterns

### Pattern 4: RAG Agent (Knowledge Base)

**Use Case:** Answer questions from company documents

```python
# agents/knowledge_agent.py
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.knowledge.pgvector import PgVectorKnowledgeBase
from agno.vectordb.pgvector import PgVector
from agno.embedder.openai import OpenAIEmbedder
import os

def create_knowledge_agent():
    # Setup vector database
    vector_db = PgVector(
        host=os.getenv("DB_HOST", "localhost"),
        port=int(os.getenv("DB_PORT", "5432")),
        database=os.getenv("DB_NAME", "knowledge_db"),
        collection="company_docs",
        embedder=OpenAIEmbedder(model="text-embedding-3-small"),
    )

    # Create knowledge base
    knowledge = PgVectorKnowledgeBase(
        vector_db=vector_db,
        num_documents=3,  # Top-3 retrieval
    )

    return Agent(
        name="Knowledge Agent",
        model=OpenAIChat(id="gpt-4o"),
        knowledge=knowledge,
        search_knowledge=True,  # Auto-search before answering
        instructions=[
            "You are a company knowledge base assistant",
            "Always search the knowledge base before answering",
            "If information is not found, say so clearly",
            "Cite your sources when possible",
        ],
        markdown=True,
    )

def load_documents(agent):
    """Load documents into knowledge base"""
    agent.knowledge.load_documents([
        "docs/employee_handbook.pdf",
        "docs/engineering_guide.md",
        "docs/api_documentation.md",
    ])

if __name__ == "__main__":
    agent = create_knowledge_agent()
    # load_documents(agent)  # Run once to load docs
    agent.print_response("What is our vacation policy?", stream=True)
```

### Pattern 5: Specialized Tool Agent

**Use Case:** Financial analysis, data processing, etc.

```python
# agents/finance_agent.py
from agno.agent import Agent
from agno.models.anthropic import Claude
from agno.tools.yfinance import YFinanceTools
from agno.tools.reasoning import ReasoningTools
import os

def create_finance_agent():
    return Agent(
        name="Finance Analyst",
        model=Claude(id="claude-sonnet-4-5"),
        tools=[
            YFinanceTools(
                stock_price=True,
                analyst_recommendations=True,
                company_info=True,
                company_news=True,
            ),
            ReasoningTools(add_instructions=True),  # Enable reasoning
        ],
        instructions=[
            "You are a financial analyst",
            "Provide data-driven insights",
            "Use tables for financial data",
            "Always show your reasoning",
        ],
        markdown=True,
        show_tool_calls=True,
    )

if __name__ == "__main__":
    agent = create_finance_agent()
    agent.print_response(
        "Analyze AAPL stock and provide a recommendation",
        stream=True
    )
```

### Pattern 6: Multi-Agent Team

**Use Case:** Complex tasks requiring multiple specialists

```python
# agents/editorial_team.py
from agno.agent import Agent
from agno.team import Team
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
import os

def create_editorial_team():
    # Define team members
    researcher = Agent(
        name="Researcher",
        role="Research information on the web",
        model=OpenAIChat(id="gpt-4o"),
        tools=[DuckDuckGoTools()],
    )

    writer = Agent(
        name="Writer",
        role="Write engaging content based on research",
        model=OpenAIChat(id="gpt-4o"),
        instructions=[
            "Write in a clear, professional tone",
            "Use the research provided by the Researcher",
            "Structure content with headers and bullet points",
        ],
    )

    editor = Agent(
        name="Editor",
        role="Review and refine content for quality",
        model=OpenAIChat(id="gpt-4o"),
        instructions=[
            "Check for clarity and accuracy",
            "Ensure professional tone",
            "Fix any grammar or style issues",
        ],
    )

    # Create coordinated team
    return Team(
        name="Editorial Team",
        mode="coordinate",  # Leader delegates tasks
        members=[researcher, writer, editor],
        instructions="""
        1. Researcher: Gather information on the topic
        2. Writer: Create a draft based on research
        3. Editor: Review and finalize the content
        """,
        markdown=True,
    )

if __name__ == "__main__":
    team = create_editorial_team()
    team.print_response(
        "Write a 500-word blog post about AI in healthcare",
        stream=True
    )
```

### Pattern 7: Production Agent with Full Config

**Use Case:** Production-ready agent with all features

```python
# agents/production_agent.py
from agno.agent import Agent
from agno.models.anthropic import Claude
from agno.db.postgres import PostgresDb
from agno.knowledge.pgvector import PgVectorKnowledgeBase
from agno.vectordb.pgvector import PgVector
from agno.tools.yfinance import YFinanceTools
import os

def create_production_agent(session_id: str):
    return Agent(
        # Identity
        name="Production Agent",
        description="Production-grade agent with full capabilities",

        # Model
        model=Claude(
            id="claude-sonnet-4-5",
            api_key=os.getenv("ANTHROPIC_API_KEY"),
        ),

        # Memory (PostgreSQL for production)
        db=PostgresDb(
            host=os.getenv("DB_HOST"),
            port=int(os.getenv("DB_PORT", "5432")),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
        ),
        session_id=session_id,
        add_history_to_context=True,
        num_history_messages=10,

        # Knowledge base (optional)
        # knowledge=knowledge_base,
        # search_knowledge=True,

        # Tools
        tools=[
            YFinanceTools(stock_price=True),
            # Add more tools as needed
        ],

        # Behavior
        instructions=[
            "You are a helpful AI assistant",
            "Provide accurate, data-driven responses",
            "Always explain your reasoning",
        ],

        # Output
        markdown=True,
        show_tool_calls=True,

        # Advanced (optional)
        # reasoning=True,
        # require_confirmation=["dangerous_operation"],
    )
```

---

## Common Use Cases

### Use Case 1: Customer Support Bot

```python
# use_cases/support_bot.py
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.db.postgres import PostgresDb
from agno.knowledge.pgvector import PgVectorKnowledgeBase
from agno.vectordb.pgvector import PgVector

def create_support_bot(user_id: str):
    # Setup knowledge base with support docs
    vector_db = PgVector(
        host="localhost",
        database="support_kb",
        collection="support_docs",
    )

    knowledge = PgVectorKnowledgeBase(
        vector_db=vector_db,
        num_documents=5,
    )

    return Agent(
        name="Support Bot",
        model=OpenAIChat(id="gpt-4o"),
        db=PostgresDb(database="support_db"),
        session_id=f"support_{user_id}",
        knowledge=knowledge,
        search_knowledge=True,
        add_history_to_context=True,
        instructions=[
            "You are a friendly customer support agent",
            "Search the knowledge base for answers",
            "If you can't help, offer to escalate to human support",
            "Be empathetic and professional",
        ],
        markdown=True,
    )
```

### Use Case 2: Data Analysis Agent

```python
# use_cases/data_analyst.py
from agno.agent import Agent
from agno.models.anthropic import Claude
from agno.tools.python import PythonTools
import os

def create_data_analyst():
    return Agent(
        name="Data Analyst",
        model=Claude(id="claude-sonnet-4-5"),
        tools=[
            PythonTools(),  # Can execute Python code
        ],
        instructions=[
            "You are a data analyst",
            "Write Python code to analyze data",
            "Use pandas, numpy for analysis",
            "Create visualizations with matplotlib",
            "Explain your findings clearly",
        ],
        markdown=True,
        show_tool_calls=True,
    )

# Usage
if __name__ == "__main__":
    agent = create_data_analyst()
    agent.print_response("""
    Analyze this sales data and provide insights:
    Q1: $150K, Q2: $180K, Q3: $165K, Q4: $210K
    """, stream=True)
```

### Use Case 3: Code Review Agent

```python
# use_cases/code_reviewer.py
from agno.agent import Agent
from agno.models.anthropic import Claude

def create_code_reviewer():
    return Agent(
        name="Code Reviewer",
        model=Claude(id="claude-sonnet-4-5"),
        instructions=[
            "You are an expert code reviewer",
            "Review code for:",
            "- Bugs and logic errors",
            "- Security vulnerabilities",
            "- Performance issues",
            "- Code style and best practices",
            "- Documentation quality",
            "Provide constructive feedback",
            "Suggest improvements with examples",
        ],
        markdown=True,
    )

# Usage
if __name__ == "__main__":
    agent = create_code_reviewer()

    code = """
    def process_user_input(user_input):
        query = f"SELECT * FROM users WHERE name = '{user_input}'"
        return db.execute(query)
    """

    agent.print_response(f"Review this code:\n\n```python\n{code}\n```", stream=True)
```

---

## Production Checklist

### Deploying with AgentOS

```python
# main.py - Production deployment
from agno.agent import Agent
from agno.db.postgres import PostgresDb
from agno.os import AgentOS
from agno.models.anthropic import Claude
import os

# Define your agents
agent1 = Agent(
    name="Agent 1",
    model=Claude(id="claude-sonnet-4-5"),
    db=PostgresDb(database="production_db"),
)

agent2 = Agent(
    name="Agent 2",
    model=Claude(id="claude-sonnet-4-5"),
    db=PostgresDb(database="production_db"),
)

# Create AgentOS
agent_os = AgentOS(
    agents=[agent1, agent2],
    db=PostgresDb(database="production_db"),
)

# Get FastAPI app
app = agent_os.get_app()

if __name__ == "__main__":
    # Production: reload=False
    # Development: reload=True
    agent_os.serve(
        app="main:app",
        host="0.0.0.0",
        port=8000,
        reload=False,
    )
```

### Docker Deployment

```dockerfile
# Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# Expose port
EXPOSE 8000

# Run application
CMD ["python", "main.py"]
```

```yaml
# docker-compose.yml
version: '3.8'

services:
  agno-api:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://user:pass@postgres:5432/agno_db
      - ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}
      - OPENAI_API_KEY=${OPENAI_API_KEY}
    depends_on:
      - postgres
    restart: unless-stopped

  postgres:
    image: postgres:15
    environment:
      - POSTGRES_DB=agno_db
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=pass
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

volumes:
  postgres_data:
```

### Pre-Production Checklist

- [ ] **Environment Variables**: All secrets in environment, not hardcoded
- [ ] **Database**: PostgreSQL configured for production
- [ ] **Error Handling**: Try/except blocks around agent calls
- [ ] **Logging**: Structured logging enabled
- [ ] **Monitoring**: Health check endpoints configured
- [ ] **Rate Limiting**: Implement if exposing public API
- [ ] **Authentication**: Add auth middleware if needed
- [ ] **Testing**: Unit tests for agent functions
- [ ] **Documentation**: API documentation generated
- [ ] **Backup**: Database backup strategy in place

---

## Best Practices

### 1. Always Use Environment Variables

```python
# ❌ Bad
model=OpenAIChat(id="gpt-4o", api_key="sk-xxx")

# ✅ Good
import os
model=OpenAIChat(id="gpt-4o", api_key=os.getenv("OPENAI_API_KEY"))
```

### 2. Use Sessions for User Isolation

```python
# ❌ Bad - All users share memory
agent = Agent(model=model, db=db)

# ✅ Good - Each user gets isolated session
agent = Agent(model=model, db=db, session_id=f"user_{user_id}")
```

### 3. Implement Error Handling

```python
# ❌ Bad - No error handling
response = agent.run(user_query)

# ✅ Good - Graceful error handling
try:
    response = agent.run(user_query)
except Exception as e:
    logger.error(f"Agent error: {e}")
    response = "I encountered an error. Please try again."
```

### 4. Use Structured Instructions

```python
# ❌ Bad - Vague instructions
instructions=["Be helpful"]

# ✅ Good - Clear, specific instructions
instructions=[
    "You are a financial analyst",
    "Always provide data sources",
    "Use tables for numerical data",
    "Include confidence levels in recommendations",
    "If you don't know, say so clearly",
]
```

### 5. Optimize Model Selection

```python
# For simple tasks
model=OpenAIChat(id="gpt-4o-mini")  # Faster, cheaper

# For complex reasoning
model=Claude(id="claude-sonnet-4-5")  # More capable

# For production balance
model=OpenAIChat(id="gpt-4o")  # Good balance
```

### 6. Use show_tool_calls for Development

```python
# Development
agent = Agent(
    model=model,
    tools=[...],
    show_tool_calls=True,  # See what tools are being called
    markdown=True,
)

# Production
agent = Agent(
    model=model,
    tools=[...],
    show_tool_calls=False,  # Cleaner output for users
    markdown=True,
)
```

### 7. Structure Your Project

```
project/
├── agents/
│   ├── __init__.py
│   ├── base.py          # Base agent configurations
│   ├── support.py       # Support agent
│   ├── analyst.py       # Data analyst agent
│   └── research.py      # Research agent
├── tools/
│   ├── __init__.py
│   └── custom_tools.py  # Your custom tools
├── config/
│   ├── __init__.py
│   ├── settings.py      # Configuration
│   └── prompts.py       # Prompt templates
├── tests/
│   └── test_agents.py
├── main.py              # AgentOS server
├── requirements.txt
├── .env
└── README.md
```

### 8. Create Agent Factory Pattern

```python
# agents/factory.py
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.models.anthropic import Claude
from agno.db.postgres import PostgresDb
import os

class AgentFactory:
    @staticmethod
    def get_db():
        """Shared database configuration"""
        return PostgresDb(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
        )

    @staticmethod
    def create_support_agent(session_id: str):
        return Agent(
            name="Support Agent",
            model=OpenAIChat(id="gpt-4o"),
            db=AgentFactory.get_db(),
            session_id=session_id,
            # ... other config
        )

    @staticmethod
    def create_analyst_agent(session_id: str):
        return Agent(
            name="Analyst Agent",
            model=Claude(id="claude-sonnet-4-5"),
            db=AgentFactory.get_db(),
            session_id=session_id,
            # ... other config
        )

# Usage
from agents.factory import AgentFactory

agent = AgentFactory.create_support_agent(session_id="user_123")
```

---

## Troubleshooting

### Issue 1: "API key not found"

**Problem:** Agent can't find API key

**Solution:**
```python
# Check environment variable is loaded
import os
print(os.getenv("OPENAI_API_KEY"))  # Should print your key

# If None, ensure .env file is loaded
from dotenv import load_dotenv
load_dotenv()
```

### Issue 2: "Database connection failed"

**Problem:** Can't connect to PostgreSQL

**Solution:**
```bash
# Check PostgreSQL is running
docker ps | grep postgres

# Start PostgreSQL with Docker
docker run -d \
  --name postgres \
  -e POSTGRES_PASSWORD=password \
  -e POSTGRES_DB=agno_db \
  -p 5432:5432 \
  postgres:15

# Test connection
psql -h localhost -U postgres -d agno_db
```

### Issue 3: "Agent not remembering conversation"

**Problem:** Memory not persisting

**Solution:**
```python
# Ensure these are set
agent = Agent(
    model=model,
    db=db,  # ✅ Database configured
    session_id="unique_id",  # ✅ Session ID set
    add_history_to_context=True,  # ✅ History enabled
)
```

### Issue 4: "Import errors"

**Problem:** Can't import agno modules

**Solution:**
```bash
# Reinstall with specific integrations
pip uninstall agno
pip install agno[openai,anthropic,postgres]

# Or install all integrations
pip install agno[all]
```

### Issue 5: "Slow agent responses"

**Problem:** Agent takes too long to respond

**Solution:**
```python
# 1. Use faster models for simple tasks
model=OpenAIChat(id="gpt-4o-mini")  # Instead of gpt-4o

# 2. Reduce history context
num_history_messages=5  # Instead of 10

# 3. Limit knowledge retrieval
knowledge=PgVectorKnowledgeBase(
    vector_db=vector_db,
    num_documents=3,  # Instead of 5
)

# 4. Use streaming for better UX
agent.print_response(query, stream=True)  # Shows progressive output
```

---

## Next Steps

### Week 1: Learn the Basics
1. ✅ Complete this quick-start guide
2. Build a simple Q&A agent
3. Add tools (web search)
4. Implement memory (conversations)

### Week 2: Advanced Features
1. Build a RAG agent with knowledge base
2. Create a multi-agent team
3. Experiment with different models
4. Create custom tools

### Week 3: Production
1. Deploy with AgentOS
2. Add PostgreSQL database
3. Implement error handling
4. Add monitoring

### Week 4: Optimization
1. Performance tuning
2. Cost optimization (model selection)
3. Add caching strategies
4. Implement rate limiting

---

## Additional Resources

### Official Documentation
- **Main Docs**: https://docs.agno.com
- **Examples**: https://docs.agno.com/examples
- **API Reference**: https://docs.agno.com/api

### Company Resources
- **Internal Slack**: #ai-development
- **Code Examples**: `/company/ai/examples/`
- **Team Wiki**: [Company Wiki - AI Development]

### Community
- **Discord**: https://discord.gg/4MtYHHrgA8
- **GitHub**: https://github.com/agno-agi/agno
- **Community Forum**: https://community.agno.com

### Getting Help

1. **Check this guide first**
2. **Search the documentation**: docs.agno.com
3. **Ask in Slack**: #ai-development
4. **Review examples**: GitHub cookbook
5. **Reach out to me**: [Your contact info]

---

## Key Takeaways

✅ **Installation**: `pip install agno[openai,anthropic,postgres]`
✅ **Basic Pattern**: Agent + Model + Tools + Instructions
✅ **Memory**: Use db + session_id for conversations
✅ **Knowledge**: RAG with PgVectorKnowledgeBase
✅ **Production**: AgentOS + PostgreSQL + Docker
✅ **Best Practice**: Environment variables, error handling, structured instructions

**Remember:** Start simple, iterate quickly, and always test with real use cases.

---

**Questions?** Reach out to me directly or post in #ai-development

**Happy Building! 🚀**
