from langgraph.graph import MessagesState

class ResearchState(MessagesState):
    url_list: list[str] = []         # スクレイピング対象のURLリスト
    scrape_result: str = ""          # スクレイピング結果
    research_result: str = ""        # 調査結果
    final_research_result: str = ""  # 最終的な調査結果
