from agents.research_agent import research_agent
from helpers.runnable_retry import runnable_retry
from langgraph.graph import MessagesState
from langgraph.types import Command
from nodes.orchestrate_node import orchestrate_node

def research_node(state: MessagesState) -> Command[orchestrate_node]:
    result = runnable_retry(research_agent).invoke(state)
    merged_messages = state.get("messages", []) + result.get("messages", [])
    return Command(
        update={
            "messages": merged_messages
        },
        goto="orchestrate",
    )
