#!/usr/bin/env python3
"""
Custom Tools Example - Claude Agent SDK

This example demonstrates how to create and use custom tools
via in-process MCP servers.

Usage:
    python 03_custom_tools.py
"""

import anyio
from claude_agent_sdk import (
    ClaudeSDKClient,
    ClaudeAgentOptions,
    tool,
    create_sdk_mcp_server
)
from datetime import datetime
import json


# Define custom tools using the @tool decorator

@tool(
    name="get_current_time",
    description="Get the current time and date",
    input_schema={}
)
async def get_current_time(args: dict):
    """Return the current time and date."""
    now = datetime.now()
    return {
        "content": [{
            "type": "text",
            "text": f"Current time: {now.strftime('%Y-%m-%d %H:%M:%S')}"
        }]
    }


@tool(
    name="calculate",
    description="Perform mathematical calculations",
    input_schema={
        "operation": str,  # +, -, *, /
        "a": float,
        "b": float
    }
)
async def calculate(args: dict):
    """Perform a mathematical operation."""
    operation = args["operation"]
    a = args["a"]
    b = args["b"]

    operations = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y if y != 0 else None
    }

    if operation not in operations:
        return {
            "content": [{
                "type": "text",
                "text": f"Error: Unknown operation '{operation}'"
            }]
        }

    result = operations[operation](a, b)

    if result is None:
        return {
            "content": [{
                "type": "text",
                "text": "Error: Division by zero"
            }]
        }

    return {
        "content": [{
            "type": "text",
            "text": f"{a} {operation} {b} = {result}"
        }]
    }


@tool(
    name="store_note",
    description="Store a note with a title and content",
    input_schema={
        "title": str,
        "content": str
    }
)
async def store_note(args: dict):
    """Store a note to a JSON file."""
    title = args["title"]
    content = args["content"]

    # Read existing notes
    try:
        with open("notes.json", "r") as f:
            notes = json.load(f)
    except FileNotFoundError:
        notes = []

    # Add new note
    note = {
        "title": title,
        "content": content,
        "timestamp": datetime.now().isoformat()
    }
    notes.append(note)

    # Save notes
    with open("notes.json", "w") as f:
        json.dump(notes, f, indent=2)

    return {
        "content": [{
            "type": "text",
            "text": f"Note '{title}' saved successfully!"
        }]
    }


@tool(
    name="list_notes",
    description="List all stored notes",
    input_schema={}
)
async def list_notes(args: dict):
    """List all stored notes."""
    try:
        with open("notes.json", "r") as f:
            notes = json.load(f)
    except FileNotFoundError:
        return {
            "content": [{
                "type": "text",
                "text": "No notes found."
            }]
        }

    if not notes:
        return {
            "content": [{
                "type": "text",
                "text": "No notes found."
            }]
        }

    # Format notes
    formatted = "Stored Notes:\n\n"
    for i, note in enumerate(notes, 1):
        formatted += f"{i}. {note['title']}\n"
        formatted += f"   {note['content']}\n"
        formatted += f"   ({note['timestamp']})\n\n"

    return {
        "content": [{
            "type": "text",
            "text": formatted
        }]
    }


async def basic_custom_tools():
    """Use basic custom tools."""
    print("=== Basic Custom Tools ===\n")

    # Create MCP server with custom tools
    server = create_sdk_mcp_server(
        name="utility-tools",
        version="1.0.0",
        tools=[get_current_time, calculate]
    )

    # Configure agent with custom tools
    options = ClaudeAgentOptions(
        custom_mcp_servers=[server]
    )

    async with ClaudeSDKClient(options=options) as client:
        # Use the tools
        print("User: What time is it?")
        response = await client.send_user_message("What time is it?")

        async for message in response:
            if message.type == "assistant":
                print(f"Assistant: {message.content}\n")

        print("User: Calculate 15 * 23")
        response = await client.send_user_message("Calculate 15 * 23")

        async for message in response:
            if message.type == "assistant":
                print(f"Assistant: {message.content}\n")


async def note_taking_agent():
    """Agent with note-taking capabilities."""
    print("\n=== Note-Taking Agent ===\n")

    # Create MCP server with note tools
    server = create_sdk_mcp_server(
        name="notes-tools",
        version="1.0.0",
        tools=[store_note, list_notes]
    )

    options = ClaudeAgentOptions(
        custom_mcp_servers=[server],
        system_prompt="You are a note-taking assistant. Help users store and retrieve notes."
    )

    async with ClaudeSDKClient(options=options) as client:
        # Store some notes
        print("User: Save a note titled 'Meeting' with content 'Discuss Q4 goals'")
        response = await client.send_user_message(
            "Save a note titled 'Meeting' with content 'Discuss Q4 goals'"
        )

        async for message in response:
            if message.type == "assistant":
                print(f"Assistant: {message.content}\n")

        print("User: Save another note 'Ideas' with 'Build a chatbot'")
        response = await client.send_user_message(
            "Save another note titled 'Ideas' with content 'Build a chatbot'"
        )

        async for message in response:
            if message.type == "assistant":
                print(f"Assistant: {message.content}\n")

        # List notes
        print("User: Show me all my notes")
        response = await client.send_user_message("Show me all my notes")

        async for message in response:
            if message.type == "assistant":
                print(f"Assistant: {message.content}\n")


async def combined_tools():
    """Agent with both built-in and custom tools."""
    print("\n=== Combined Tools ===\n")

    # Create MCP server
    server = create_sdk_mcp_server(
        name="all-tools",
        version="1.0.0",
        tools=[get_current_time, calculate, store_note, list_notes]
    )

    options = ClaudeAgentOptions(
        custom_mcp_servers=[server],
        # Built-in tools are available by default
        system_prompt="You have access to file operations, calculations, and note-taking."
    )

    async with ClaudeSDKClient(options=options) as client:
        print("User: Calculate the average of numbers in data.txt and save it as a note")
        response = await client.send_user_message(
            """
            If data.txt exists, read it, calculate the average of the numbers,
            and save the result as a note titled 'Average'.
            If data.txt doesn't exist, create it with sample numbers first.
            """
        )

        async for message in response:
            if message.type == "assistant":
                print(f"Assistant: {message.content}\n")


async def main():
    """Run all examples."""
    try:
        await basic_custom_tools()
        await note_taking_agent()
        await combined_tools()

    except Exception as e:
        print(f"\nError: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    print("Claude Agent SDK - Custom Tools Examples\n")
    anyio.run(main)
