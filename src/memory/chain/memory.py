from core.state.pipeline_state import PipelineState
from memory.func.memory_human_info import memory_human_info

def memory_chain(state: PipelineState):
    """
    関係性チェーン

    - 人材情報を保存
    """
    # 人材情報を保存
    state = memory_human_info(state)
    print("-----------relation_chain-------------")
    print(state)


    return state
