# 🚀 Agentic SRE: Fintech Observability with MCP

A Model Context Protocol (MCP) server designed for high-scale Fintech environments. This project bridges the gap between AI Agents and Kubernetes observability stacks, enabling autonomous incident investigation.

## 🛠 Tech Stack
* **Runtime:** Python 3.12+
* **Framework:** FastMCP
* **Orchestration:** Kubernetes
* **Observability:** Prometheus, Loki, Tempo
* **Protocol:** MCP

## 🚀 Key Features
* **Live Prometheus Querying:** Agent can fetch p95 latency on-demand.
* **Context-Aware SRE:** LLM can correlate metrics through the MCP gateway.
* **Security:** Designed for VPC/AirGap environments.

## 💻 Quick Start
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 src/server.py
```

---
*Let's build systems that don't break.* 🛠️
