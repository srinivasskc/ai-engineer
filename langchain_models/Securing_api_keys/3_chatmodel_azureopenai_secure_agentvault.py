# Incomplete
import os
import sys
import re
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Read the environment variables piped from agent-vault instead of looking at the disk
if not sys.stdin.isatty():
    load_dotenv(stream=sys.stdin)
else:
    load_dotenv()  # Fallback to normal loading if run without agent-vault


model = ChatOpenAI(
    model="gpt-4o-mini",
    base_url="https://models.inference.ai.azure.com",
)
response = model.invoke("Explain Quantum Computing in one sentence.")
print(response.content)
