from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

def generate_linkedin(topic):

    prompt = PromptTemplate.from_template("""
    Create a professional LinkedIn post about:

    {topic}

    Add relevant hashtags.
    """)

    chain = prompt | llm

    result = chain.invoke({
        "topic": topic
    })

    return result.content