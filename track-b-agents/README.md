# Track B - Tool-Calling AI Agent

## What this does

Creates a Foundry agent with two custom Python tools: a calculator and a weather lookup. The agent decides on its own when a tool is needed based on the user's message.

## Folder structure

```
track-b-agents/
  agent.py         <- main script
  README.md
```

## Setup

1. Make sure your `.env` has:
   ```
   PROJECT_CONNECTION_STRING=<your Foundry project connection string>
   ```

2. Run:
   ```bash
   python agent.py
   ```

## Adding your own tools

Open `agent.py` and define a new Python function with a clear docstring (the agent reads the docstring to understand what the tool does). Then add it to the `FunctionTool` list:

```python
def my_tool(param: str) -> str:
    """Short description of what this tool does and what param means."""
    return "result"

functions = FunctionTool(functions=[calculator, weather_lookup, my_tool])
```

That is all. The agent will automatically know when to call it.

## Replacing the mock weather tool

Swap the mock dictionary in `weather_lookup` with a real API call:

```python
import requests

def weather_lookup(city: str) -> str:
    """Returns current weather for a city using OpenWeatherMap."""
    api_key = os.environ["OPENWEATHER_API_KEY"]
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    data = requests.get(url).json()
    return f"{data['weather'][0]['description']}, {data['main']['temp']}C"
```

## Resources

- [Foundry Agent Service - Function Tools](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/agents/tools/function-tool)
- [azure-ai-projects FunctionTool reference](https://learn.microsoft.com/en-us/python/api/azure-ai-projects/azure.ai.projects.models.functiontool)
- [Develop AI Agents on Azure (Microsoft Learn path)](https://learn.microsoft.com/en-us/training/paths/develop-ai-agents-azure/)
- [Official agent samples (GitHub)](https://github.com/Azure-Samples/azureai-samples/tree/main/scenarios/Agents)
- [OpenWeatherMap free API](https://openweathermap.org/api) (for a real weather tool)
