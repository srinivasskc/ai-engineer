import os
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(
    model="gpt-4o-mini",
    openai_api_key=os.getenv("GITHUB_TOKEN"),
    base_url="https://models.inference.ai.azure.com",
    temperature=1.5,
)

messages = [
    SystemMessage(content="You are a Helpful Chat Assistant"),
    HumanMessage(content="Tell me about Langchain"),
]

response = model.invoke(messages)

messages.append(AIMessage(content=response.content))

print(messages)
