from langgraph.prebuilt import create_react_agent
from core.llm.openai import llm_openai
from shared.tool.tavily_research import tavily_research
from shared.helper.read_text import read_text


"""
戦略決定エージェント

- ユーザーの入力を受け取り、要件に合致した人材に必要そうな条件を決定
- 条件を満たす人材を探せるサイトを検索
"""
strategy_agent = create_react_agent(
    name = "strategy_agent",
    model = llm_openai,
    tools = [tavily_research],
    prompt = read_text("strategy/prompt/strategy_prompt.txt")
  )
