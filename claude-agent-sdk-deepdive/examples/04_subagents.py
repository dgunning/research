#!/usr/bin/env python3
"""
Subagents Example - Claude Agent SDK

This example demonstrates using subagents for parallel processing
and context isolation.

Usage:
    python 04_subagents.py
"""

import anyio
from claude_agent_sdk import ClaudeSDKClient, ClaudeAgentOptions
import asyncio
from typing import List, Dict


async def analyze_file_with_subagent(file_path: str) -> Dict:
    """Use a subagent to analyze a single file."""
    options = ClaudeAgentOptions(
        custom_allowed_tools=["Read", "Grep"],
        system_prompt=f"Analyze {file_path} for code quality issues."
    )

    async with ClaudeSDKClient(options=options) as subagent:
        response = await subagent.send_user_message(
            f"""
            Analyze {file_path} and report:
            1. Number of functions
            2. Number of classes
            3. Any potential issues (long functions, missing docstrings, etc.)
            """
        )

        result = ""
        async for message in response:
            if message.type == "assistant":
                for block in message.content:
                    if isinstance(block, dict) and block.get("type") == "text":
                        result += block["text"]

        return {
            "file": file_path,
            "analysis": result
        }


async def parallel_file_analysis():
    """Analyze multiple files in parallel using subagents."""
    print("=== Parallel File Analysis ===\n")

    # Find Python files
    async with ClaudeSDKClient() as main_agent:
        response = await main_agent.send_user_message(
            "List all Python files in the current directory (just the filenames)"
        )

        files = []
        async for message in response:
            if message.type == "assistant":
                for block in message.content:
                    if isinstance(block, dict) and block.get("type") == "text":
                        # Extract filenames (simplified parsing)
                        text = block["text"]
                        files = [line.strip() for line in text.split("\n") if line.endswith(".py")]

    print(f"Found {len(files)} Python files\n")

    # Analyze files in parallel with subagents
    print("Analyzing files with subagents...")
    results = await asyncio.gather(*[
        analyze_file_with_subagent(file) for file in files[:5]  # Limit to 5 for demo
    ])

    # Display results
    print("\nAnalysis Results:")
    print("=" * 60)
    for result in results:
        print(f"\nFile: {result['file']}")
        print("-" * 60)
        print(result['analysis'])


async def process_data_with_subagents():
    """Process data chunks in parallel."""
    print("\n\n=== Data Processing with Subagents ===\n")

    # Create sample data
    async with ClaudeSDKClient() as main_agent:
        response = await main_agent.send_user_message(
            """
            Create a CSV file called 'sales_data.csv' with sample sales data:
            - Date, Product, Quantity, Price
            - Include 20 rows of sample data
            """
        )

        async for message in response:
            if message.type == "assistant":
                for block in message.content:
                    if isinstance(block, dict) and block.get("type") == "text":
                        print(block["text"])

    # Define subagent tasks
    async def analyze_product(product_name: str) -> Dict:
        """Subagent analyzes a specific product."""
        options = ClaudeAgentOptions(
            custom_allowed_tools=["Read", "Bash"],
            system_prompt=f"Analyze sales data for {product_name}"
        )

        async with ClaudeSDKClient(options=options) as subagent:
            response = await subagent.send_user_message(
                f"""
                Read sales_data.csv and calculate for {product_name}:
                1. Total quantity sold
                2. Total revenue
                3. Average price
                """
            )

            result = ""
            async for message in response:
                if message.type == "assistant":
                    for block in message.content:
                        if isinstance(block, dict) and block.get("type") == "text":
                            result += block["text"]

            return {
                "product": product_name,
                "analysis": result
            }

    # Process products in parallel
    products = ["Product A", "Product B", "Product C"]
    print("\nAnalyzing products in parallel...")

    results = await asyncio.gather(*[
        analyze_product(product) for product in products
    ])

    print("\nProduct Analysis:")
    print("=" * 60)
    for result in results:
        print(f"\n{result['product']}:")
        print("-" * 60)
        print(result['analysis'])


