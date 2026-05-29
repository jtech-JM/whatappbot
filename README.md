# Multi-Agent Market Research & Copywriting Crew

An autonomous multi-agent workflow built with [CrewAI](https://crewai.com) that orchestrates a team of specialized AI agents to conduct web research and generate structured, markdown-formatted blog content.

Learn more about the technical workflow design in [`ARCHITECTURE.md`](ARCHITECTURE.md).

![Workflow Diagram](assets/workflow-diagram.png)

## 🚀 Overview

This architecture avoids the common pitfalls of single-prompt AI systems (such as hallucinations and loss of focus) by splitting the operational logic into two distinct steps:
1. **Information Gathering:** A dedicated Research Agent searches the live web for verified facts.
2. **Content Synthesis:** A dedicated Writing Agent processes the research brief without web access, ensuring high fidelity to the source data.

## 🛠️ Prerequisites & Installation

### 1. Clone or Set Up Your Project Directory
Create a new directory and navigate into it:
```bash
mkdir multi-agent-crew && cd multi-agent-crew
```

### 2. Create a Python Virtual Environment
Create and activate a local virtual environment before installing dependencies:

**Linux/macOS:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows (PowerShell):**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies
Install the required CrewAI core, tools, LLM orchestration packages, and the Pydantic schema library:
```bash
pip install -r requirements.txt
```

### 4. Install Development Dependencies
For tests and linting, install the developer dependency set:
```bash
pip install -r requirements-dev.txt
```

### 4. Configure Environment Variables
Copy `.env.example` to `.env` and update it with your API credentials.

```bash
cp .env.example .env
```

Update the values in `.env`:
```text
OPENAI_API_KEY=your-openai-api-key
SERPER_API_KEY=your-serper-api-key
```

If you prefer shell exports instead of an env file, you can also use:

**On Linux/macOS:**
```bash
export OPENAI_API_KEY="your-openai-api-key"
export SERPER_API_KEY="your-serper-api-key"
```

**On Windows (Command Prompt):**
```cmd
set OPENAI_API_KEY=your-openai-api-key
set SERPER_API_KEY=your-serper-api-key
```

**On Windows (PowerShell):**
```powershell
$env:OPENAI_API_KEY="your-openai-api-key"
$env:SERPER_API_KEY="your-serper-api-key"
```

## 💻 Usage

Run the scaffolded workflow from the repository root after activating your virtual environment:

```bash
python main.py --topic "Your Topic Here" --verbose
```

The workflow will:
- build a `ResearchBriefPayload` from a stubbed Researcher,
- generate markdown content via the Writer,
- evaluate the draft via the Editor/Critic,
- persist the session to `data/{session_id}.json`, and
- write `final_output.md` when the draft is approved.

## 📁 Product Structure

This repository currently includes both architecture and a working scaffold implementation.

```text
whatappbot/
├── ARCHITECTURE.md                # Enterprise MAS architecture definition
├── README.md                      # Project documentation + usage guidance
├── main.py                        # Workflow implementation entrypoint
├── persistence.py                 # JSON session persistence layer
├── requirements.txt               # Python dependency manifest
├── .env.example                   # Example environment variables
├── final_output.md                # Sample generated markdown output
├── tests/                         # Automated unit tests
│   ├── test_main.py
│   └── test_persistence.py
└── assets/
    ├── workflow-diagram.png       # Workflow diagram
    └── enterprise-mas-flow.png    # Enterprise MAS topology diagram
```

The current implementation includes:
- a Multi-Agent workflow scaffold (`main.py`)
- typed payload contracts in `schemas.py`
- a persistence layer in `persistence.py`
- automated tests for both workflow execution and session saving
- a GitHub Actions CI workflow in `.github/workflows/ci.yml`

## 🧩 Step 1: Rigid Pydantic Data Schemas

The first implementation step is to establish the inter-agent payload contracts as strongly typed models.

- `schemas.py` contains the core Pydantic models that mirror the JSON schemas defined in `ARCHITECTURE.md`.
- `ResearchBriefPayload` is the contract passed from the Researcher to the Writer.
- `ContentEvaluationSchema` is the contract returned by the Editor/Critic to the system control layer.

This ensures all future node implementations can share a consistent schema and minimizes ambiguity during development.

## 🎛️ Customization

To change the research subject, simply update the `inputs` dictionary at the bottom of `main.py`:

```python
result = tech_crew.kickoff(inputs={"topic": "Your Custom Tech Topic Here"})
```

