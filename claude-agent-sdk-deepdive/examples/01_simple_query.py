#!/usr/bin/env python3
"""
Simple Query Example - Claude Agent SDK

This example demonstrates the simplest way to use the Claude Agent SDK:
the query() function for one-off questions or tasks.

Usage:
    python 01_simple_query.py
"""

import anyio
from claude_agent_sdk import query


async def simple_query_example():
    """Ask the agent a simple question."""
    print("=== Simple Query Example ===\n")

    prompt = "What files are in the current directory? List them with their sizes."

    print(f"Query: {prompt}\n")
    print("Response:")
    print("-" * 60)

    # The query() function returns an AsyncIterator that yields messages
    async for message in query(prompt=prompt):
        print(message)

    print("-" * 60)


async def code_analysis_example():
    """Ask the agent to analyze code."""
    print("\n=== Code Analysis Example ===\n")

    prompt = """
    Find all Python files in the current directory and analyze them for:
    1. Total lines of code
    2. Number of functions
    3. Number of classes
    Provide a summary.
    """

    print(f"Query: {prompt}\n")
    print("Response:")
    print("-" * 60)

    async for message in query(prompt=prompt):
        print(message)

    print("-" * 60)


async def data_processing_example():
    """Ask the agent to process data."""
    print("\n=== Data Processing Example ===\n")

    prompt = """
    Create a CSV file called 'data.csv' with sample data:
    - Name, Age, City
    - Include 5 rows of sample data
    Then read it back and calculate the average age.
    """

    print(f"Query: {prompt}\n")
    print("Response:")
    print("-" * 60)

    async for message in query(prompt=prompt):
        print(message)

    print("-" * 60)


async def main():
    """Run all examples."""
    try:
        # Example 1: Simple query
        await simple_query_example()

        # Example 2: Code analysis
        await code_analysis_example()

        # Example 3: Data processing
        await data_processing_example()

    except Exception as e:
        print(f"\nError: {e}")


if __name__ == "__main__":
    print("Claude Agent SDK - Simple Query Examples\n")
    anyio.run(main)
