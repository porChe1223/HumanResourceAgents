from langgraph.prebuilt import create_react_agent
from core.llm.openai import llm_openai
from research.tool.beautiful_soup_scraping import beautiful_soup_scraping
from shared.helper.read_text import read_text

"""
調査エージェント
"""
research_agent = create_react_agent(
    name = "research_agent",
    model = llm_openai,
    tools = [beautiful_soup_scraping],
    prompt = read_text("research/prompt/research_prompt.txt")
)
