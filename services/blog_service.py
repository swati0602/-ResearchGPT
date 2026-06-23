from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
import os

load_dotenv()

GEMINI_API_KEY = st.secrets.get(
    "GEMINI_API_KEY",
    os.getenv("GEMINI_API_KEY")
)

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GEMINI_API_KEY
)

def generate_blog(topic):

    prompt = PromptTemplate.from_template("""
    Write a professional blog article about:

    {topic}

    Include:

    - Introduction
    - Main Content
    - Conclusion
    """)

    chain = prompt | llm

    result = chain.invoke({
        "topic": topic
    })

    return result.content
