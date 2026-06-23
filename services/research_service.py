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

def generate_research(topic, search_results):

    formatted_sources = "\n\n".join(
        [
            f"""
            Title: {item['title']}
            Content: {item['content']}
            URL: {item['url']}
            """
            for item in search_results
        ]
    )

    prompt = PromptTemplate.from_template("""
    You are an expert research analyst.

    Topic:
    {topic}

    Sources:
    {search_results}

    Create a report containing:

    1. Overview
    2. Key Findings
    3. Advantages
    4. Challenges
    5. Conclusion
    """)

    chain = prompt | llm

    result = chain.invoke({
        "topic": topic,
        "search_results": formatted_sources
    })

    return result.content
