from typing import Annotated
from langchain_core.tools import tool, InjectedToolCallId
from langgraph.prebuilt import InjectedState
from langgraph.graph import MessagesState
from langgraph.types import Command


def create_assignee(
    *,
    chain_name: str,
    description: str | None = None
):
    """ハンドオフツール

    エージェント間のハンドオフを行うツール

    Args:
        agent_name: ハンドオフするエージェント名
        description: ハンドオフの説明
        
    Returns:
        handoff_tool: ハンドオフツール
    """
    name = f"transfer_to_{chain_name}"
    description = description or f"Ask {chain_name} for help."

    @tool(name, description=description)
    def assign(
        state: Annotated[MessagesState, InjectedState],
        tool_call_id: Annotated[str, InjectedToolCallId],
        *args, **kwargs,
    ) -> Command:
        tool_message = {
            "role": "tool",
            "content": f"Successfully transferred to {chain_name}",
            "name": name,
            "tool_call_id": tool_call_id,
        }
        return Command(
            goto=chain_name,  
            update={**state, "messages": state["messages"] + [tool_message]},  
            graph=Command.PARENT,  
        )

    return assign
