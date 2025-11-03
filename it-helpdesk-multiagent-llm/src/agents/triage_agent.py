"""
triage_agent.py
---------------
Agent 1: Classifies incoming IT tickets.

Responsibilities:
- Takes a raw text description of a user’s issue.
- Predicts the category (e.g. VPN, password reset, laptop performance, etc.).
- Predicts priority: Low / Medium / High.
- Creates a short summary (1 sentence).
- Returns a structured dictionary.

Right now this uses an OpenAI model through LangChain.
Later we can swap this for a cheaper local model without touching main.py.
"""

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src')))

from utils.models import get_llm


class TriageAgent:
    def __init__(self):
        # Reuse the shared LLM you defined in utils/models.py
        self.llm = get_llm()

    def _build_prompt(self, ticket_text: str) -> str:
        """
        Build the instruction we send to the model.

        We FORCE the model to answer in JSON.
        This makes it easier to parse and pass to the next agent.
        """
        return f"""
You are an IT helpdesk triage assistant.
You will read an employee's IT support ticket and classify it.

For the given ticket text, you MUST respond ONLY in valid JSON with keys:
- category: one of ["VPN Issue", "Password / Access", "Laptop Performance", "Email / Outlook", "Network / Connectivity", "Other"]
- priority: one of ["Low", "Medium", "High"]
- summary: short 1-sentence summary of the user's problem

Rules:
- High priority if they are blocked from doing work (e.g. cannot connect to VPN, cannot access corporate systems).
- Medium priority if the issue affects them but they can still work.
- Low priority if it's just a general complaint or slow performance.

Ticket text:
\"\"\"{ticket_text}\"\"\"
Respond with JSON only, no commentary.
"""

    def classify(self, ticket_text: str) -> dict:
        """
        Ask the LLM to classify this ticket.
        Returns a Python dict with category, priority, summary, ticket_text.
        """

        prompt = self._build_prompt(ticket_text)

        # Call the model using LangChain's ChatOpenAI interface.
        # .invoke() returns an AIMessage with .content which is the model's text output.
        response = self.llm.invoke(prompt)

        raw_output = response.content

        # We'll try to parse the JSON the model returns.
        # If parsing fails for any reason, we fall back gracefully instead of crashing.
        import json
        try:
            parsed = json.loads(raw_output)
        except json.JSONDecodeError:
            parsed = {
                "category": "Unknown",
                "priority": "Unknown",
                "summary": raw_output.strip()
            }

        # Add original text so we always keep context
        parsed["ticket_text"] = ticket_text
        return parsed
