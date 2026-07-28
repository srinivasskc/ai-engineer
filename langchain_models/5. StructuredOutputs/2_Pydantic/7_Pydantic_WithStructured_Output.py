# Working with Github API Key
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from typing import TypedDict, Annotated, Optional, Literal
from pydantic import BaseModel, Field

load_dotenv()

# https://github.com/marketplace/models

model = ChatOpenAI(
    model="gpt-4o-mini",
    openai_api_key=os.getenv("GITHUB_TOKEN"),
    base_url="https://models.inference.ai.azure.com",
    temperature=0,
)


# Schema Format - Output - Pydantic
class Review(BaseModel):
    key_themes: list[str] = Field(
        description="write down all the key themes discussed in the review in a list"
    )

    summary: str = Field(description="A brief summary of the review")

    sentiment: Optional[Literal["Pos", "Neg"]] = Field(
        default=None,
        description="Return sentiment of the review - either positive or negative or neutral",
    )

    pros: Optional[list[str]] = Field(
        default=None, description="Write down all the pros inside in a list"
    )
    cons: Optional[list[str]] = Field(
        default=None, description="Write down all the cons inside in a list"
    )


structured_model = model.with_structured_output(Review)


result = structured_model.invoke(
    """Great book. Being a military officer, I've read a lot of of books on Strategy. I think the book is misnamed, it is really a primer on game theory. What is the difference between Game Theory and Strategy you ask? Game theory is primarily mathematical. It uses math to guide decision-making. If you have good data on probabilities of different courses of action or a reasonably bounded problem, game theory is extremely helpful. Strategy, as the book title suggests, is more of an art when you don't have a lot of data on probability. I found this book was really good when thinking through decisions a coach or manager would make in sports, such as when to go for two-points instead of one, how to decide which way to kick on a penalty kick. Some great insights here.

As an example, one of the insights from the book is that if your opponent would gain an advantage if they knew your course of action ahead of time, there is an advantage to you to include some level of randomness in your decision-making. It uses the example of a penalty kick in soccer. Even if you're better kicking to the right, if the goalkeeper knows ahead of time which way you will kick, your chances of scoring a goal will decrease. You can increase your chance of scoring by randomly deciding to kick to the left some percentage (here is where the math kicks in) even through you aren't as good kicking to the left. Same would apply to a football team on the goal line. Even if you are much better running the ball, you will have a better chance of scoring touchdowns if you throw the ball a certain percentage of the time. Again, the math proves this even if you aren't a believer."""
)

# print(type(result))
print(result)
# dictionary
result_dict = result.dict()
print(result_dict)

print(result_dict["sentiment"])
print(result_dict.keys())
