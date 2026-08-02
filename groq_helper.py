import streamlit as st
from groq import Groq

api_key = st.secrets["GROQ_API_KEY"]

client = Groq(api_key=api_key)


def ask_llm(prompt):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content
