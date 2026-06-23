import os
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)

def search_web(query):

    try:

        results = client.search(
            query=query,
            max_results=5
        )

        formatted_results = []

        for item in results["results"]:

            formatted_results.append({
                "title": item["title"],
                "url": item["url"],
                "content": item["content"]
            })

        return formatted_results

    except Exception as e:

        print("Search Error:", e)

        return []