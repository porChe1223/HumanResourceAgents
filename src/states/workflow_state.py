from typing import Annotated, List
from typing_extensions import TypedDict
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages


class WorkflowState(TypedDict):
    """
    ワークフローの状態を管理します。

    Attributes:
        messages: これまでの会話履歴
        sites: define_site_agentによって定義されたサイトURLのリスト
        scrapes: スクレイピングされ、分割されたチャンクのリスト
        researches: research_agentによる調査結果のリスト
    """

    messages: Annotated[List[BaseMessage], add_messages]
    sites: List[str]
    scrapes: List[str]
    researches: List[str]
