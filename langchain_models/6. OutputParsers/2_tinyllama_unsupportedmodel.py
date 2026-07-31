# String Output Parser - This model does not give structured output
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

# https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0
# First, we need to connect the HuggingFaceEndpoint.

huggingface_llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it", task="text-generation"
)


model = ChatHuggingFace(llm=huggingface_llm)


# 1st Prompt - Detailed Report
template1 = PromptTemplate(
    template="Write a detailed report on {topic}", input_variables=["topic"]
)


# 2nd prompt - Summary
template2 = PromptTemplate(
    template="Write a 5 liner summary on the following text \n {text}",
    input_variables=["text"],
)

prompt1 = template1.invoke({"topic": "Blackhole"})
result = model.invoke(prompt1)
print(result)

prompt2 = template2.invoke({"text": result.content})
summary = model.invoke(prompt2)
print(summary)
