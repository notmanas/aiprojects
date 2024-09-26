import os
from openai import OpenAI
import streamlit as st
from gpt_response import get_openai_response


st.set_page_config(layout="wide")
st.title("Prompt Generator")

columns = st.columns(2)
with columns[0]:
    user_input = st.text_input("Enter your requirements for prompt here:")
    examples = st.text_area("Enter examples here (any format works)")
    run_btn = st.button("Run")

response_from_gpt = ""
if run_btn:
    response_from_gpt = get_openai_response(user_input=user_input, examples=examples)
    st.code(response_from_gpt)
