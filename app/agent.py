from langchain.agents import initialize_agent, AgentType
from app.config import get_llm
from app.tools import web_search, weather

def create_agent():
    llm = get_llm()

    tools = [web_search, weather]

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
         max_iterations=1
    )

    return agent
