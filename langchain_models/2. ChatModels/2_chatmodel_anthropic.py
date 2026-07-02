# Can Work
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

# https://platform.claude.com/docs/en/about-claude/models/overview
model = ChatAnthropic(model_name="claude-haiku-4-5-20251001")
result = model.invoke("What is the capital of India")
print(result.content)
