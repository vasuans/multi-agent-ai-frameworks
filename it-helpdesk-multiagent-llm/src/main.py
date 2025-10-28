import json
import os

from agents.triage_agent import TriageAgent


def load_sample_tickets():
    """
    Load demo IT tickets from src/data/sample_tickets.json
    Returns a Python list of dicts.
    """
    current_dir = os.path.dirname(__file__)              # src/
    data_path = os.path.join(current_dir, "data", "sample_tickets.json")

    with open(data_path, "r", encoding="utf-8") as f:
        tickets = json.load(f)

    return tickets


def run_demo():
    triage = TriageAgent()

    tickets = load_sample_tickets()

    for t in tickets:
        classification = triage.classify(t["text"])
        print("----")
        print("ticket_id:", t["ticket_id"])
        print("user:", t["user"])
        print("classification:", classification)


if __name__ == "__main__":
    run_demo()
