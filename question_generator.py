from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="llama-3.1-8b-instant",
    temperature=0.7
)

prompt = PromptTemplate(
    input_variables=["topic", "level", "count"],
    template="""
You are a computer science interviewer.

Generate EXACTLY {count} {level}-level interview questions on the topic "{topic}".

Rules:
- Number each question (1., 2., 3., ...)
- One question per line
- No answers
- No explanations
- Do not repeat questions

Output:
"""
)

chain = prompt | llm

def generate_questions(topic: str, level: str, count: int) -> str:
    response = chain.invoke({
        "topic": topic,
        "level": level,
        "count": count
    })
    return response.content
