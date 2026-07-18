<div align="center">

# Azure AI Capstone

### Applying LLMs, Prompt Engineering, RAG, and AI Agents on Microsoft Azure

[![Azure](https://img.shields.io/badge/Microsoft-Azure-0078D4?style=flat-square&logo=microsoftazure&logoColor=white)](https://azure.microsoft.com/)
[![Foundry](https://img.shields.io/badge/Microsoft-Foundry-5C2D91?style=flat-square&logo=microsoft&logoColor=white)](https://learn.microsoft.com/en-us/training/azure/ai-foundry)
[![Learn Plan](https://img.shields.io/badge/Microsoft%20Learn-Plan-107C10?style=flat-square&logo=microsoftacademic&logoColor=white)](https://learn.microsoft.com/en-us/plans/zw0wtdtowmyxe2?sharingId=7ECC3D2E58004DEB&wt.mc_id=studentamb_564123)
[![Status](https://img.shields.io/badge/status-in%20progress-yellow?style=flat-square)]()
[![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)]()

</div>

---

## About This Project

This is the capstone project for **[AI, NLP & Agents with Microsoft Azure: A Complete Learning Path](https://learn.microsoft.com/en-us/plans/zw0wtdtowmyxe2?sharingId=7ECC3D2E58004DEB&wt.mc_id=studentamb_564123)**, a 9-milestone Microsoft Learn Plan covering everything from LLM fundamentals to building AI agents on Azure.

The capstone is where theory turns into a real, working system. Pick one of the three project tracks below, build it, and document it here.

## Table of Contents

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

```
[ Add your architecture diagram or flow here once the track is chosen ]

Example (Track A - RAG):
User Query -> Azure AI Search (retrieval) -> Foundry IQ (grounding) -> Response + Citation
```

## Getting Started

```bash
git clone https://github.com/Aadarshttech/azure-ai-capstone.git
cd azure-ai-capstone

# Set up environment
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install -r requirements.txt

# Configure Azure credentials
cp .env.example .env
# then fill in your Azure/Foundry keys
```

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
