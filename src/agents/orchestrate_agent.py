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
from helpers.print.pretty_print_message import pretty_print_messages

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
    prompt = (
      "You are an orchestrator agent.\n\n"
      "INSTRUCTIONS:\n"
      "- 受け取ったデータから次のワークフローステージを判定しなさい。\n"
      "- 必ずassign_to_workflow_stageツールを使って、次のステージを返しなさい。\n"
      "WORKFLOW:\n"
      "以下の順番にワークフローを進めてください。\n"
      # "1. client: クライアントの要件を定義する。\n"
      "2. define_target: 調査対象を定義する。\n"
      "3. define_site: 調査サイトを定義する。\n"
      # "4. research: 調査を行う。\n"
      "5. score: 調査結果を評価する。\n"
      # "6. report: レポートを作成する。\n"
      "assign_to_score_agentは最後のみで使用して"
      "- ステージ名は、define_research_target, define_research_strategy, scoreのいずれかを返しなさい。\n"
    )
)

if __name__ == "__main__":
    for chunk in orchestrate_agent.stream(
      {"messages": [{"role": "user", "content": "次はdefine_target"}]}
    ):
      pretty_print_messages(chunk)
