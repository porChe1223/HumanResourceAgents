from langgraph.prebuilt import create_react_agent
from llms.openai import llm_openai_4o
from tools.research.tavily_research import tavily_research
from helpers.read_text import read_text
from helpers.pretty_print_message import pretty_print_messages

"""
調査対象決定エージェント
"""
define_target_agent = create_react_agent(
    name = "define_target_agent",
    model = llm_openai_4o,
    tools = [tavily_research],
    prompt = read_text("prompts/define_target_prompt.txt")
  )

if __name__ == "__main__":
  for chunk in define_target_agent.stream(
    {"messages": [{"role": "user", "content": read_text("prompts/user_input_samples/llm_developer.txt")}]}
):
    pretty_print_messages(chunk)

