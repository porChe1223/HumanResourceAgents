from langgraph.graph import StateGraph, MessagesState, START, END
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
    .add_node("strategy_chain", strategy_chain)
    .add_node("research_chain", research_chain)
    .add_node("recommend_chain", recommend_chain)

    # --- チェーンを接続 ---
    .add_edge(START, "strategy_chain")             # 開始     =>  戦略決定
    .add_edge("strategy_chain", "research_chain")  # 戦略決定  =>  調査
    .add_edge("research_chain", "recommend_chain") # 調査     =>  推薦
    .add_edge("recommend_chain", END)              # 推薦     =>  終了

    # --- コンパイル ---
    .compile()
)
