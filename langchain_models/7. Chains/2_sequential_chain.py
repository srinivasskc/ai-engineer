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

prompt1 = PromptTemplate(
    template="Generate a detailed report about {topic}", input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Generate summary in 5 bullet points from the following text \n {text}",
    input_variables=["text"],
)

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

response = chain.invoke({"topic": "EU AI Act"})
print(response)

chain.get_graph().print_ascii()
