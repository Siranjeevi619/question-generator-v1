import streamlit as st

def render_form():
    topic = st.text_input("Topic", "JVM")

    level = st.selectbox(
        "Difficulty",
        ["Easy", "Medium", "Hard"]
    )

    count = st.number_input(
        "Number of questions",
        min_value=1,
        max_value=10,
        value=5
    )

    submit = st.button("Generate")

    return topic, level, count, submit


def render_result(result):
    st.success("Done")
    st.text_area("Questions", result, height=300)
