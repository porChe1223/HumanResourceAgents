from langgraph.prebuilt import create_react_agent
from core.llm.openai import llm_openai
from shared.helper.read_text import read_text


"""
サイト選択エージェント

- 条件を満たす人材を探せるサイトを選択
"""
site_agent = create_react_agent(
    name = "site_agent",
    model = llm_openai,
    tools = [],
    prompt = read_text("strategy/prompt/site_prompt.txt")
  )
