from langgraph.prebuilt import create_react_agent
from llms.openai import llm_openai
from tools.scraping.beautiful_soup_scraping import beautiful_soup_scraping
from helpers.pretty_print_message import pretty_print_messages

"""
調査エージェント
"""
research_agent = create_react_agent(
    name = "research_agent",
    model = llm_openai,
    tools = [beautiful_soup_scraping],
    prompt = (
        "You are a research agent.\n\n"
        "INSTRUCTIONS:\n"
        "- Assist ONLY with research-related tasks, DO NOT do any other tasks\n"
        "- 調査対象のサイトから情報をスクレイピングして\n"
        "- その情報をもとに目的の情報を探して\n"
        "- Respond ONLY with the results of your work, do NOT include ANY other text."
      )
  )

if __name__ == "__main__":
  for chunk in research_agent.stream(
    {"messages": [{"role": "user", "content": "https://webedge.jp/information/8469.html\nLLMの開発ができる人が欲しいです"}]}
):
    pretty_print_messages(chunk)
