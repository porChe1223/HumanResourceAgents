from langgraph.prebuilt import create_react_agent
from core.llm.openai import llm_openai
from orchestrate.tool.assign_strategy_chain import assign_strategy_chain
from orchestrate.tool.assign_recommend_chain import assign_recommend_chain
from shared.helper.read_text import read_text

"""
司令エージェント

- パイプラインのステップを決定
"""
# LangGraph agentとして定義
orchestrate_agent = create_react_agent(
    name = "orchestrate_agent",
    model = llm_openai,
    tools = [
        assign_strategy_chain,
        assign_recommend_chain,
    ],
    prompt = read_text("orchestrate/prompt/orchestrate_prompt.txt")
)
