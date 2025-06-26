from langgraph.graph import MessagesState

class State(MessagesState):
    skills: str
    sites: list[str]
