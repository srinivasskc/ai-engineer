from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

# Embedding Models: https://developers.openai.com/api/docs/guides/embeddings

embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32)

documents = [
    "Delhi is capital of India",
    "Hyderabad is capital of Telangana",
    "Bangalore is capital of Karnataka",
    "Chennai is capital of Tamil Nadu",
    "Amaravati is capital of Andhra Pradesh",
]

result = embedding.embed_documents(documents)
print(str(result))
