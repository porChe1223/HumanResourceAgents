from core.state.pipeline_state import PipelineState
from core.state.research_state import ResearchState
from research.func.research import research
from research.func.additional_research import additional_research

def research_chain(state: PipelineState):
    """
    調査チェーン

    - ユーザを見つけれそうなサイトで調査
    - 見つけた各ユーザに関して追加で調査
    """
    research_state = ResearchState()

    # ユーザを見つけれそうなサイトで調査
    state, research_state = research(state, research_state)
    print("-----------research_chain-------------")
    print(state)
    print(research_state)

    # 見つけた各ユーザに関して追加で調査
    state = additional_research(state, research_state)
    print("-----------additional_research-------------")
    print(state)


    return state
