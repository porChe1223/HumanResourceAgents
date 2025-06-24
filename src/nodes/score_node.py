from agents.score_agent import score_agent
from helpers.runnable_retry import runnable_retry
from langgraph.graph import MessagesState
from langgraph.types import Command
from nodes.report_node import report_node

def score_node(state: MessagesState) -> Command[report_node]:
    result = runnable_retry(score_agent).invoke(state)
    merged_messages = state.get("messages", []) + result.get("messages", [])
    return Command(
        update={
            "messages": merged_messages
        },
        goto="report",
    )
