# No ChatHistory Chatbot

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(
    model="gpt-4o-mini",
    openai_api_key=os.getenv("GITHUB_TOKEN"),
    base_url="https://models.inference.ai.azure.com",
    temperature=1.5,
)

while True:
    user_input = input("You: ")
    if user_input == "exit":
        break
    response = model.invoke(user_input)
    print("AI Response: ", response.content)
