from langgraph.graph import END, StateGraph, MessagesState, START
from research.chain.research_chain import research_chain

"""
LangGraphのワークフローグラフを定義
"""
pipeline = (
    # --- パイプラインを定義 ---
    StateGraph(MessagesState)

    # --- チェーンを定義 ---
    .add_node("research_chain", research_chain)

    # --- チェーンを接続 ---
    .add_edge(START, "research_chain")
    .add_edge("research_chain", END)

    # --- コンパイル ---
    .compile()
)
