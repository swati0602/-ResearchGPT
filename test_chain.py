from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

prompt = PromptTemplate.from_template("""
Research the topic: {topic}

Give:
1. Overview
2. Key Points
3. Advantages
4. Challenges
""")

chain = prompt | llm

result = chain.invoke({
    "topic": "Blockchain Technology"
})

print(result.content)