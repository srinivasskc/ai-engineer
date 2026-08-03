import os
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()


huggingface_llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct", task="text-generation"
)


model = ChatHuggingFace(llm=huggingface_llm)


prompt = PromptTemplate(
    template="Generate 5 Interesting facts about {topic}", input_variables=["topic"]
)


parser = StrOutputParser()


chain = prompt | model | parser

# Result from Chain.
result = chain.invoke({"topic": "cricket"})
print(result)

# Visualizing the Chains
chain.get_graph().print_ascii()
