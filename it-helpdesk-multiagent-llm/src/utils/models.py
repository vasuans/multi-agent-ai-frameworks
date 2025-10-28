import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv(override=True)

def get_llm(model_name: str = "gpt-4o-mini", temperature: float = 0.2):

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY not found"

        )

    llm = ChatOpenAI(
        model=model_name,
        temperature=temperature,
        openai_api_key=api_key

    )
    print("Loaded LLM model:", llm)
    return llm

