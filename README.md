<div align="center">

# Azure AI Capstone

### Applying LLMs, Prompt Engineering, RAG, and AI Agents on Microsoft Azure

[![Azure](https://img.shields.io/badge/Microsoft-Azure-0078D4?style=flat-square&logo=microsoftazure&logoColor=white)](https://azure.microsoft.com/)
[![Foundry](https://img.shields.io/badge/Microsoft-Foundry-5C2D91?style=flat-square&logo=microsoft&logoColor=white)](https://learn.microsoft.com/en-us/training/azure/ai-foundry)
[![Learn Plan](https://img.shields.io/badge/Microsoft%20Learn-Full%20Course%20Here-107C10?style=for-the-badge&logo=microsoftacademic&logoColor=white)](https://learn.microsoft.com/en-us/plans/zw0wtdtowmyxe2?sharingId=7ECC3D2E58004DEB&wt.mc_id=studentamb_564123)
[![Status](https://img.shields.io/badge/status-in%20progress-yellow?style=flat-square)]()
[![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)]()

</div>

---

## What is this?

This repo is the final project (Milestone 9) for the **AI, NLP & Agents with Microsoft Azure** learning path — a free, structured course on Microsoft Learn covering LLM fundamentals, prompt engineering, Azure AI Language, AI Foundry, agents, and RAG.

**You don't need a Microsoft Learn account to use this repo.** Everything you need to understand and build the project is documented right here. The Learn Plan link above is optional — it gives you the full guided course with modules, quizzes, and progress tracking if you want the structured learning experience alongside this project.

### What the course covers

| Milestone | Topic |
|---|---|
| 1 | AI & NLP Foundations |
| 2 | How Large Language Models Work |
| 3 | Prompt Engineering |
| 4 | Azure AI Language Services |
| 5 | Azure AI Foundry |
| 6 | Build AI Agents |
| 7 | Retrieval-Augmented Generation (RAG) |
| 8 | Responsible AI & Security |
| 9 | **Capstone Project ← you are here** |

> **Access the full course free:** https://learn.microsoft.com/en-us/plans/zw0wtdtowmyxe2?sharingId=7ECC3D2E58004DEB&wt.mc_id=studentamb_564123

---

## About This Project

This is the capstone project for **[AI, NLP & Agents with Microsoft Azure: A Complete Learning Path](https://learn.microsoft.com/en-us/plans/zw0wtdtowmyxe2?sharingId=7ECC3D2E58004DEB&wt.mc_id=studentamb_564123)**, a 9-milestone Microsoft Learn Plan covering everything from LLM fundamentals to building AI agents on Azure.

The capstone is where theory turns into a real, working system. Pick one of the three project tracks below, build it, and document it here.

## Table of Contents

- [What is this?](#what-is-this)
- [Project Tracks](#project-tracks)
- [Tech Stack](#tech-stack)
- [Architecture](#architecture)
- [Getting Started](#getting-started)
- [Evaluation Criteria](#evaluation-criteria)
- [Deliverables](#deliverables)
- [Learning Path Reference](#learning-path-reference)
- [Author](#author)

## Project Tracks

Choose one and build it end to end.

### 🔍 Track A: RAG-Based Q&A Agent
An agent that answers questions grounded in your own documents, with citations back to source.

- Retrieval via Azure AI Search
- Grounded generation via Foundry IQ / Foundry Agent Service
- Builds on Milestones 5 (Foundry) and 7 (RAG)

### 🛠️ Track B: Tool-Calling AI Agent
An agent that reasons about *when* to act, not just what to say.

- At least two custom tools (calculator, lookup, database query, your choice)
- Orchestrated with Microsoft Foundry Agent Service + Agent Framework
- Builds on Milestones 5 (Foundry) and 6 (Agents)

### 🌐 Track C: Nepali-English NLP Tool
A tool tackling a real low-resource language problem.

- Sentiment analysis, translation, or transcription for Nepali / code-switched text
- Powered by Azure AI Language
- Evaluated against a small, manually labeled test set
- Builds on Milestones 2 (LLMs) and 4 (Azure AI Language)

## Tech Stack

| Layer | Technology |
|---|---|
| Models | Azure OpenAI / Foundry Models |
| Retrieval | Azure AI Search, Foundry IQ |
| Agents | Microsoft Foundry Agent Service, Agent Framework |
| Language Services | Azure AI Language |
| Interface | *(fill in: CLI, notebook, web app, etc.)* |

## Architecture

Each track has a different flow. Pick the one that matches your chosen track.

**Track A — RAG-Based Q&A Agent**
```
Your Documents (PDFs / notes)
        |
        v
  Azure AI Search          <-- indexes and retrieves relevant chunks
        |
        v
  Foundry IQ / Agent Service  <-- generates a grounded answer
        |
        v
  Response + Source Citation  <-- user sees the answer AND where it came from
```

**Track B — Tool-Calling AI Agent**
```
  User Input
        |
        v
  Foundry Agent Service       <-- decides whether a tool is needed
        |
   _____|______
  |            |
  v            v
Tool 1       Tool 2           <-- e.g. calculator, weather API, DB query
  |            |
  v            v
  Agent assembles final response from tool outputs
```

**Track C — Nepali-English NLP Tool**
```
  Input Text (Nepali / code-switched)
        |
        v
  Azure AI Language Service   <-- sentiment / translation / transcription
        |
        v
  Output + Confidence Score
        |
        v
  Compared against manually labeled test set
```

## Getting Started

### Step 1 — Complete the course first

This capstone builds directly on the 8 milestones in the Microsoft Learn plan. If you are coming here fresh, go through the course before diving into code:

> [AI, NLP & Agents with Microsoft Azure — Full Learning Path](https://learn.microsoft.com/en-us/plans/zw0wtdtowmyxe2?sharingId=7ECC3D2E58004DEB&wt.mc_id=studentamb_564123)

Once you have covered Milestones 1–8, you will have the Azure knowledge needed to build any of the three tracks here.

### Step 2 — Set up your Azure environment

Before running any code you need an active Azure subscription. Free accounts work fine for this project.

- [Create a free Azure account](https://azure.microsoft.com/free/)
- [Set up Azure AI Foundry](https://learn.microsoft.com/en-us/training/azure/ai-foundry)
- For Track A/B: deploy a model in Foundry and note your endpoint + key
- For Track C: enable Azure AI Language in your resource group

### Step 3 — Clone and configure

```bash
git clone https://github.com/Aadarshttech/azure-ai-capstone.git
cd azure-ai-capstone

# Create a virtual environment
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows

pip install -r requirements.txt

# Copy the environment template and fill in your keys
cp .env.example .env
```

Open `.env` and add your Azure credentials:

```
AZURE_OPENAI_ENDPOINT=your_endpoint_here
AZURE_OPENAI_KEY=your_key_here
AZURE_SEARCH_ENDPOINT=your_search_endpoint   # Track A only
AZURE_SEARCH_KEY=your_search_key             # Track A only
AZURE_LANGUAGE_ENDPOINT=your_lang_endpoint  # Track C only
AZURE_LANGUAGE_KEY=your_lang_key            # Track C only
```

### Step 4 — Pick your track and build

Open the folder for your chosen track and follow the notebook or script inside:

```
track-a-rag/        <-- RAG Q&A Agent
track-b-agents/     <-- Tool-Calling Agent
track-c-nlp/        <-- Nepali-English NLP Tool
```

Each folder will have its own `README.md` with track-specific instructions once implementation is added.

## Evaluation Criteria

| Criteria | What it means |
|---|---|
| **Functionality** | The system works, shown with real examples, not just described |
| **Grounding** | Outputs are traceable to a source or method, not hallucinated |
| **Responsible AI** | At least one risk, bias, or limitation is acknowledged |
| **Clarity** | Someone unfamiliar with the project could follow this README and understand it |

## Deliverables

- [ ] Working application (repo, notebook, or deployed demo)
- [ ] Architecture write-up
- [ ] Sample inputs and outputs
- [ ] Prompt design notes (if applicable)
- [ ] Responsible AI considerations section

## Learning Path Reference

- [Microsoft Foundry Training](https://learn.microsoft.com/en-us/training/azure/ai-foundry)
- [Develop AI Agents on Azure](https://learn.microsoft.com/en-us/training/paths/develop-ai-agents-azure/)
- [Explore Azure AI Language](https://learn.microsoft.com/en-us/training/paths/explore-natural-language-processing/)
- [Full Learn Plan (this project's parent path)](https://learn.microsoft.com/en-us/plans/zw0wtdtowmyxe2?sharingId=7ECC3D2E58004DEB&wt.mc_id=studentamb_564123)

## Author

**Aadarsh Pandit**
BTech AI, Kathmandu University
Microsoft Student Ambassador Contributor ID: `studentamb_564123`

[![GitHub](https://img.shields.io/badge/GitHub-Aadarshttech-181717?style=flat-square&logo=github)](https://github.com/Aadarshttech)

---

<div align="center">
<sub>Built as part of the Microsoft Learn Student Ambassadors program.</sub>
</div>
