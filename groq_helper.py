import streamlit as st
from groq import Groq

api_key = "gsk_xxxxxxxxxxxxxxxxx"
client = Groq(api_key=api_key)

if api_key is None:
    st.error("Groq API key not found.")
    st.stop()

client = Groq(api_key=api_key)
