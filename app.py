import streamlit as st
from prompts.sql_prompt import PROMPT
from utils.groq_helper import ask_llm
from utils.db_helper import run_query

st.set_page_config(
    page_title="Smart SQL Assistant",
    layout="wide"
)

st.title("🤖 Smart SQL Assistant")

question = st.text_input(
    "Ask your question",
    placeholder="Show employees with salaries greater than 50000"
)

if st.button("Generate Result"):

    prompt = PROMPT.format(question=question)

    sql_query = ask_llm(prompt)

    st.write("Generated query:")
    st.write(sql_query)

    try:
        result = run_query(sql_query)
        st.dataframe(result)

    except Exception as e:
        st.error(e)