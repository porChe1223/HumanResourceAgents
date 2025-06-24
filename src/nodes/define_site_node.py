from agents.define_site_agent import define_site_agent, SiteList, PydanticOutputParser
from helpers.runnable_retry import runnable_retry
from langgraph.graph import MessagesState
from langgraph.types import Command
from nodes.research_node import research_node

def define_site_node(state: MessagesState) -> Command[research_node]:
    result = runnable_retry(define_site_agent).invoke(state)
    output_parser = PydanticOutputParser(pydantic_object=SiteList)
    try:
        parsed = output_parser.invoke(result["messages"][-1]["content"])
        sites = parsed.sites
    except Exception as e:
        sites = []
    merged_messages = state.get("messages", []) + result.get("messages", [])
    return Command(
        update={
            "messages": merged_messages,
            "sites": sites,
        },
        goto="research",
    )
