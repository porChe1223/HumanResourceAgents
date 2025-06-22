from langgraph.prebuilt import create_react_agent
from llms.openai import llm_openai
from tools.assign_agents import(
  assign_to_define_research_target_node,
  assign_to_define_research_strategy_node,
  assign_to_scrape_and_chunk_node,
  assign_to_score_node,
)
from helpers.pretty_print_message import pretty_print_messages

"""
司令エージェント
"""
# LangGraph agentとして定義
orchestrate_agent = create_react_agent(
    name = "orchestrate_agent",
    model = llm_openai,
    tools = [
      assign_to_define_research_target_node,
      assign_to_define_research_strategy_node,
      assign_to_scrape_and_chunk_node,
      assign_to_score_node,
    ],
    prompt = (
      "You are an orchestrator agent.\n\n"
      "INSTRUCTIONS:\n"
      "- 受け取ったデータから次のワークフローステージを判定しなさい。\n"
      "- 必ずassign_to_workflow_stageツールを使って、次のステージを返しなさい。\n"
      "WORKFLOW:\n"
      "以下の順番にワークフローを進めてください。\n"
      "1. define_target_node: 調査対象を定義する。\n"
      "2. define_site_node: 調査サイトを定義する。\n"
      "3. scrape_and_chunk_node: サイトをスクレイピングして、コンテンツをチャンクに分割する。\n"
      "4. score_node: 調査結果を評価する。\n"
      "assign_to_score_nodeは最後のみで使用して"
      "- ステージ名は、define_target_node, define_site_node, scrape_and_chunk_node, score_nodeのいずれかを返しなさい。\n"
    )
)

if __name__ == "__main__":
    for chunk in orchestrate_agent.stream(
      {"messages": [{"role": "user", "content": "次はdefine_target"}]}
    ):
      pretty_print_messages(chunk)
