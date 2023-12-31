from langchain import OpenAI, SerpAPIWrapper
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
from decouple import config

llm = OpenAI(temperature=0)
search = SerpAPIWrapper(serpapi_api_key=config('SERPAPI_API_KEY'))
tools = [
    Tool(
        name="Intermediate Answer",
        func=search.run,
        description="useful for when you need to ask with search"
    )
]

self_ask_with_search = initialize_agent(tools, llm, agent=AgentType.SELF_ASK_WITH_SEARCH, verbose=True)
self_ask_with_search.run("Which social media messaging app has the most users?")
