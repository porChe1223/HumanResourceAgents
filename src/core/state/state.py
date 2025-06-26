from langgraph.graph import MessagesState

class State(MessagesState):
    user_input: str = ""  # ユーザ入力
    skills: str = ""      # スキル
    sites: list[str] = [] # サイト
