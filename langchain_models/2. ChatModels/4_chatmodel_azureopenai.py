# Working with Github API Key
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# https://github.com/marketplace/models

model = ChatOpenAI(
    model="gpt-4o-mini",
    base_url="https://models.inference.ai.azure.com",
)
response = model.invoke("Explain Quantum Computing in one sentence.")
print(response.content)
