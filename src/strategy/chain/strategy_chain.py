from core.state.pipeline_state import PipelineState
from strategy.func.analyze_skill import analyze_skill
from strategy.func.select_site import select_site

def strategy_chain(state: PipelineState):
    """
    戦略決定チェーン

    - 要件から必要なスキルを選択
    - スキルから必要なサイトを選択
    """
    print("-----------start-------------")
    print(state)
    print("-----------analyze_skill-------------")
    state = analyze_skill(state) # スキル選択
    print(state)
    print("-----------select_site-------------")
    state = select_site(state)   # サイト選択
    print(state)
    print("---------------------------")
    return state
