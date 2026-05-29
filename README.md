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

1. Create a script named `main.py` and paste the provided workflow code into it.
2. Run the script:
```bash
# activate virtualenv first (see Prerequisites)
python main.py --topic "Your Topic Here" --verbose
```

Upon execution the scaffolded workflow will run using stubbed agents; the `--verbose` flag prints intermediate payloads and evaluation traces.

## 📁 Product Structure

This repository is currently in architecture-first mode. The current workspace contains the design and documentation assets needed to define the eventual implementation.

### Current Available Material

```text
whatappbot/
├── ARCHITECTURE.md                # Enterprise MAS architecture definition
├── README.md                      # Project documentation + usage guidance
└── assets/
    ├── workflow-diagram.png       # Visual workflow representation
    └── enterprise-mas-flow.png    # Enterprise MAS topology diagram
```

### Material Not Yet Available

- `main.py` — entrypoint implementation for the CrewAI workflow
- `final_output.md` — generated markdown content output
- `tests/` — automated unit or integration tests
- implementation-specific configuration or orchestration scripts

### Final Product Structure (Target)

When the architecture is implemented, this repository should look like:

```text
whatappbot/
├── ARCHITECTURE.md                # Final MAS architecture and design reference
├── README.md                      # Project overview, setup, and usage
├── main.py                        # Workflow implementation entrypoint
├── requirements.txt               # Python dependency manifest
├── .env.example                   # Example environment variables
├── final_output.md                # Generated markdown publication output
├── assets/
│   ├── workflow-diagram.png       # Workflow diagram
│   └── enterprise-mas-flow.png    # MAS topology diagram
└── tests/
    └── test_main.py              # Basic implementation tests
```

This structure provides a clean separation between architecture and implementation, and makes it clear which assets are already available versus which files are planned for the final deliverable.

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

