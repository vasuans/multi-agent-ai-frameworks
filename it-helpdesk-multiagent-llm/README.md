# IT Helpdesk Multi-Agent LLM (LangChain)

## What this is
This project is a proof-of-concept IT service desk assistant built with LangChain and multi-agent orchestration.

### Why it matters
Internal IT teams lose hours every week on repeated "Level 1" issues like VPN access, password reset, and printer setup.
Modern agentic AI systems are already resolving 30–70% of these tickets automatically and cutting MTTR (mean time to resolution) by up to 60%. :contentReference[oaicite:14]{index=14}

This repo shows how we could reproduce that in a safe, auditable way.

## Architecture
- **TriageAgent**  
  Classifies each ticket ("VPN issue", "password reset", "laptop slow") and sets priority.

- **ResolutionAgent**  
  Drafts a step-by-step fix or response using internal knowledge base articles.

- **AuditAgent**  
  Writes a structured compliance log (who asked for what, what fix was recommended, timestamp). This is critical for enterprise trust.

- **Orchestrator**  
  A controller that passes the ticket through these agents in sequence. In production this could plug into ServiceNow / Jira / Slack.

## Tech stack
- Python
- LangChain for agent reasoning + tool calls
- OpenAI model for natural language understanding and draft responses
- `.env` for secrets handling
- Simple JSON to simulate an IT ticket queue

## Status
- [ ] TriageAgent stub
- [ ] ResolutionAgent stub
- [ ] AuditAgent stub
- [ ] Orchestrator stub
- [ ] Sample tickets
- [ ] Basic tests

I am building this in public to demonstrate practical agentic AI: not just "a chatbot", but multiple collaborating agents that plan, act, and document.
