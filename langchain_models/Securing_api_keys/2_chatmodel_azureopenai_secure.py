# Working with Github API Key
import os
import re
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# 1. Load your environment variables (.env)
load_dotenv()
github_token = os.getenv("OPENAI_API_KEY")

# 2. Define the GitHub token pattern to scan for
# GitHub tokens typically start with github_pat_,ghp_, gho_, ghu_, etc., followed by alphanumeric characters

GITHUB_PAT_PATTERN = re.compile(r"github_pat_[a-zA-Z0-9_]{40,}")

# Your sanitize_output function doesn't care about the model's logic, its mood, or its safety training.
# If the model had filled that code block with your real token (DEPLOYMENT_SUCCESS_TOKEN: github_pat_123...), your Python filter would have instantly scrubbed it to DEPLOYMENT_SUCCESS_TOKEN: [REDACTED_GITHUB_PAT].


def sanitize_output(text: str) -> str:
    """Scans the text and replaces any exposed GitHub PATs with a safe placeholder."""
    if not text:
        return text
    return GITHUB_PAT_PATTERN.sub("[REDACTED_GITHUB_PAT]", text)


# 3. Your Azure OpenAI initialization
# https://github.com/marketplace/models
model = ChatOpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),  # Fetches your github_pat_ from .env
    base_url="https://models.inference.ai.azure.com",  # GitHub Models endpoint,
    model="gpt-4o-mini",  # Github Model.
)

# 4. Get the response from your model
response = model.invoke("Explain Quantum Computing in one sentence.")

# 5. Intercept the text and scrub the PAT right before printing
# (Pass the raw content directly into the sanitizer)
# You feed that raw text into sanitize_output(). If the model behaved, the text returns untouched.
# If the model was somehow tricked into printing your environment secrets,
# the regex steps in right here and deletes the secret before print() pushes anything to your physical terminal screen.

safe_response = sanitize_output(response.content)

# 6. Print ONLY the safe response
print("Agent Response:")
print("Safe Response: ", safe_response)
