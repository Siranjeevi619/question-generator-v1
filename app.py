from transformers import pipeline
from langchain_community.llms import HuggingFacePipeline
from langchain_core.prompts import PromptTemplate

pipe = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    max_new_tokens=512,
    temperature=0.3,
    do_sample=False
)

llm = HuggingFacePipeline(pipeline=pipe)

question_prompt = PromptTemplate(
    input_variables=["topic", "level", "count"],
    template="""
You are an expert educator.

Generate EXACTLY {count} {level}-level questions on "{topic}".

Rules:
- Number from 1 to {count}
- Each question on a new line
- No answers
- No explanations
"""
)

chain = question_prompt | llm

result = chain.invoke({
    "topic": "Java Threads",
    "level": "beginner",
    "count": 5
})

print(result)
