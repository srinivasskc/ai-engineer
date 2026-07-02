# Working
from langchain_openrouter import ChatOpenRouter
from dotenv import load_dotenv

load_dotenv()

# https://openrouter.ai/openai/gpt-oss-20b:free
model = ChatOpenRouter(model="openai/gpt-oss-20b:free")

response = model.invoke("What is the capital of India!")

print(response.content)
