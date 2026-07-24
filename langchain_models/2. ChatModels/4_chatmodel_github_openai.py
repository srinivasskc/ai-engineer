# Working with Github API Key
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

# https://github.com/marketplace/models

model = ChatOpenAI(
    model="gpt-4o-mini",
    openai_api_key=os.getenv("GITHUB_TOKEN"),
    base_url="https://models.inference.ai.azure.com",
    temperature=1.5,
)

response = model.invoke("Write a 5 line poem on Cricket")
# response = model.invoke("Explain Quantum Computing in one sentence.")
print(response.content)
