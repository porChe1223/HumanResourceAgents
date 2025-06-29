from langgraph.graph import MessagesState

class PipelineState(MessagesState):
    user_input: str = ""  # ユーザ入力
    skills: str = ""      # スキル
    sites: list[str] = [] # サイト
    researchs: str = ""   # 調査結果
