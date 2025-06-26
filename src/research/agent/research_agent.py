from langgraph.prebuilt import create_react_agent
from core.llm.openai import llm_openai
from shared.helper.read_text import read_text

"""
調査エージェント

- スクレイピング結果から人材の情報を取得
"""
research_agent = create_react_agent(
    name = "research_agent",
    model = llm_openai,
    tools = [],
    prompt = read_text("research/prompt/research_prompt.txt")
)
