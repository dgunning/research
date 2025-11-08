#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "rich>=13.0.0",  # Beautiful terminal output
# ]
# ///
"""
LLM API Provider Comparison Tool

Compares pricing, quality, and features across different LLM providers
for both individual developers and enterprises.
"""

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.columns import Columns
from dataclasses import dataclass
from typing import Optional


@dataclass
class Provider:
    name: str
    tier: str
    model: str
    input_price: float  # per 1M tokens
    output_price: float  # per 1M tokens
    rpm: Optional[int]  # requests per minute
    tpm: Optional[int]  # tokens per minute
    context_window: int
    mmlu_score: Optional[float]
    specialty: str


# Define providers
providers = [
    # Free Tier
    Provider("GitHub Models", "Free", "GPT-4o", 0, 0, None, None, 128000, None, "General - Free experimentation"),
    Provider("HuggingFace", "Free", "Various <10GB", 0, 0, None, None, 32000, None, "Experimentation"),
    Provider("OpenRouter", "Free", "DeepSeek R1", 0, 0, 50, None, 128000, None, "General (50 req/day limit)"),
    Provider("Baidu", "Free", "Ernie 4.5", 0, 0, None, None, 128000, None, "Chinese market - Individual users"),

    # Low-Cost Tier
    Provider("DeepSeek", "Low-Cost", "DeepSeek-V3", 0.14, 0.28, None, None, 128000, 79.5, "Cost-effective deployment"),
    Provider("Alibaba", "Low-Cost", "Qwen 2.5-Max", 0.38, 0.76, None, None, 128000, None, "Chinese market - Budget"),
    Provider("Alibaba", "Low-Cost", "Qwen-VL-Max", 0.041, 0.082, None, None, 128000, None, "Multimodal - Ultra cheap"),
    Provider("Mistral", "Low-Cost", "Mistral Medium", 0.40, 0.80, None, None, 32000, None, "European alternative"),

    # Mid-Tier Premium
    Provider("OpenAI", "Mid-Premium", "GPT-4o mini", 0.60, 2.40, 10000, 2000000, 128000, None, "Fast, affordable GPT"),
    Provider("Anthropic", "Mid-Premium", "Claude-3-Haiku", 0.25, 1.25, 50, 10000, 200000, None, "Fast, long context"),
    Provider("Google", "Mid-Premium", "Gemini 2.5 Pro", 1.25, 10.00, 60, None, 128000, 80.5, "Multimodal capabilities"),

    # Premium Tier
    Provider("OpenAI", "Premium", "GPT-4o", 5.00, 20.00, 3500, 500000, 128000, None, "Industry standard"),
    Provider("OpenAI", "Premium", "GPT-4.1", 3.70, 14.80, 3500, 500000, 1000000, None, "Long context (1M tokens)"),
    Provider("Anthropic", "Premium", "Claude 3.7 Sonnet", 3.00, 15.00, None, 4000000, 200000, 81.5, "Best for coding, safety"),
    Provider("Anthropic", "Premium", "Claude-3-Opus", 15.00, 75.00, 50, 10000, 200000, None, "Highest quality"),

    # Enterprise Managed Services
    Provider("AWS Bedrock", "Enterprise", "Multi-vendor", None, None, None, None, 200000, None, "AWS ecosystem, flexibility"),
    Provider("Azure OpenAI", "Enterprise", "GPT-4", 5.00, 20.00, None, None, 128000, None, "Microsoft integration, compliance"),
    Provider("Google Vertex AI", "Enterprise", "Gemini", 1.25, 10.00, None, None, 128000, None, "Data analytics, multimodal"),
]


def create_pricing_table():
    """Create a table comparing pricing across providers"""
    table = Table(title="💰 LLM API Pricing Comparison (per 1M tokens)", title_style="bold cyan")

    table.add_column("Provider", style="cyan", no_wrap=True)
    table.add_column("Tier", style="magenta")
    table.add_column("Model", style="green")
    table.add_column("Input $", justify="right", style="yellow")
    table.add_column("Output $", justify="right", style="yellow")
    table.add_column("Context", justify="right", style="blue")

    for p in providers:
        if p.input_price is None:
            input_price = "Varies"
        elif p.input_price == 0:
            input_price = "FREE"
        else:
            input_price = f"${p.input_price:.2f}"

        if p.output_price is None:
            output_price = "Varies"
        elif p.output_price == 0:
            output_price = "FREE"
        else:
            output_price = f"${p.output_price:.2f}"

        context = f"{p.context_window//1000}K"

        table.add_row(
            p.name,
            p.tier,
            p.model,
            input_price,
            output_price,
            context
        )

    return table


