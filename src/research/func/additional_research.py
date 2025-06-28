import json
from langchain_core.messages import HumanMessage
from core.state.pipeline_state import PipelineState
from core.state.research_state import ResearchState
from core.helper.runnable_retry import runnable_retry
from research.agent.parse_json_agent import parse_json_agent
from research.agent.select_additional_site_agent import select_additional_site_agent

def additional_research(state: PipelineState, research_state: ResearchState):
    """
    追加調査ノード

    - 調査結果をJSON形式に変換
    - 各ユーザに関する追加のサイトを選択
    - 追加のサイトを調査
    """
    research_result = research_state["researchs"]
    print("-----------research_result--------------")
    print(research_result)

    research_result_json = runnable_retry(parse_json_agent).invoke(HumanMessage(content=research_result))
    print("-----------research_result_json--------------")
    print(research_result_json)


    # State更新用
    user_input = state["user_input"]               # ユーザ入力
    skills = state["skills"]                       # スキル
    sites = state["sites"]                         # サイト
    researchs = research_state["researchs"]        # 調査結果

    return {
        "messages": researchs,     # 全体履歴
        "user_input": user_input,  # ユーザ入力
        "skills": skills,          # スキル
        "sites": sites,            # サイト
        "researchs": researchs,    # 調査結果
    }
    
