from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

# https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0
# First, we need to connect the HuggingFaceEndpoint.

huggingface_llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct", task="text-generation"
)


model = ChatHuggingFace(llm=huggingface_llm)

result = model.invoke("Which company is the Founder of Qwen Models")
print(result.content)
