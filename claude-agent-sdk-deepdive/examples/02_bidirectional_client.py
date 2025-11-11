#!/usr/bin/env python3
"""
Bidirectional Client Example - Claude Agent SDK

This example demonstrates using ClaudeSDKClient for interactive
conversations with full control over the message flow.

Usage:
    python 02_bidirectional_client.py
"""

import anyio
from claude_agent_sdk import ClaudeSDKClient, ClaudeAgentOptions


async def basic_conversation():
    """Basic back-and-forth conversation with the agent."""
    print("=== Basic Conversation ===\n")

    async with ClaudeSDKClient() as client:
        # Send first message
        print("User: Can you list the files in the current directory?")
        response = await client.send_user_message(
            "Can you list the files in the current directory?"
        )

        # Process response
        async for message in response:
            if message.type == "assistant":
                print(f"Assistant: {message.content}")

        # Continue conversation
        print("\nUser: How many Python files are there?")
        response = await client.send_user_message(
            "How many Python files are there?"
        )

        async for message in response:
            if message.type == "assistant":
                print(f"Assistant: {message.content}")


async def multi_turn_task():
    """Multi-turn task with iterative refinement."""
    print("\n=== Multi-Turn Task ===\n")

    async with ClaudeSDKClient() as client:
        # Initial request
        print("User: Create a simple Python function to calculate fibonacci numbers.")
        response = await client.send_user_message(
            "Create a simple Python function to calculate fibonacci numbers."
        )

        async for message in response:
            if message.type == "assistant":
                print(f"Assistant: {message.content}")

        # Refinement
        print("\nUser: Now add type hints and docstrings.")
        response = await client.send_user_message(
            "Now add type hints and docstrings."
        )

        async for message in response:
            if message.type == "assistant":
                print(f"Assistant: {message.content}")

        # Testing
        print("\nUser: Add unit tests for the function.")
        response = await client.send_user_message(
            "Add unit tests for the function."
        )

        async for message in response:
            if message.type == "assistant":
                print(f"Assistant: {message.content}")


async def constrained_agent():
    """Agent with specific tool restrictions."""
    print("\n=== Constrained Agent ===\n")

    # Create options that restrict tools
    options = ClaudeAgentOptions(
        custom_allowed_tools=["Read", "Glob", "Grep"],  # Only search tools
        system_prompt="You are a code search assistant. You can only read and search files, not modify them."
    )

    async with ClaudeSDKClient(options=options) as client:
        print("User: Find all functions named 'main' in Python files.")
        response = await client.send_user_message(
            "Find all functions named 'main' in Python files."
        )

        async for message in response:
            if message.type == "assistant":
                print(f"Assistant: {message.content}")


async def working_directory_agent():
    """Agent operating in a specific directory."""
    print("\n=== Working Directory Agent ===\n")

    # Set working directory
    options = ClaudeAgentOptions(
        working_directory="/tmp/agent_workspace"
    )

    async with ClaudeSDKClient(options=options) as client:
        print("User: Create a project structure for a Python web app.")
        response = await client.send_user_message(
            """
            Create a basic project structure for a Python web app:
            - src/ directory for source code
            - tests/ directory for tests
            - requirements.txt
            - README.md
            """
        )

        async for message in response:
            if message.type == "assistant":
                print(f"Assistant: {message.content}")


async def message_inspection():
    """Inspect detailed message structure."""
    print("\n=== Message Inspection ===\n")

    async with ClaudeSDKClient() as client:
        response = await client.send_user_message(
            "What is 2 + 2?"
        )

        async for message in response:
            print(f"Message Type: {message.type}")
            print(f"Message Content: {message.content}")

            if message.type == "assistant":
                # Inspect content blocks
                for block in message.content:
                    if block.get("type") == "text":
                        print(f"  Text: {block['text']}")
                    elif block.get("type") == "tool_use":
                        print(f"  Tool: {block['tool']}")
                        print(f"  Input: {block['input']}")

            print()


async def main():
    """Run all examples."""
    try:
        await basic_conversation()
        await multi_turn_task()
        await constrained_agent()
        await working_directory_agent()
        await message_inspection()

    except Exception as e:
        print(f"\nError: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    print("Claude Agent SDK - Bidirectional Client Examples\n")
    anyio.run(main)
