import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src')))
from utils.models import get_llm

class ResolutionAgent:
    def __init__(self):
        self.llm = get_llm()
        base_dir = os.path.dirname(os.path.dirname(__file__))
        kb_path = os.path.join(base_dir, "data", "knowledge_base.md")
        with open(kb_path, "r", encoding="utf-8") as f:
            self.knowledge_base = f.read()

    def generate_resolution(self, triage_result: dict) -> dict:
        ticket_text = triage_result.get("ticket_text", "")
        category = triage_result.get("category", "Other")
        prompt = f"""
You are an IT support assistant.
Use the following internal KB to suggest a fix.

KB:
{self.knowledge_base}

Ticket:
Category: {category}
Text: {ticket_text}

Return JSON with:
- steps: list of steps to fix
- reply: short message to user
"""
        resp = self.llm.invoke(prompt)
        import json
        try:
            data = json.loads(resp.content)
        except json.JSONDecodeError:
            data = {
                "steps": ["Review KB manually."],
                "reply": resp.content.strip()
            }
        return data
