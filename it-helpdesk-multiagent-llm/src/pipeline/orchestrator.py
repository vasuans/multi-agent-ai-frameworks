import json
import os

from src.agents.triage_agent import TriageAgent
from src.agents.resolution_agent import ResolutionAgent
from src.agents.audit_agent import AuditAgent

class Orchestrator:
    def __init__(self):
        self.triage = TriageAgent()
        self.resolution = ResolutionAgent()
        self.audit = AuditAgent()

    def load_tickets(self):
        cur_dir = os.path.dirname(os.path.dirname(__file__))  # src/
        data_path = os.path.join(cur_dir, "data", "sample_tickets.json")
        with open(data_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def run(self):
        tickets = self.load_tickets()
        results = []
        for t in tickets:
            triage_res = self.triage.classify(t["text"])
            resolution_res = self.resolution.generate_resolution(triage_res)
            self.audit.write_log(t, triage_res, resolution_res)
            results.append({
                "ticket": t,
                "triage": triage_res,
                "resolution": resolution_res
            })
        return results
