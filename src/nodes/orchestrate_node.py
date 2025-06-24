from agents.orchestrate_agent import orchestrate_agent
from helpers.runnable_retry import runnable_retry
from langgraph.graph import MessagesState, END
from langgraph.types import Command
from typing import TypedDict, Literal
from llms.openai import llm_openai_4o as llm

# 仮のメンバーリスト
members = ["define_site", "define_target", "research", "score"]
options = members + ["FINISH"]

# 仮のsystem_prompt
system_prompt = (
    "You are an orchestrator tasked with managing a conversation between the "
    f"following workers: {members}. Given the following user request, "
    "respond with the worker to act next. Each worker will perform a "
    "task and respond with their results and status. When finished, "
    "respond with FINISH."
)

class Router(TypedDict):
    next: Literal["define_site", "define_target", "research", "score", "FINISH"]

def orchestrate_node(state: MessagesState) -> Command:
    messages = [
        {"role": "system", "content": system_prompt},
    ] + state["messages"]
    response = llm.with_structured_output(Router).invoke(messages)

    # ノード名のマッピング
    node_map = {
        "define_site": "define_site_node",
        "define_target": "define_target_node",
        "research": "research_node",
        "score": "score_node",
        "FINISH": END,
    }
    goto = node_map[response["next"]]

    # 新しいassistantメッセージとしてresponseを追加
    new_messages = state["messages"] + [
        {"role": "assistant", "content": f"Next: {response['next']}"}
    ]
    return Command(
        update={"messages": new_messages},
        goto=goto
    )