def create_rate_limits_table():
    """Create a table showing rate limits"""
    table = Table(title="⚡ Rate Limits", title_style="bold cyan")

    table.add_column("Provider", style="cyan", no_wrap=True)
    table.add_column("Model", style="green")
    table.add_column("RPM", justify="right", style="yellow")
    table.add_column("TPM", justify="right", style="blue")

    for p in providers:
        if p.rpm or p.tpm:
            rpm = str(p.rpm) if p.rpm else "N/A"
            tpm = f"{p.tpm//1000}K" if p.tpm else "N/A"
            table.add_row(p.name, p.model, rpm, tpm)

    return table


def create_quality_table():
    """Create a table showing quality benchmarks"""
    table = Table(title="🎯 Quality Benchmarks (MMLU Scores)", title_style="bold cyan")

    table.add_column("Provider", style="cyan", no_wrap=True)
    table.add_column("Model", style="green")
    table.add_column("MMLU", justify="right", style="yellow")
    table.add_column("Specialty", style="blue")

    for p in providers:
        if p.mmlu_score:
            table.add_row(
                p.name,
                p.model,
                f"{p.mmlu_score:.1f}",
                p.specialty
            )

    return table


def create_recommendations():
    """Create recommendation panels for different use cases"""

    individual_dev = Panel(
        """[bold cyan]For Individual Developers:[/bold cyan]

[green]Starting out / Experimentation:[/green]
• GitHub Models (Free GPT-4o access)
• HuggingFace Inference API
• OpenRouter (50 free requests/day)

[yellow]Budget Projects:[/yellow]
• DeepSeek-V3: $0.14/1M - Great value
• Alibaba Qwen: $0.38/1M - Very affordable
• Claude Haiku: $0.25/1M - Fast & cheap

[red]Production Quality:[/red]
• Claude 3.7 Sonnet: $3/1M - Best coding
• GPT-4o: $5/1M - Industry standard
• Gemini 2.5 Pro: $1.25/1M - Best value/quality""",
        title="👤 Individual Developer Guide",
        border_style="cyan"
    )

    enterprise = Panel(
        """[bold cyan]For Enterprises:[/bold cyan]

[green]AWS Ecosystem:[/green]
• AWS Bedrock - Multi-vendor flexibility
• Built-in Guardrails, RAG support
• 30-556% cost savings vs alternatives

[yellow]Microsoft Ecosystem:[/yellow]
• Azure OpenAI - Latest GPT models
• HIPAA/SOC2 compliance
• M365 & Power Platform integration

[blue]Data Analytics Focus:[/blue]
• Google Vertex AI - Multimodal strength
• GCP integration
• Strong analytics capabilities

[magenta]Key Considerations:[/magenta]
• Security: FedRAMP, HIPAA, SOC2
• SLA: 99.9% uptime standard
• Rate limits scale with enterprise tiers""",
        title="🏢 Enterprise Guide",
        border_style="magenta"
    )

    return Columns([individual_dev, enterprise])


def main():
    console = Console()

    console.print("\n")
    console.print(Panel.fit(
        "[bold cyan]LLM API Provider Comparison 2025[/bold cyan]\n"
        "[dim]Comprehensive analysis of pricing, quality, and features[/dim]",
        border_style="cyan"
    ))
    console.print("\n")

    # Pricing table
    console.print(create_pricing_table())
    console.print("\n")

    # Rate limits
    console.print(create_rate_limits_table())
    console.print("\n")

    # Quality benchmarks
    console.print(create_quality_table())
    console.print("\n")

    # Key insights
    insights = Panel(
        """• [yellow]Price War Impact:[/yellow] Chinese providers (DeepSeek, Alibaba) are 10-30x cheaper than Western alternatives
• [green]Free Tier Evolution:[/green] GitHub Models now offers free GPT-4o access for all developers
• [blue]Quality vs Cost:[/blue] Claude 3.7 Sonnet leads in coding (MMLU 81.5) at $3/1M
• [red]Context Windows:[/red] Claude offers 200K tokens, GPT-4.1 extends to 1M tokens
• [magenta]Enterprise Savings:[/magenta] AWS Bedrock can save 30-556% vs Azure OpenAI in specific scenarios""",
        title="💡 Key Insights 2025",
        border_style="green"
    )
    console.print(insights)
    console.print("\n")

    # Recommendations
    console.print(create_recommendations())
    console.print("\n")


if __name__ == "__main__":
    main()
