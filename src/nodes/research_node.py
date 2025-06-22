from states.workflow_state import WorkflowState
from agents.research_agent import research_agent
from helpers.runnable_retry import runnable_retry

def research_node(state: WorkflowState) -> dict:
    """各チャンクに対して並列で調査
    
    Args:
        state: WorkflowState
        
    Returns:
        dict: 調査結果のリスト
    """
    print(f"--- Parallel Research on {len(state['scrapes'])} chunks ---")
    user_request_content = state['messages'][-1].content
    scrapes = state['scrapes']
    
    research_tasks = [{"messages": [("user", f"Text chunk: '{chunk}'\n\nUser request: '{user_request_content}'")]} for chunk in scrapes]
    
    # 並列実行
    research_results_messages = runnable_retry(research_agent).batch(research_tasks)
    
    research_contents = [msg['messages'][-1].content for msg in research_results_messages]
    
    return {"researches": research_contents}
