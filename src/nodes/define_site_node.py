from states.workflow_state import WorkflowState
from agents.define_site_agent import define_site_agent
from helpers.runnable_retry import runnable_retry
from helpers.parse_list import parse_list

def define_site_node(state: WorkflowState) -> dict:
    """define_site_agentを呼び出し、サイトを定義する
    
    Args:
        state: WorkflowState
        
    Returns:
        dict: サイトのリスト
    """
    messages = state["messages"]
    response = runnable_retry(define_site_agent).invoke({"messages": messages[-2:]})
    sites = parse_list(response.content)

    existing_sites = state.get("sites") or []

    return {
        "messages": [response],
        "sites": existing_sites + sites,
    }
