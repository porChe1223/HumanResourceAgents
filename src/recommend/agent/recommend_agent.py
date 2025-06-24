from langgraph.prebuilt import create_react_agent
from core.llm.openai import llm_openai
from shared.helper.read_text import read_text


"""
推薦エージェント

- 人材のスコアリングをし、推薦レポートを作成
- 人材のスコアリングをし、推薦レポートを作成
"""
recommend_agent = create_react_agent(
    name = "recommend_agent",
    model = llm_openai,
    tools = [],
    prompt = read_text("recommend/prompt/recommend_prompt.txt")
  )
