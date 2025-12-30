from langchain_core.prompts import PromptTemplate

question_prompt = PromptTemplate(
    input_variables=["topic", "level", "count"],
    template="""
You are an expert educator.

TASK:
Generate EXACTLY {count} {level}-level questions on the topic "{topic}".

RULES (MANDATORY):
- Output must be a numbered list from 1 to {count}
- Each question must be on a NEW line
- Do NOT include answers
- Do NOT combine questions
- Do NOT add explanations
- ONLY output the questions list

Start now.
"""
)
