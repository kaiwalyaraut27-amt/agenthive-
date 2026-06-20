# 🚀 AgentHive

## Multi-Agent Startup Builder using Google ADK, MCP, and Gemini

AgentHive is an AI-powered multi-agent startup planning platform that transforms a startup idea into a comprehensive business plan using specialized AI agents.

Built for the Kaggle AI Agents: Intensive Vibe Coding Capstone Project.

---

## Problem

Startup founders spend weeks performing:

* Market research
* Competitor analysis
* Customer discovery
* Product planning
* Technical architecture design
* Business validation

These activities are often fragmented across multiple tools and require significant manual effort.

---

## Solution

AgentHive uses a coordinated team of AI agents that collaborate to generate a startup blueprint from a single idea.

Users provide a startup concept, and AgentHive automatically generates:

* Market Research
* Competitor Analysis
* Customer Personas
* Product Requirements Document (PRD)
* Technical Architecture
* Startup Report

---

## Key Features

### Multi-Agent System

AgentHive consists of specialized agents:

* Research Agent
* Competitor Agent
* Persona Agent
* Product Agent
* Critic Agent
* Architecture Agent
* Security Agent

A Root Agent orchestrates the entire workflow.

---

### Google ADK Integration

AgentHive uses Google Agent Development Kit (ADK) to implement a hierarchical multi-agent architecture.

The Root Agent coordinates specialized sub-agents that perform independent tasks and collaborate to produce high-quality startup plans.

---

### MCP Integration

AgentHive integrates Model Context Protocol (MCP) servers.

#### Filesystem MCP

Capabilities:

* Save startup reports
* Read generated reports
* Manage project outputs

#### GitHub MCP

Capabilities:

* Generate README templates
* Generate repository structures

---

### Antigravity (Self-Improvement)

AgentHive implements an iterative feedback loop.

Workflow:

Product Agent
→ Product Plan V1
→ Critic Agent
→ Improvement Suggestions
→ Product Plan V2

This process improves output quality before presenting results to the user.

---

### Security Features

AgentHive includes a dedicated Security Agent.

Implemented protections:

* Prompt Injection Detection
* API Key Detection
* Input Validation
* Malicious Input Screening

Unsafe requests are blocked before reaching the agent workflow.

---

## System Architecture

Insert architecture diagram here.

![Architecture](docs/architecture.png)

---

## Antigravity Workflow

Insert antigravity diagram here.

![Antigravity](docs/antigravity.png)

---

## Security Architecture

Insert security diagram here.

![Security](docs/security.png)

---

## Project Structure

```text
AgentHive/

├── agents/
├── tools/
├── ui/
├── mcp_servers/
├── docs/
├── tests/
├── data/

├── app.py
├── config.py
├── requirements.txt
├── README.md
└── .env.example
```

---

## Installation

Clone repository:

```bash
git clone https://github.com/YOUR_USERNAME/agenthive.git

cd agenthive
```

Create virtual environment:

```bash
python -m venv venv
```

Activate:

Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create .env file:

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

---

## Run Application

```bash
streamlit run app.py
```

---

## Example Workflow

Input:

```text
AI Tutor Platform for Engineering Students
```

Generated Outputs:

* Market Research
* Competitor Analysis
* Customer Personas
* Product Plan
* Technical Architecture
* Startup Report

---

## Technology Stack

* Python
* Streamlit
* Google Gemini
* Google ADK
* MCP SDK
* GitHub
* Model Context Protocol

---

## Competition Requirements Covered

| Requirement        | Status |
| ------------------ | ------ |
| Multi-Agent System | ✅      |
| Google ADK         | ✅      |
| MCP Server         | ✅      |
| Antigravity        | ✅      |
| Security Features  | ✅      |
| Deployability      | ✅      |
| Agent Skills       | ✅      |

---

## Future Improvements

* Real-time web research
* Investor pitch deck generation
* Financial forecasting
* Team formation recommendations
* Multi-language support

---

## Demo Video

Add YouTube link after upload.

---

## Live Demo

Add deployment URL after deployment.

---

## License

MIT License

---

Built with Google ADK, MCP, Gemini, and Streamlit for the Kaggle AI Agents Capstone Project.
