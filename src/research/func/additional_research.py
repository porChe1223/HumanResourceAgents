import ast
import json
from langchain_core.messages import HumanMessage
from core.state.pipeline_state import PipelineState
from core.state.research_state import ResearchState
from core.helper.runnable_retry import runnable_retry
from research.agent.data_shape_agent import data_shape_agent
from research.agent.select_additional_site_agent import select_additional_site_agent
from research.agent.additional_research_agent import additional_research_agent
from research.helper.beautiful_soup_scrape import beautiful_soup_scrape

def additional_research(state: PipelineState, research_state: ResearchState):
    """
    追加調査ノード

    - 調査結果をJSON形式に変換
    - 各ユーザに関する追加のサイトを選択
    - 追加のサイトを調査
    """
    # --- 調査結果を取得 ---
    researchs = state["researchs"]
    print("-----------research_result--------------")
    print(researchs)

    # --- 調査結果を整形 ---
    shaped_researchs = runnable_retry(data_shape_agent).invoke(HumanMessage(content=researchs))
    shaped_researchs = json.loads(shaped_researchs["messages"][-1].content)
    print("-----------shaped_researchs--------------")
    print(shaped_researchs)

    # --- ユーザリストを取得 ---
    person_list = list(shaped_researchs.keys())
    print("-----------person_list--------------")
    print(person_list)

    # --- 各ユーザに関する追加調査 ---
    for person in person_list:
        print("-----------person--------------")
        print(person)
        # 追加サイトを選択
        additional_sites = runnable_retry(select_additional_site_agent).invoke(HumanMessage(content=person))
        print("-----------additional_sites--------------")
        print(additional_sites)
        url_list = ast.literal_eval(additional_sites["messages"][-1].content) if isinstance(additional_sites["messages"][-1].content, str) else additional_sites["messages"][-1].content
        print("-----------url_list--------------")
        print(url_list)
        for url in url_list:
            # スクレイピング
            print("-----------url--------------")
            print(url)
            scrape_result = beautiful_soup_scrape(url)
            print("-----------scrape_result--------------")
            print(scrape_result)
            # 調査エージェントを呼び出す
            research_result = runnable_retry(additional_research_agent).invoke(HumanMessage(content=scrape_result))
            print("-----------research_result--------------")
            print(research_result)
            # 調査結果を追加
            shaped_researchs[person] += "ああああああああ"
            shaped_researchs[person] +=  research_result["messages"][-1].content
            print("-----------shaped_researchs_later--------------")
            print(shaped_researchs)




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
    
