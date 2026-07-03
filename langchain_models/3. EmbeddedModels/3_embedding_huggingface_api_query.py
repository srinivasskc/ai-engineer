from langchain_huggingface import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = HuggingFaceEndpointEmbeddings(
    model="sentence-transformers/all-MiniLM-L6-v2"
)

text = "Delhi is the capital of India"

vector_result = embeddings.embed_query(text)
print(str(vector_result))

# print(type(vector_result)) - List to Str
