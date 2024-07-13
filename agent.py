import os

from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_core.prompts import ChatPromptTemplate

from tools import *

def initialize_agent():
    os.environ['OPENAI_API_KEY'] = 'sk-None-UYrgNTFk4TjYLNQ0dnX6T3BlbkFJTDopdRybVwanAaD7AaW8'

    # Create the language model
    llm = ChatOpenAI(model="gpt-3.5-turbo-1106", temperature=0)

    tools = get_tools()
    
    # You are very powerful assistant called Lyra that helps with questions about exclusively about league of legends and world of warcraft.
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """            
                You are a very powerful assistant called Lyra that answers questions about league of legends and world of warcraft. 
                Make sure to use your tools for information.

                Key tools:
                    - search_league_of_legends_info: use to access up-to-date league of legends data.
                    - search_world_of_warcraft_info: use to access up-to-date world of warcraft data.

                Always pass user's question as an argument.
                """,
            ),
            ("placeholder", "{chat_history}"),
            ("human", "{input}"),
            ("placeholder", "{agent_scratchpad}"),
        ]
    )

    # Construct the Tools agent
    agent = create_openai_tools_agent(llm, tools, prompt)

    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    return agent_executor
