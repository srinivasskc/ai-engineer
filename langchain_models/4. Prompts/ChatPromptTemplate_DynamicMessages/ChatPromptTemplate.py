# Multi-Turn Messages - ChatPromptTemplate.

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

model = ChatOpenAI(
    model="gpt-4o-mini",
    openai_api_key=os.getenv("GITHUB_TOKEN"),
    base_url="https://models.inference.ai.azure.com",
    temperature=0,
)

# This is different way from PromptTemplate.
chat_template = ChatPromptTemplate(
    [
        ("system", "You are a helpful {domain} expert"),
        ("human", "Explain in simple terms, what is {topic}"),
    ]
)


prompt_message = chat_template.invoke({"domain": "Testing", "topic": "SOAK Tests"})

print(prompt_message)
