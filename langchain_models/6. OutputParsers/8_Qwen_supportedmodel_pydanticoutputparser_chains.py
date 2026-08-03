# Json Output Parser

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

# https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0
# First, we need to connect the HuggingFaceEndpoint.

huggingface_llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct", task="text-generation"
)


model = ChatHuggingFace(llm=huggingface_llm)


# Pydantic Object
class Person(BaseModel):
    name: str = Field(description="Name of the Person")
    age: int = Field(ge=18, description="Age of the Person")
    city: str = Field(description="City Name of the Person")


# Pydantic Output Parser.
parser = PydanticOutputParser(pydantic_object=Person)


# 1st Prompt - Detailed Report
template1 = PromptTemplate(
    template="Generate name, age, city of a fictional {place} person \n {format_instruction}",
    input_variables=["place"],
    partial_variables={"format_instruction": parser.get_format_instructions()},
)


chain = template1 | model | parser

# print(chain)

result = chain.invoke({"place": "Sri Lanka"})
print(result)
