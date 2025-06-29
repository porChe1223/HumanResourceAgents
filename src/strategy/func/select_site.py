from langchain_core.messages import HumanMessage
from core.state.pipeline_state import PipelineState
from core.helper.runnable_retry import runnable_retry
from strategy.agent.select_site_agent import select_site_agent
from shared.helper.read_text import read_text

def select_site(state: PipelineState):
    """
    サイト選択ノード

    - 要件から必要なサイトを選択
    """
    # サイト選択エージェント
    # result = runnable_retry(select_site_agent).invoke(HumanMessage(content=state["skills"]))

    # PipelineStateを更新
    user_input = state["user_input"]        # ユーザ入力
    skills = state["skills"]                # スキル
    # sites = result["messages"][-1].content  # サイト
    sites = read_text("../docs/sample/strategy/select_site_result.txt")
    researchs = ""                          # 調査結果

    return {
        "messages": sites,         # 全体履歴
        "user_input": user_input,  # ユーザ入力
        "skills": skills,          # スキル
        "sites": sites,            # サイト
        "researchs": researchs,    # 調査結果
    }
