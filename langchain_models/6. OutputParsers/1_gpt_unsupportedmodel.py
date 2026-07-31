# String Output Parser - This model does not give structured output

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

load_dotenv()

# https://github.com/marketplace/models

model = ChatOpenAI(
    model="gpt-4o-mini",
    base_url="https://models.inference.ai.azure.com",
    temperature=1.5,
    api_key=os.getenv("GITHUB_TOKEN"),
)

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
