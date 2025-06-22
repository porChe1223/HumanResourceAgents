from langgraph.prebuilt import create_react_agent
from llms.openai import llm_openai
from tools.research.tavily_research import tavily_research
from helpers.print.pretty_print_message import pretty_print_messages
from helpers.read_txt import read_txt

"""
調査対象決定エージェント
"""
define_target_agent = create_react_agent(
    name = "define_target_agent",
    model = llm_openai,
    tools = [tavily_research],
    prompt = (
        "You are a research target agent.\n\n"
        "INSTRUCTIONS:\n"
        "- Assist ONLY with research-related tasks, DO NOT do any other tasks\n"
        "- 要件に対してどのようなスキル・経験が必要か調べて\n"
        "- そのスキル名・経験名だけを教えて。\n"
        "- Respond ONLY with the results of your work, do NOT include ANY other text."
      )
  )

if __name__ == "__main__":
  for chunk in define_target_agent.stream(
    {"messages": [{"role": "user", "content": read_txt("tests/llm_developer/application_requirements.txt")}]}
):
    pretty_print_messages(chunk)

