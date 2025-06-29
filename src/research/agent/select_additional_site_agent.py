from langgraph.prebuilt import create_react_agent
from core.llm.openai import llm_openai
from strategy.tool.tavily_research import tavily_research
from shared.helper.read_text import read_text

"""
追加サイト選択エージェント
- 各ユーザに関する追加のサイトを選択する
"""
select_additional_site_agent = create_react_agent(
    name = "select_additional_site_agent",
    model = llm_openai,
    tools = [tavily_research],
    prompt = read_text("research/prompt/select_additional_site_prompt.txt")
)
