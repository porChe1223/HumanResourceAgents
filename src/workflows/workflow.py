from langgraph.graph import END, StateGraph, MessagesState, START
from nodes.define_site_node import define_site_node
from nodes.define_target_node import define_target_node
from nodes.orchestrate_node import orchestrate_node
from nodes.report_node import report_node
from nodes.research_node import research_node
from nodes.score_node import score_node

"""
LangGraphのワークフローグラフを定義
"""
workflow = (
    # --- グラフを定義 ---
    StateGraph(MessagesState)

    # --- エージェントを定義 ---
    .add_node(
      orchestrate_node,
      destinations=(
        # "client_agent",
        "define_target_node",
        "define_site_node",
        # "split_and_wait_node",
        # "research_agent",
        # "collect_result_node",
        "score_node",
        "report_node",
        END
    ))

    # --- エージェントを追加 ---
    # .add_node(client_agent)
    .add_node(define_target_node)
    .add_node(define_site_node)
    # .add_node(split_and_wait_node)
    .add_node(research_node)
    # .add_node(collect_result_node)
    .add_node(score_node)
    .add_node(report_node)

    # --- 司令から開始 ---
    .add_edge(
      START,
      "orchestrate_node",  # 司令から各エージェントへ
    )

    # --- 指令を挟まない接続 ---
    # サイト決定後はそのまま調査へ
    # .add_edge(
    #   "define_target_agent",
    #   "define_site_agent",
    # )
    .add_edge(
      "define_site_node",
      "research_node",
    )
    # 評価後はそのままレポートへ
    .add_edge(
      "score_node",
      "report_node",
    )

    # --- 各エージェントから司令へ ---
    # （サイト決定エージェントと評価エージェントから司令へはない）
    # .add_edge(
    #   "client_agent",
    #   "orchestrate_agent",
    # )
    .add_edge(
      "define_target_node",
      "orchestrate_node",
    )
    .add_edge(
      "research_node",
      "orchestrate_node",
    )

    # --- 終了 ---
    .add_edge(
      "report_node",
      END,
    )

    # --- グラフをコンパイル ---
    .compile()
)
