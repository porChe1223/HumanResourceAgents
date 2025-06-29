from core.state.pipeline_state import PipelineState
from core.helper.runnable_retry import runnable_retry
from strategy.agent.analyze_skill_agent import analyze_skill_agent
# from shared.helper.read_text import read_text

def analyze_skill(state: PipelineState):
    """
    スキル分析ノード

    - 要件から必要なスキルを分析
    """
    # スキル分析エージェント
    result = runnable_retry(analyze_skill_agent).invoke(state)

    # PipelineStateを更新
    user_input = result["messages"][0]       # ユーザ入力
    skills = result["messages"][-1].content  # スキル
    # user_input = read_text("../docs/sample/user_input/llm_developer.txt")
    # skills = read_text("../docs/sample/strategy/skill_analyze_result.txt")
    sites = ""                               # サイト
    researchs = ""                           # 調査結果

    return {
        "messages": skills,        # 全体履歴
        "user_input": user_input,  # ユーザ入力
        "skills": skills,          # スキル
        "sites": sites,            # サイト
        "researchs": researchs,    # 調査結果
    }
