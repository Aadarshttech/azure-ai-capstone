# Track A - RAG-Based Q&A Agent

## What this does

Uploads your documents to Azure AI Foundry, creates a File Search-powered agent, and lets you ask questions grounded in those documents. Every answer cites which file it came from.

## Folder structure

```
track-a-rag/
  agent.py         <- main script
  data/            <- put your PDFs, .txt, .md, or .docx files here
  README.md
```

## Setup

1. Make sure your `.env` has:
   ```
   PROJECT_CONNECTION_STRING=<your Foundry project connection string>
   ```
   Get this from: Azure AI Foundry portal -> your project -> Settings -> Connection string

2. Drop your documents into the `data/` folder.

3. Run:
   ```bash
   python agent.py
   ```

## How to get your Project Connection string

1. Go to https://ai.azure.com
2. Open your project
3. Click **Settings** in the left panel
4. Copy the **Project connection string**

## Resources

- [Azure AI Foundry Agent Service docs](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/agents/create-agent)
- [File Search tool reference](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/agents/tools/file-search)
- [azure-ai-projects SDK reference](https://learn.microsoft.com/en-us/python/api/overview/azure/ai-projects-readme)
- [Official RAG agent sample (GitHub)](https://github.com/Azure-Samples/azureai-samples)
- [Tutorial: Build an agentic retrieval solution](https://learn.microsoft.com/en-us/azure/search/tutorial-rag-build-solution)
