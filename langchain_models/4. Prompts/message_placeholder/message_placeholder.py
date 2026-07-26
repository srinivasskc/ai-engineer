import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# Chat Template
chat_template = ChatPromptTemplate(
    [
        ("system", "You are a helpful customer support agent"),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{query}"),
    ]
)

chat_history = []

# Load Chat History
with open("chat_history.txt", encoding="utf-8") as f:
    chat_history.extend(f.readlines())
    # This f.readlines() - Reads all lines at once from the file and returns them as a list of string

# print(chat_history)

# Prompt
prompt = chat_template.invoke(
    {"chat_history": chat_history, "query": "Where is my refund?"}
)

print(prompt)
