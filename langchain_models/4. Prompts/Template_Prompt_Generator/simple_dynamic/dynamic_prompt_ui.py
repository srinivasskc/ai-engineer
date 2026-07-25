import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import streamlit as st
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatOpenAI(
    model="gpt-4o-mini",
    openai_api_key=os.getenv("GITHUB_TOKEN"),
    base_url="https://models.inference.ai.azure.com",
    temperature=1.5,
)

st.header("Research Assistant Tool")

# Attention Is All You Need (Classic AI architecture paper)
# AI Assurance: A Comprehensive Testing Strategy for Enterprise AI Systems (Enterprise governance, reliability & quality assurance)
# (Over)Reliance on Test Agents in AI-Assisted Software Testing (Human-AI interaction, empirical software engineering & testing)
# MCP Server Architecture Patterns for LLM-Integrated Applications (System architecture, protocols & integration design)


paper_input = st.selectbox(
    "Select the research paper",
    [
        "Attention Is All You Need",
        "AI Assurance: A Comprehensive Testing Strategy for Enterprise AI Systems",
        "(Over)Reliance on Test Agents in AI-Assisted Software Testing",
        "MCP Server Architecture Patterns for LLM-Integrated Applications",
    ],
)

style_options = {
    "EL15 / Plain English": "Simple, everyday language with real-world analogies (no heavy jargon).",
    "Real-World Analogy Focus": "Explains core ideas using everyday scenarios (e.g., comparing Attention to a library search).",
    "Executive / Business Summary": "High-level takeaways focused on impact, business value, and ROI.",
    "Practical / How-To": "Focuses on real-world application, step-by-step usage, and edge cases.",
    "Technical & Code-Oriented": "Deep dive into architecture, workflow, and code implementations.",
    "Mathematical & Algorithmic": "Focuses on underlying formulas, equations, and theoretical concepts.",
}

selected_style_key = st.selectbox(
    "Select Explanation Style",
    options=list(style_options.keys()),
    help="Choose how complex or practical you want the explanation to be.",
)

# Extract the detailed description for the LLM
selected_style_description = style_options[selected_style_key]

length_input = st.selectbox(
    "Select the Explanation Length",
    [
        "Short (1-2) paragraphs",
        "Medium (3-5) Paragraphs",cd 
        "Long (Detailed Explanation)",
    ],
)

# Creating Prompt Template using langchain_core.prompts import PromptTemplate
template = PromptTemplate(
    input_variables=["paper_input", "style_name", "style_description", "length_input"],
    validate_template=True,
    template="""
Please summarize the research paper titled {paper_input} with the following specifications:
- Explanation Style Requestd: {style_name} ({style_description})
- Explanation Length: {length_input}

Guidelines:
1. Core Concepts & Findings:
   - Clearly explain the primary contribution, architecture, or empirical findings of the paper.
2. Technical / Mathematical Details (if applicable):
   - Include key equations, formulas, or system flow diagrams/snippets depending on what the paper focuses on.
3. Practical Implications & Takeaways:
   - Highlight practical risks, implementation advice, or architectural trade-offs mentioned in the paper.
4. Analogies & Intuition:
   - Use relatable analogies where useful to simplify complex concepts.
5. Real World Examples:
   - Summarize the main contribution using relatable real-world examples wherever relevant.
6. Structure & Tone:
   - Ensure the explanation strictly adheres to the requested style definition: "{style_description}".
7. Accuracy:
   - If key technical or mathematical information is not present in the paper, respond with "Insufficient information available" for that section instead of guessing.
""",
)

# Filling the placeholders in the template.
prompt = template.invoke(
    {
        "paper_input": paper_input,
        "style_name": selected_style_key,
        "style_description": selected_style_description,
        "length_input": length_input,
    }
)


if st.button("Summarize"):
    response = model.invoke(prompt)
    print(response.content)
    st.write(response.content)
