import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import streamlit as st

load_dotenv()

model = ChatOpenAI(
    model="gpt-4o-mini",
    openai_api_key=os.getenv("GITHUB_TOKEN"),
    base_url="https://models.inference.ai.azure.com",
    temperature=1.5,
)

st.header("Research Assistant Tool")
user_input = st.text_input("Enter your prompt: ")

if st.button("Summarize"):
    result = model.invoke(user_input)
    st.write(result.content)
