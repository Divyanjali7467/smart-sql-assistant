import streamlit as st
from groq import Groq

api_key = "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"
client = Groq(api_key=api_key)

if api_key is None:
    st.error("Groq API key not found.")
    st.stop()

client = Groq(api_key=api_key)
