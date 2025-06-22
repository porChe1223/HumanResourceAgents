from langgraph.graph import END, StateGraph, START
from states.workflow_state import WorkflowState
from nodes.define_target_node import define_target_node
from nodes.define_site_node import define_site_node
from nodes.scrape_and_chunk_node import scrape_and_chunk_node
from nodes.research_node import research_node
from nodes.assemble_node import assemble_node
from agents.orchestrate_agent import orchestrate_agent
from agents.score_agent import score_agent
from agents.report_agent import report_agent
from helpers.runnable_retry import runnable_retry

def orchestrate_node(state: WorkflowState) -> dict:
    """orchestrate_agentを呼び出し、メッセージを更新する
    
    Args:
        state: WorkflowState
        
    Returns:
        dict: "messages"キーにエージェントの応答メッセージ
    """
    response = runnable_retry(orchestrate_agent).invoke(state)
    return {"messages": response["messages"]}

"""
LangGraphのワークフローグラフを定義
"""
workflow = (
    # --- グラフを定義 ---
    StateGraph(WorkflowState)

    # --- ノードを定義 ---
    .add_node(
        "orchestrate_node",
        orchestrate_node,
        destinations={
            "define_target_node",    # 司令塔 => ターゲット定義
            "define_site_node",      # 司令塔 => サイト定義
            "scrape_and_chunk_node", # 司令塔 => スクレイピング
            "score_node",            # 司令塔 => 評価
            END,                     # 司令塔 => 終了
        }
    )
    .add_node(
        "define_target_node",
        define_target_node
    )
    .add_node(
        "define_site_node",
        define_site_node
    )
    .add_node(
        "scrape_and_chunk_node",
        scrape_and_chunk_node
    )
    .add_node(
        "research_node",
        research_node
    )
    .add_node(
        "assemble_node",
        assemble_node
    )
    .add_node(
        "score_node",
        runnable_retry(score_agent)
    )
    .add_node(
        "report_node",
        runnable_retry(report_agent)
    )

    # --- 接続を定義 ---
    .add_edge(
        START,
        "orchestrate_node"
    ) # 開始 => 司令塔
    .add_edge(
        "define_target_node",
        "orchestrate_node"
    ) # ターゲット定義 => 司令塔
    .add_edge(
        "define_site_node",
        "orchestrate_node",
    ) # サイト定義 => 司令塔
    .add_edge(
        "scrape_and_chunk_node",
        "research_node"
    ) # スクレイピング => 調査
    .add_edge(
        "research_node",
        "assemble_node"
    ) # 調査 => 集約
    .add_edge(
        "assemble_node",
        "orchestrate_node"
    ) # 集約 => 司令塔
    .add_edge(
        "score_node",
        "report_node"
    ) # 評価 => レポート
    .add_edge(
        "report_node",
        END
    ) # レポート => 終了

    # --- グラフをコンパイル ---
    .compile()
)

# # --- 司令塔からの分岐 ---
# def route_from_orchestrator(state: WorkflowState):
#     print("--- Route from Orchestrator ---")
#     last_message = state['ai_messages'][-1]
    
#     if "define_target_agent" in last_message.content:
#         return "define_target_node"
#     if "define_site_agent" in last_message.content:
#         return "define_site_node"
#     if "score_agent" in last_message.content:
#         return "score_agent"
#     if "report_agent" in last_message.content:
#         return "report_agent"
#     return END

# workflow_builder.add_conditional_edges(
#     "orchestrate_agent",
#     route_from_orchestrator,
#     {
#         "define_target_node": "define_target_node",
#         "define_site_node": "define_site_node",
#         "score_agent": "score_agent",
#         "report_agent": "report_agent",
#         END: END,
#     },
# )
