from langchain_core.prompts import PromptTemplate
import json
from langchain_core.load import dumps


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


# Serialize the template to a JSON string
json_data = dumps(template)

# Saving to Json File.
with open("template.json", "w", encoding="utf-8") as f:
    f.write(json_data)


# Running the template with - python prompt_generator.py
# Template will be stored in template.json file.
