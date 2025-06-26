from core.state.state import State
from core.helper.runnable_retry import runnable_retry
from strategy.agent.analyze_skill_agent import analyze_skill_agent

def analyze_skill(state: State):
    """
    スキル分析ノード

    - 要件から必要なスキルを分析
    """
    # スキル分析エージェント
    result = runnable_retry(analyze_skill_agent).invoke(state)

    # ユーザ入力
    user_input = result["messages"][0]
    # スキル
    skills = result["messages"][-1].content
    # サイト
    sites = ""

    return {
        "messages": skills,        # 全体履歴
        "user_input": user_input,  # ユーザ入力
        "skills": skills,          # スキル
        "sites": sites,            # サイト
    }
