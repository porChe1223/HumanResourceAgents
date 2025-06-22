from langgraph.graph import END, StateGraph, MessagesState, START
from agents.orchestrate_agent import orchestrate_agent
# from agents.client_agent import client_agent
from agents.define_target_agent import define_target_agent
from agents.define_site_agent import define_site_agent
from agents.research_agent import research_agent
from agents.score_agent import score_agent
from agents.report_agent import report_agent
from helpers.runnable_retry import runnable_retry

"""
LangGraphのワークフローグラフを定義
"""
workflow = (
    # --- グラフを定義 ---
    StateGraph(MessagesState)

    # --- エージェントを定義 ---
    .add_node(
      runnable_retry(orchestrate_agent),
      destinations=(
        # "client_agent",
        "define_target_agent",
        "define_site_agent",
        # "split_and_wait_node",
        "research_agent",
        # "collect_result_node",
        "score_agent",
        "report_agent",
        END
    ))

    # --- エージェントを追加 ---
    # .add_node(client_agent)
    .add_node(runnable_retry(define_target_agent))
    .add_node(runnable_retry(define_site_agent))
    # .add_node(split_and_wait_node)
    .add_node(runnable_retry(research_agent))
    # .add_node(collect_result_node)
    .add_node(runnable_retry(score_agent))
    .add_node(runnable_retry(report_agent))

    # --- 司令から開始 ---
    .add_edge(
      START,
      "orchestrate_agent",  # 司令から各エージェントへ
    )

    # --- 指令を挟まない接続 ---
    # サイト決定後はそのまま調査へ
    .add_edge(
      "define_target_agent",
      "define_site_agent",
    )
    .add_edge(
      "define_site_agent",
      "research_agent",
    )
    # 評価後はそのままレポートへ
    .add_edge(
      "score_agent",
      "report_agent",
    )

    # --- 各エージェントから司令へ ---
    # （サイト決定エージェントと評価エージェントから司令へはない）
    # .add_edge(
    #   "client_agent",
    #   "orchestrate_agent",
    # )
    .add_edge(
      "define_target_agent",
      "orchestrate_agent",
    )
    .add_edge(
      "research_agent",
      "orchestrate_agent",
    )

    # --- 終了 ---
    .add_edge(
      "report_agent",
      END,
    )

    # --- グラフをコンパイル ---
    .compile()
)
