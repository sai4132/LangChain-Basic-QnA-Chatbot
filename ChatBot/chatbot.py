# Q&A Chatbot
from langchain.llms import OpenAI
from dotenv import load_dotenv
import streamlit as st
import os
load_dotenv() # Calls enironment variables from .env

## Function to load openai model and get response
def get_openai_response(question):
    llm = OpenAI(openai_api_key = os.getenv("OPEN_API_KEY"), model_name = "text-davinci-003", temperature=0.5)
    response = llm(question)

    return response

## Initialize our streamlit app
st.set_page_config(page_title="QnA demo")
st.header("Langchain Application")

input = st.text_input("Input: ", key = "input")
response = get_openai_response(input)

submit = st.button("Ask the question")

## If ask button is clicked
if submit:
    st.subheader("Response is:")
    st.write(response)

