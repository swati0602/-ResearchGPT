from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

import streamlit as st

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=st.secrets["GEMINI_API_KEY"]
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
