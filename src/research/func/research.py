import ast
from langchain_core.messages import HumanMessage
from core.state.pipeline_state import PipelineState
from core.state.research_state import ResearchState
from core.helper.runnable_retry import runnable_retry
from research.agent.research_agent import research_agent
from research.helper.beautiful_soup_scrape import beautiful_soup_scrape
from shared.helper.read_text import read_text

def research(state: PipelineState, research_state: ResearchState):
    """
    調査ノード

    - スクレイピングを行う
    - スクレイピング結果から人材の情報を調査
    """    
    url_list_str = state["sites"]
    # 実際のリストに変換
    url_list = ast.literal_eval(url_list_str) if isinstance(url_list_str, str) else url_list_str
    
    final_research_result = ""

    # for url in url_list:
    #     # スクレイピング
    #     research_state["scrape_result"] = beautiful_soup_scrape(url)
    #     print("-----------scrape_result--------------")
    #     print(research_state["scrape_result"])
    #     # 調査エージェントを呼び出す
    #     research_result = runnable_retry(research_agent).invoke(HumanMessage(content=research_state["scrape_result"]))
    #     print("-----------research_result--------------")
    #     print(research_result)
    #     final_research_result += research_result["messages"][-1].content
    #     print("-----------final_research_result--------------")
    #     print(final_research_result)

    # テスト用
    print("-----------mock_test--------------")
    final_research_result = read_text("research/prompt/sample.txt")
    research_state["research_result"] = final_research_result
    print(url_list)
    print("--------------------------------")

    # State更新用
    user_input = state["user_input"]   # ユーザ入力
    skills = state["skills"]           # スキル
    sites = state["sites"]             # サイト
    researchs = final_research_result  # 最終調査結果
    print("-----------researchs--------------")
    print(researchs)
    print("--------------------------------")

    return (
        # PipelineState更新
        {
            "messages": researchs,     # 全体履歴
            "user_input": user_input,  # ユーザ入力
            "skills": skills,          # スキル
            "sites": sites,            # サイト
            "researchs": researchs,    # 調査結果
        },
        # ResearchState更新
        {
            "messages": researchs,    # 全体履歴
            "researchs": researchs,   # 調査結果
        }
    )

    

