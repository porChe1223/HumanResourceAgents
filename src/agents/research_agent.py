from langgraph.prebuilt import create_react_agent
from llms.openai import llm_openai_4o
from tools.scraping.beautiful_soup_scraping import beautiful_soup_scraping
from helpers.read_text import read_text
from helpers.pretty_print_message import pretty_print_messages

"""
調査エージェント
"""
research_agent = create_react_agent(
    name = "research_agent",
    model = llm_openai_4o,
    tools = [beautiful_soup_scraping],
    prompt = read_text("prompts/research_prompt.txt")
  )

if __name__ == "__main__":
  for chunk in research_agent.stream(
    {"messages": [{"role": "user", "content": "https://webedge.jp/information/8469.html\nLLMの開発ができる人が欲しいです"}]}
):
    pretty_print_messages(chunk)
