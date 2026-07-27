# Working with Github API Key
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from typing import TypedDict

load_dotenv()

# https://github.com/marketplace/models

model = ChatOpenAI(
    model="gpt-4o-mini",
    openai_api_key=os.getenv("GITHUB_TOKEN"),
    base_url="https://models.inference.ai.azure.com",
    temperature=0,
)


# Schema Format - Output
class Review(TypedDict):
    summary: str
    sentiment: str


structured_model = model.with_structured_output(Review)


result = structured_model.invoke(
    """Human Edge in the AI Age discusses how people can stay relevant as AI becomes more common. Nitin Seth introduces the POSSIBLE framework and reflects on skills like adaptability, leadership, and problem-solving. The book mixes business insights with philosophy and personal stories, offering a broad perspective on the future of work."""
)

# print(type(result))
print("Summary: ", result["summary"])
print("Sentiment: ", result["sentiment"])
