from langgraph.graph import StateGraph, MessagesState, START, END
from orchestrate.chain.orchestrate_chain import orchestrate_chain
from strategy.chain.strategy_chain import strategy_chain
from research.chain.research_chain import research_chain
from recommend.chain.recommend_chain import recommend_chain

"""
LangGraphのワークフローグラフを定義
"""
pipeline = (
    # --- パイプラインを定義 ---
    StateGraph(MessagesState)

    # --- チェーンを定義 ---
    .add_node(
      orchestrate_chain,
      destinations=(
        "strategy_chain",                             # 司令 => 戦略決定
        "recommend_chain",                            # 司令 => 推薦
      )
    )
    .add_node(strategy_chain)
    .add_node(research_chain)
    .add_node(recommend_chain)

    # --- チェーンを接続 ---
    .add_edge(START, "orchestrate_chain")             # 開始     =>  司令
    .add_edge("strategy_chain", "research_chain")     # 戦略決定  =>  調査
    .add_edge("research_chain", "orchestrate_chain")  # 調査     =>  司令
    .add_edge("recommend_chain", END)                 # 推薦     =>  終了

    # --- コンパイル ---
    .compile()
)
