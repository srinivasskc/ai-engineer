# Needs better machine configuration
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import os

# Set your custom cache directory
os.environ["HF_HOME"] = "F:/huggingface_cache"

# 1. Initialize the local pipeline wrapper (Note: task is lowercase)
llm_model = HuggingFacePipeline.from_model_id(
    model_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation",
    pipeline_kwargs={"temperature": 0.5, "max_new_tokens": 100, "do_sample": True},
)

# 2. Wrap it using the correct keyword argument 'llm='
model = ChatHuggingFace(llm=llm_model)

# 3. Invoke the local model
response = model.invoke("What is HuggingFacePipeline?")
print(response.content)
