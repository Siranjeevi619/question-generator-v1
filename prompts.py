from langchain_core.prompts import PromptTemplate

question_prompt = PromptTemplate(
    input_variables=["topic", "level", "count"],
    template="""
You are an expert educator.

Generate {count} {level}-level questions on the topic "{topic}".

Rules:
- Do NOT include answers
- Number the questions
- Keep them clear and simple
"""
)
