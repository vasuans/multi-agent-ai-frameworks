import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src')))

from utils.models import get_llm

if __name__ == "__main__":
    llm = get_llm()
    print("Model loaded successfully:", llm)
