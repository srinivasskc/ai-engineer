from langchain_huggingface import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = HuggingFaceEndpointEmbeddings(
    model="sentence-transformers/all-MiniLM-L6-v2"
)

documents = [
    "Delhi is capital of India",
    "Hyderabad is capital of Telangana",
    "Bangalore is capital of Karnataka",
    "Chennai is capital of Tamil Nadu",
    "Amaravati is capital of Andhra Pradesh",
]

vector_result = embeddings.embed_documents(documents)
print(str(vector_result))

# print(type(vector_result)) - List to Str
