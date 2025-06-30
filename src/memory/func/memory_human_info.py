from core.state.pipeline_state import PipelineState
from memory.helper.handle_dynamo_db import DynamoDBHandler
# from shared.helper.read_text import read_text

def memory_human_info(state: PipelineState):
    """
    人材情報保存ノード

    - 人材情報をDynamoDBに保存
    """
    # --- DynamoDBのインスタンス ---
    dynamo_db_handler = DynamoDBHandler(table_name='human_resources', region_name='ap-northeast-1')

    # --- 人材情報を取得 ---
    human_data = state["researchs"]
    # human_data = read_text("../docs/sample/additional_research/additional_research_result.txt")
    print("-----------human_data--------------")
    print(human_data)
    print(type(human_data))
    
    # Python辞書型に変換
    if isinstance(human_data, str):
        try:
            human_data = "{" + human_data + "}"
            human_data = eval(human_data)
            print("-----------human_data--------------")
            print(human_data)
            print(type(human_data))
        except (ValueError, SyntaxError) as e:
            print(f"辞書変換エラー: {e}")
            return state
    
    
    # --- 人材情報を保存 ---
    dynamo_db_handler.put_items(human_data)

    return state
