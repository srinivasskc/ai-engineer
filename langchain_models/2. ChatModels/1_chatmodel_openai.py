# Can work with OpenAI Key
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# https://developers.openai.com/api/docs/models/all
model = ChatOpenAI(
    model="gpt-4o-mini-2024-07-18", temperature=0, max_completion_tokens=10
)

# results = model.invoke("What is the capital of India")
results = model.invoke("Write a 5 line poem on Cricket")

print(results)
print(results.content)
