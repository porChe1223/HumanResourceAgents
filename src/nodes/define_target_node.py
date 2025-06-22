from states.workflow_state import WorkflowState
from agents.define_target_agent import define_target_agent
from helpers.runnable_retry import runnable_retry

def define_target_node(state: WorkflowState) -> dict:
    """define_target_agentを呼び出す
    
    Args:
        state: WorkflowState
        
    Returns:
        dict: "messages"キーにエージェントの応答メッセージ
    """
    messages = state["messages"]
    response = runnable_retry(define_target_agent).invoke({"messages": messages[-2:]})

    return {
        "messages": response["messages"],
    }
