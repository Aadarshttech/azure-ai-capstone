<div align="center">

# Azure AI Capstone

## Applying LLMs, prompt engineering, RAG, and AI agents on Microsoft Azure

[![Azure](https://img.shields.io/badge/Microsoft-Azure-0078D4?style=flat-square&logo=microsoftazure&logoColor=white)](https://azure.microsoft.com/)
[![Foundry](https://img.shields.io/badge/Microsoft-Foundry-5C2D91?style=flat-square&logo=microsoft&logoColor=white)](https://learn.microsoft.com/en-us/training/azure/ai-foundry)
[![Learn Plan](https://img.shields.io/badge/Microsoft%20Learn-Plan-107C10?style=flat-square&logo=microsoftacademic&logoColor=white)](https://learn.microsoft.com/en-us/plans/zw0wtdtowmyxe2?sharingId=7ECC3D2E58004DEB&wt.mc_id=studentamb_564123)
[![Status](https://img.shields.io/badge/status-in%20progress-yellow?style=flat-square)]()
[![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)]()

</div>

---

## About this project

This is the capstone project for [AI, NLP & Agents with Microsoft Azure: A Complete Learning Path](https://learn.microsoft.com/en-us/plans/zw0wtdtowmyxe2?sharingId=7ECC3D2E58004DEB&wt.mc_id=studentamb_564123), a 9-milestone Microsoft Learn Plan. The plan covers LLM fundamentals and building AI agents on Azure.

The capstone turns theory into a working system. Pick one of the project tracks below, build it, and document it here.

## Table of contents

- [Project tracks](#project-tracks)
- [Tech stack](#tech-stack)
- [Architecture](#architecture)
- [Getting started](#getting-started)
- [Evaluation criteria](#evaluation-criteria)
- [Deliverables](#deliverables)
- [Learning path reference](#learning-path-reference)
- [Author](#author)

## Project tracks

Choose one and build it end to end.

### Track A: RAG-based Q&A agent
An agent that answers questions grounded in your own documents, with citations back to the source.

- Retrieval via Azure AI Search
- Grounded generation via Foundry IQ or Foundry Agent Service
- Builds on milestones 5 (Foundry) and 7 (RAG)

### Track B: Tool-calling AI agent
An agent that reasons about when to act and what to say.

- At least two custom tools (calculator, lookup, database query, your choice)
- Orchestrated with Microsoft Foundry Agent Service and Agent Framework
- Builds on milestones 5 (Foundry) and 6 (Agents)

### Track C: Nepali-English NLP tool
A tool tackling a low-resource language problem.

- Sentiment analysis, translation, or transcription for Nepali or code-switched text
- Powered by Azure AI Language
- Evaluated against a small, manually labeled test set
- Builds on milestones 2 (LLMs) and 4 (Azure AI Language)

## Tech stack

| Layer | Technology |
|---|---|
| Models | Azure OpenAI, Foundry Models |
| Retrieval | Azure AI Search, Foundry IQ |
| Agents | Microsoft Foundry Agent Service, Agent Framework |
| Language services | Azure AI Language |
| Interface | *(fill in: CLI, notebook, web app, etc.)* |

## Architecture

```text
[ Add your architecture diagram or flow here once the track is chosen ]

Example (Track A - RAG):
User Query -> Azure AI Search (retrieval) -> Foundry IQ (grounding) -> Response + Citation
```

## Getting started

```bash
git clone https://github.com/Aadarshttech/azure-ai-capstone.git
cd azure-ai-capstone

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

cp .env.example .env
```

## Evaluation criteria

| Criteria | What it means |
|---|---|
| Functionality | The system works, shown with real examples |
| Grounding | Outputs are traceable to a source or method |
| Responsible AI | At least one risk, bias, or limitation is acknowledged |
| Clarity | Someone unfamiliar with the project could follow this file and understand it |

## Deliverables

- [ ] Working application (repo, notebook, or deployed demo)
- [ ] Architecture write-up
- [ ] Sample inputs and outputs
- [ ] Prompt design notes (if applicable)
- [ ] Responsible AI considerations section

## Learning path reference

- [Microsoft Foundry training](https://learn.microsoft.com/en-us/training/azure/ai-foundry)
- [Develop AI agents on Azure](https://learn.microsoft.com/en-us/training/paths/develop-ai-agents-azure/)
- [Explore Azure AI Language](https://learn.microsoft.com/en-us/training/paths/explore-natural-language-processing/)
- [Full learn plan](https://learn.microsoft.com/en-us/plans/zw0wtdtowmyxe2?sharingId=7ECC3D2E58004DEB&wt.mc_id=studentamb_564123)

## Author

Aadarsh Pandit
BTech AI, Kathmandu University
Microsoft Student Ambassador Contributor ID: `studentamb_564123`

[![GitHub](https://img.shields.io/badge/GitHub-Aadarshttech-181717?style=flat-square&logo=github)](https://github.com/Aadarshttech)

---

<div align="center">
<sub>Built as part of the Microsoft Learn Student Ambassadors program.</sub>
</div>
