from langgraph.prebuilt import create_react_agent
from llms.openai import llm_openai
from tools.research.tavily_research import tavily_research
from helpers.read_text.read_text import read_text
from helpers.log.pretty_print_message import pretty_print_messages

"""
サイト決定エージェント
"""
define_site_agent = create_react_agent(
    name = "define_site_agent",
    model = llm_openai,
    tools = [tavily_research],
    prompt = (
        "You are a site decision agent.\n\n"
        "INSTRUCTIONS:\n"
        "- Assist ONLY with site-related tasks, DO NOT do any other tasks\n"
        "- あなたはスキルを渡されます。\n"
        "- そのスキルを持った人の情報を見つけれそうなサイトを調べて\n"
        "- どのサイトでそのスキルを持った人の情報を見つけれそうかを調べて\n"
        "- 人材サイトや論文のサイトをメインに調べてください\n"
        "- 人材サイトは募集要項ではなくユーザプロフィールの方を調べてください\n"
        "- 困ったらResearchMapやKakenでも良いです\n"
        "- 必要であればニュースサイトも調べて良いです\n"
        "- ブログは調べないでください\n"
        "IMPORTANT:\n"
        "- 目的はそのスキルを持った人を見つけることです\n"
        "- 調査結果は、サイトのリンクだけを教えて。\n"
        "- 1つだけ返して。\n"
        # "- Pythonのリスト形式で返してください。\n"
        # "- 例: ['https://www.google.com', 'https://www.yahoo.co.jp']\n"
        "- 他のテキストは一切含めないでください\n"
        "- Respond ONLY with the results of your work, do NOT include ANY other text."
      )
  )

if __name__ == "__main__":
  for chunk in define_site_agent.stream(
    {"messages": [{"role": "user", "content": read_text("prompts/llm_developer.txt")}]}
):
    pretty_print_messages(chunk)

