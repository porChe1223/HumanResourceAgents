from agents.report_agent import report_agent
from helpers.runnable_retry import runnable_retry
from langgraph.graph import MessagesState, END
from langgraph.types import Command

def report_node(state: MessagesState) -> Command[END]:
    result = runnable_retry(report_agent).invoke(state)
    merged_messages = state.get("messages", []) + result.get("messages", [])
    return Command(
        update={
            "messages": merged_messages
        },
        goto="__end__",
    )
