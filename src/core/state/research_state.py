from langgraph.graph import MessagesState

class ResearchState(MessagesState):
    scrape_result: str = ""          # スクレイピング結果
    research_result: str = ""        # 調査結果
