from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

# Embedding Models: https://developers.openai.com/api/docs/guides/embeddings

embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32)

# By default, the length of the embedding vector is 1536 for text-embedding-3-small or 3072 for text-embedding-3-large
# Dimensions represent the length of the vector (the list of numbers) that the embedding model generates to represent a piece of text.


result = embedding.embed_query("Delhi is the capital of India.")
print(str(result))
