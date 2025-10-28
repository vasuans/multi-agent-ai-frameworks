import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src')))

from agents.triage_agent import TriageAgent


if __name__ == "__main__":
    triage = TriageAgent()
    result = triage.classify("VPN stopped working after the latest update.")
    print(result)