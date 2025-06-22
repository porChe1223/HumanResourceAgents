from states.workflow_state import WorkflowState
from langchain_core.messages import AIMessage

def assemble_node(state: WorkflowState) -> dict:
    """並列調査の結果を集約する
    
    Args:
        state: WorkflowState
        
    Returns:
        dict: 調査結果のリスト
    """
    researches = state['researches']
    
    relevant_info = [res for res in researches if "UNRELATED" not in res]
            
    if not relevant_info:
        summary = "Webサイトを調査しましたが、ユーザーの要求に関連する情報は見つかりませんでした。"
    else:
        summary = "\n".join(relevant_info)
        
    return {"messages": [AIMessage(content=summary)]}
