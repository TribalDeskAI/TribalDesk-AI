import streamlit as st
from openai import OpenAI

def get_client() -> OpenAI:
    api_key = st.secrets.get("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("Missing OPENAI_API_KEY in Streamlit Secrets.")
    return OpenAI(api_key=api_key)
