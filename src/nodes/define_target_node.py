from agents.define_target_agent import define_target_agent
from helpers.runnable_retry import runnable_retry
from langgraph.graph import MessagesState
from langgraph.types import Command
from nodes.orchestrate_node import orchestrate_node

def define_target_node(state: MessagesState) -> Command[orchestrate_node]:
    result = runnable_retry(define_target_agent).invoke(state)
    merged_messages = state.get("messages", []) + result.get("messages", [])
    return Command(
        update={
            "messages": merged_messages
        },
        goto="orchestrate",
    )
