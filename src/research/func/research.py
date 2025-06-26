from core.state.pipeline_state import PipelineState
from research.func.beautiful_soup_scrape import beautiful_soup_scrape
import ast

def research(state: PipelineState):
    """
    調査チェーン

    - 調査エージェントを呼び出す
    """
    # スクレイピング対象のURLリスト
    url_list_str = state["sites"]
    print(url_list_str)
    # 文字列形式のリストを実際のリストに変換
    url_list = ast.literal_eval(url_list_str) if isinstance(url_list_str, str) else url_list_str
    print(url_list)
    print(type(url_list))
    print(url_list[0])
    final_research_result = beautiful_soup_scrape(url_list[0])


    # ユーザ入力
    user_input = state["user_input"]
    # スキル
    skills = state["skills"]
    # サイト
    sites = state["sites"]
    # 調査結果
    researchs = final_research_result
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
    

