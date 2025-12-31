import streamlit as st
from question_generator import generate_questions

st.set_page_config(
    page_title="AI Question Generator",
    layout="centered"
)

st.title("🧠 AI Question Generator")
st.write("Generate interview questions using LangChain + Groq")

# ---- Inputs ----
topic = st.text_input("Topic", value="JVM")

level = st.selectbox(
    "Difficulty Level",
    ["Easy", "Medium", "Hard"]
)

count = st.number_input(
    "Number of Questions",
    min_value=1,
    max_value=10,
    value=5
)

# ---- Action ----
if st.button("Generate Questions"):
    with st.spinner("Generating questions..."):
        result = generate_questions(topic, level, count)

    st.success("Questions generated successfully!")
    st.text_area(
        "Generated Questions",
        result,
        height=300
    )
