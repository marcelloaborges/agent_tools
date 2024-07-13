from langchain_openai import ChatOpenAI
from langchain.pydantic_v1 import BaseModel, Field
from langchain.tools import tool
from langchain_core.messages import HumanMessage, SystemMessage

def get_tools():

    class SearchLeagueOfLegendsInput(BaseModel):
        query: str = Field(description="user query about league of legends")

    class SearchWorldOfWarcraftInput(BaseModel):
        query: str = Field(description="user query about world of warcraft")

    @tool("search-league-of-legends-tool", args_schema=SearchLeagueOfLegendsInput)
    def search_league_of_legends_info(query: str) -> str:
        """Look up things about league of legends news and patch notes"""

        # COMMENT THIS OUT IF YOU DON'T WANT TO USE LMSTUDIO FOR THE AUXILIAR/TOOL LLM
        llm_lol = ChatOpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio", temperature=0)
        # llm_lol = ChatOpenAI(model="gpt-3.5-turbo-1106", temperature=0)
        
        messages = [
            SystemMessage(content="You are very powerful assistant called that answers questions exclusively about league of legends."
                    "Any other questions should be answered with 'I don't have info about this rigth now, but I'm working on it'."),
            HumanMessage(content=query),
        ]
        output = llm_lol.invoke(messages)

        return output

    @tool("search-world-of-warcraft-tool", args_schema=SearchWorldOfWarcraftInput)
    def search_world_of_warcraft_info(query: str) -> str:
        """Look up things about world of warcraft news and patch notes"""
        
        # COMMENT THIS OUT IF YOU DON'T WANT TO USE LMSTUDIO FOR THE AUXILIAR/TOOL LLM
        llm_wow = ChatOpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio", temperature=0)
        # llm_wow = ChatOpenAI(model="gpt-3.5-turbo-1106", temperature=0)
        
        messages = [
            SystemMessage(content="You are very powerful assistant that answers questions exclusively about world of warcraft."
                    "Any other questions should be answered with 'I don't have info about this rigth now, but I'm working on it'."),
            HumanMessage(content=query),
        ]
        output = llm_wow.invoke(messages)

        return output

    tools = [
        search_league_of_legends_info,
        search_world_of_warcraft_info
    ]

    return tools