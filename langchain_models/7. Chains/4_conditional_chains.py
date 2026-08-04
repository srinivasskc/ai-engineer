import os
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda


load_dotenv()

# Model 1
huggingface_llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1-Distill-Qwen-7B", task="text-generation"
)

model = ChatHuggingFace(llm=huggingface_llm)

parser1 = StrOutputParser()


class Feedback(BaseModel):
    sentiment: Literal["Positive", "Negative"] = Field(
        description="Give me the sentiment of the feedback"
    )


parser2 = PydanticOutputParser(pydantic_object=Feedback)


prompt1 = PromptTemplate(
    template="Classify the sentiment of the following feedback text into Positive or Negative \n {feedback} \n {format_instruction}",
    input_variables=["feedback"],
    partial_variables={"format_instruction": parser2.get_format_instructions()},
)

classifier_chain = prompt1 | model | parser2

# classifier_chain.get_graph().print_ascii()

# result = classifier_chain.invoke({"feedback": "This is a terrible book"}).sentiment
# print(result)

prompt2 = PromptTemplate(
    template="Write an appropriate response to this positive feedback \n  {feedback}",
    input_variables=["feedback"],
)

prompt3 = PromptTemplate(
    template="Write an appropriate response to this negative feedback \n  {feedback}",
    input_variables=["feedback"],
)

branch_chain = RunnableBranch(
    (lambda x: x.sentiment == "Positive", prompt2 | model | parser1),
    (lambda x: x.sentiment == "Negative", prompt3 | model | parser1),
    RunnableLambda(lambda x: "could not find sentiment"),
)


final_chain = classifier_chain | branch_chain

result = final_chain.invoke({"feedback": "This is a terrific book"})
print(result)

final_chain.get_graph().print_ascii()
