import json
import os
from datetime import datetime
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src')))

class AuditAgent:
    def __init__(self):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        self.log_path = os.path.join(base_dir, "data", "audit_log.jsonl")

    def write_log(self, ticket: dict, triage: dict, resolution: dict):
        entry = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "ticket": ticket,
            "triage": triage,
            "resolution": resolution
        }
        with open(self.log_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry) + "\n")
