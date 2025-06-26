import ast
from langchain_core.messages import HumanMessage
from core.state.pipeline_state import PipelineState
from core.state.research_state import ResearchState
from core.helper.runnable_retry import runnable_retry
from research.agent.research_agent import research_agent
from research.func.beautiful_soup_scrape import beautiful_soup_scrape

def research(state: PipelineState):
    """
    調査ノード

    - スクレイピングを行う
    - スクレイピング結果から人材の情報を調査
    """
    research_state = ResearchState()
    
    url_list_str = state["sites"]
    # 実際のリストに変換
    url_list = ast.literal_eval(url_list_str) if isinstance(url_list_str, str) else url_list_str
    
    final_research_result = []

    for url in url_list:
        # スクレイピング
        research_state["scrape_result"] = beautiful_soup_scrape(url)
        print("-----------scrape_result--------------")
        print(research_state["scrape_result"])
        # 調査エージェントを呼び出す
        research_result = runnable_retry(research_agent).invoke(HumanMessage(content=research_state["scrape_result"]))
        print("-----------research_result--------------")
        print(research_result)
        final_research_result.append(research_result["messages"][-1].content)

    # PipelineStateを更新
    user_input = state["user_input"]   # ユーザ入力
    skills = state["skills"]           # スキル
    sites = state["sites"]             # サイト
    researchs = final_research_result  # 最終調査結果
    print("-----------researchs--------------")
    print(researchs)
    print("--------------------------------")

    return {
        "messages": researchs,         # 全体履歴
        "user_input": user_input,  # ユーザ入力
        "skills": skills,          # スキル
        "sites": sites,            # サイト
        "researchs": researchs,    # 調査結果
    }
    

