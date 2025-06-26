from langgraph.prebuilt import create_react_agent
from core.llm.openai import llm_openai
from strategy.tool.tavily_research import tavily_research
from shared.helper.read_text import read_text


"""
スキル選択エージェント

- ユーザーの入力を受け取り、要件に合致した人材に必要そうなスキルを決定
"""
skill_agent = create_react_agent(
    name = "skill_agent",
    model = llm_openai,
    tools = [tavily_research],
    prompt = read_text("strategy/prompt/skill_prompt.txt")
  )
