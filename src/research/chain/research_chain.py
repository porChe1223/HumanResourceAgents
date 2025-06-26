from core.state.pipeline_state import PipelineState
from research.func.research import research

def research_chain(state: PipelineState):
    """
    調査チェーン

    - スクレイピングを行う
    """
    state = research(state)
    print("-----------research_chain-------------")
    print(state)
    return state
