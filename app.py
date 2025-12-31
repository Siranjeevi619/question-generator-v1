import streamlit as st
from question_generator import generate_questions
from ui.styles import system_font
from ui.form import render_form, render_result

st.set_page_config(
    page_title="AI Question Generator",
    layout="centered"
)


st.markdown(system_font(), unsafe_allow_html=True)
st.markdown(
    "<h1 style='font-size:44px; font-weight:900;'>AI Question Generator</h1>",
    unsafe_allow_html=True
)
st.caption("generate questions with Groq + Langchain")


topic, level, count, submit = render_form()

if submit:
    with st.spinner("Generating..."):
        result = generate_questions(topic, level, count)

    render_result(result)