async def hierarchical_subagents():
    """Demonstrate hierarchical agent structure."""
    print("\n\n=== Hierarchical Subagents ===\n")

    async def research_subagent(topic: str) -> str:
        """Subagent that researches a topic."""
        options = ClaudeAgentOptions(
            custom_allowed_tools=["WebSearch", "WebFetch"],
            system_prompt=f"Research information about {topic}"
        )

        async with ClaudeSDKClient(options=options) as subagent:
            response = await subagent.send_user_message(
                f"Find and summarize key information about {topic}"
            )

            result = ""
            async for message in response:
                if message.type == "assistant":
                    for block in message.content:
                        if isinstance(block, dict) and block.get("type") == "text":
                            result += block["text"]

            return result

    async def writing_subagent(topic: str, research: str) -> str:
        """Subagent that writes content based on research."""
        options = ClaudeAgentOptions(
            custom_allowed_tools=["Write"],
            system_prompt="Write a blog post based on research"
        )

        async with ClaudeSDKClient(options=options) as subagent:
            response = await subagent.send_user_message(
                f"""
                Using this research about {topic}:

                {research}

                Write a blog post (save as {topic.lower().replace(' ', '_')}_post.md)
                """
            )

            result = ""
            async for message in response:
                if message.type == "assistant":
                    for block in message.content:
                        if isinstance(block, dict) and block.get("type") == "text":
                            result += block["text"]

            return result

    # Main agent coordinates subagents
    async with ClaudeSDKClient() as main_agent:
        print("Main agent: Creating blog post about Claude Agent SDK...")

        # Subagent 1: Research
        print("\nSubagent 1: Researching...")
        research = await research_subagent("Claude Agent SDK")

        print("Research completed!")

        # Subagent 2: Write
        print("\nSubagent 2: Writing blog post...")
        result = await writing_subagent("Claude Agent SDK", research)

        print("Blog post completed!")
        print("\nMain agent result:")
        print(result)


async def load_balanced_subagents():
    """Distribute work across subagents with load balancing."""
    print("\n\n=== Load-Balanced Subagents ===\n")

    async def process_chunk(chunk_id: int, data: List[str]) -> Dict:
        """Process a data chunk with a subagent."""
        options = ClaudeAgentOptions(
            custom_allowed_tools=["Bash"],
            system_prompt=f"Process data chunk {chunk_id}"
        )

        async with ClaudeSDKClient(options=options) as subagent:
            response = await subagent.send_user_message(
                f"Process these items: {', '.join(data)}"
            )

            result = ""
            async for message in response:
                if message.type == "assistant":
                    for block in message.content:
                        if isinstance(block, dict) and block.get("type") == "text":
                            result += block["text"]

            return {
                "chunk_id": chunk_id,
                "count": len(data),
                "result": result
            }

    # Divide work into chunks
    all_data = [f"Item {i}" for i in range(1, 21)]
    chunk_size = 5
    chunks = [all_data[i:i + chunk_size] for i in range(0, len(all_data), chunk_size)]

    print(f"Processing {len(all_data)} items in {len(chunks)} chunks...\n")

    # Process chunks in parallel
    results = await asyncio.gather(*[
        process_chunk(i, chunk) for i, chunk in enumerate(chunks)
    ])

    # Aggregate results
    print("Results:")
    print("=" * 60)
    for result in results:
        print(f"Chunk {result['chunk_id']}: Processed {result['count']} items")


async def main():
    """Run all examples."""
    try:
        await parallel_file_analysis()
        await process_data_with_subagents()
        await hierarchical_subagents()
        await load_balanced_subagents()

    except Exception as e:
        print(f"\nError: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    print("Claude Agent SDK - Subagents Examples\n")
    anyio.run(main)
