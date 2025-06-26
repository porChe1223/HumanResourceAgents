from langchain_core.messages import HumanMessage
from core.state.state import State
from core.helper.runnable_retry import runnable_retry
from strategy.agent.select_site_agent import select_site_agent

def select_site(state: State):
    """
    サイト選択ノード

    - 要件から必要なサイトを選択
    """
    # サイト選択エージェント
    result = runnable_retry(select_site_agent).invoke(HumanMessage(content=state["skills"]))

    # ユーザ入力
    user_input = state["user_input"]
    # スキル
    skills = state["skills"]
    # サイト
    sites = result["messages"][-1].content

    return {
        "messages": sites,         # 全体履歴
        "user_input": user_input,  # ユーザ入力
        "skills": skills,          # スキル
        "sites": sites,            # サイト
    }
