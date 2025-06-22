from typing import Annotated
from langchain_core.tools import tool, InjectedToolCallId
from langgraph.prebuilt import InjectedState
from langgraph.graph import MessagesState
from langgraph.types import Command


def create_handoff_tool(
    *,
    agent_name: str,
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
    name = f"transfer_to_{agent_name}"
    description = description or f"Ask {agent_name} for help."

    @tool(name, description=description)
    def handoff_tool(
        state: Annotated[MessagesState, InjectedState],
        tool_call_id: Annotated[str, InjectedToolCallId],
    ) -> Command:
        tool_message = {
            "role": "tool",
            "content": f"Successfully transferred to {agent_name}",
            "name": name,
            "tool_call_id": tool_call_id,
        }
        return Command(
            goto=agent_name,
            update={**state, "messages": state["messages"] + [tool_message]},  
            graph=Command.PARENT,
        )

    return handoff_tool


# 調査対象決定ノードにタスクを渡す
assign_to_define_research_target_node = create_handoff_tool(
    agent_name="define_target_node",
    description="Assign task to a define_research_target agent.",
)

# 調査サイト決定ノードにタスクを渡す
assign_to_define_research_strategy_node = create_handoff_tool(
    agent_name="define_site_node",
    description="Assign task to a define_research_strategy agent.",
)

# スクレイピングノードにタスクを渡す
assign_to_scrape_and_chunk_node = create_handoff_tool(
    agent_name="scrape_and_chunk_node",
    description="Assign task to a scrape_and_chunk agent.",
)

# 評価ノードにタスクを渡す
assign_to_score_node = create_handoff_tool(
    agent_name="score_node",
    description="Assign task to a score agent.",
)
