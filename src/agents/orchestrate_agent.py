from langgraph.prebuilt import create_react_agent
from llms.openai import llm_openai
from tools.assign_agents import(
  # assign_to_client_agent,
  assign_to_define_research_target_agent,
  assign_to_define_research_strategy_agent,
  # assign_to_research_agent,
  assign_to_score_agent,
  # assign_to_report_agent
)
from helpers.read_text import read_text
from helpers.pretty_print_message import pretty_print_messages

"""
司令エージェント
"""
# LangGraph agentとして定義
orchestrate_agent = create_react_agent(
    name = "orchestrate_agent",
    model = llm_openai,
    tools = [
      # assign_to_client_agent,
      assign_to_define_research_target_agent,
      assign_to_define_research_strategy_agent,
      # assign_to_research_agent,
      assign_to_score_agent,
      # assign_to_report_agent
    ],
    prompt = read_text("prompts/orchestrate_prompt.txt")
)

if __name__ == "__main__":
    for chunk in orchestrate_agent.stream(
      {"messages": [{"role": "user", "content": "次はdefine_target"}]}
    ):
      pretty_print_messages(chunk)
