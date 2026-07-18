"""
Track B - Tool-Calling AI Agent
--------------------------------
This starter shows how to:
  1. Define custom Python functions as tools
  2. Register them with a Foundry Agent
  3. Let the agent decide when to call them based on the user's message

Two example tools are included:
  - calculator: handles math expressions
  - weather_lookup: simulates a weather API (swap with a real one)

Prerequisites:
  - Azure AI Foundry project set up
  - PROJECT_CONNECTION_STRING in your .env file
"""

import os
import json
import math
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import FunctionTool, ToolSet
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv

load_dotenv()


# ─── Define your custom tools ────────────────────────────────────────────────

def calculator(expression: str) -> str:
    """
    Evaluates a mathematical expression and returns the result.

    Args:
        expression: A math expression string, e.g. '2 + 2' or 'sqrt(16)'

    Returns:
        The result as a string, or an error message.
    """
    try:
        # Safe eval with math functions available
        allowed = {k: getattr(math, k) for k in dir(math) if not k.startswith("_")}
        result = eval(expression, {"__builtins__": {}}, allowed)
        return str(result)
    except Exception as e:
        return f"Error evaluating expression: {e}"


def weather_lookup(city: str) -> str:
    """
    Returns the current weather for a given city.

    Args:
        city: Name of the city to look up.

    Returns:
        A short weather description string.
    """
    # Replace this with a real weather API call (e.g. OpenWeatherMap)
    mock_data = {
        "kathmandu": "Partly cloudy, 22C, humidity 65%",
        "london": "Overcast, 14C, light drizzle",
        "new york": "Sunny, 28C, humidity 40%",
        "tokyo": "Clear, 30C, humidity 55%",
    }
    return mock_data.get(city.lower(), f"Weather data not available for {city}.")


# ─── Register tools and create agent ─────────────────────────────────────────

def create_agent(client: AIProjectClient):
    """Create the Foundry agent with custom tools registered."""

    functions = FunctionTool(functions=[calculator, weather_lookup])
    tool_set = ToolSet()
    tool_set.add(functions)

    agent = client.agents.create_agent(
        model="gpt-4o",
        name="tool-calling-agent",
        instructions=(
            "You are a helpful assistant with access to tools. "
            "Use the calculator tool for any math. "
            "Use the weather_lookup tool when the user asks about weather. "
            "Reason step by step before calling a tool. "
            "Always tell the user what tool you are using and why."
        ),
        tools=tool_set.definitions,
    )

    print(f"Agent created: {agent.id}")
    return agent, tool_set


def run_conversation(client: AIProjectClient, agent, tool_set: ToolSet, message: str) -> str:
    """Send a message to the agent and process any tool calls."""
    thread = client.agents.create_thread()

    client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content=message,
    )

    # create_and_process_run handles tool call execution automatically
    # when you pass the tool_set with the actual Python functions attached
    run = client.agents.create_and_process_run(
        thread_id=thread.id,
        agent_id=agent.id,
        tool_set=tool_set,
    )

    if run.status == "failed":
        return f"Run failed: {run.last_error}"

    messages = client.agents.list_messages(thread_id=thread.id)
    return messages.data[0].content[0].text.value


def main():
    client = AIProjectClient.from_connection_string(
        credential=DefaultAzureCredential(),
        conn_str=os.environ["PROJECT_CONNECTION_STRING"],
    )

    agent, tool_set = create_agent(client)

    print("\nTool-Calling Agent ready.")
    print("Try asking: 'What is sqrt(144) + 50?' or 'What is the weather in Kathmandu?'")
    print("Type 'quit' to exit.\n")

    try:
        while True:
            user_input = input("You: ").strip()
            if user_input.lower() in ["quit", "exit", "q"]:
                break
            if not user_input:
                continue
            response = run_conversation(client, agent, tool_set, user_input)
            print(f"\nAgent: {response}\n")
    finally:
        client.agents.delete_agent(agent.id)
        print("Agent deleted.")


if __name__ == "__main__":
    main()
