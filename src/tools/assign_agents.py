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
        *args, **kwargs,
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


# --- Handoffs ---
# クライアントエージェントにタスクを渡す
assign_to_client_agent = create_handoff_tool(
    agent_name="client_agent",
    description="Assign task to a client agent.",
)

# 調査対象決定エージェントにタスクを渡す
assign_to_define_research_target_agent = create_handoff_tool(
    agent_name="define_target_agent",
    description="Assign task to a define_research_target agent.",
)

# 調査方針決定エージェントにタスクを渡す
assign_to_define_research_strategy_agent = create_handoff_tool(
    agent_name="define_site_agent",
    description="Assign task to a define_research_strategy agent.",
)

# 調査エージェントにタスクを渡す
assign_to_research_agent = create_handoff_tool(
    agent_name="research_agent",
    description="Assign task to a research agent.",
)

# 評価エージェントにタスクを渡す
assign_to_score_agent = create_handoff_tool(
    agent_name="score_agent",
    description="Assign task to a score agent.",
)

# レポートエージェントにタスクを渡す
assign_to_report_agent = create_handoff_tool(
    agent_name="report_agent",
    description="Assign task to a report agent.",
)
