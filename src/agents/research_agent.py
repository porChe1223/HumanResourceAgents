from langgraph.prebuilt import create_react_agent
from llms.openai import llm_openai
from helpers.pretty_print_message import pretty_print_messages

"""
調査エージェント
"""
research_agent = create_react_agent(
    name = "research_agent",
    model = llm_openai,
    tools = [],
    prompt = (
        "あなたは、与えられたテキストの断片（チャンク）を分析する専門の調査エージェントです。\n"
        "ユーザーの要求に合致する情報がチャンクに含まれているかを判断してください。\n\n"
        "INSTRUCTIONS:\n"
        "- テキストチャンクと、元のユーザー要求が渡されます。\n"
        "- テキストチャンクを注意深く読み、ユーザー要求に直接関連する情報のみを抽出してください。\n"
        "- 関連情報が見つかった場合は、その情報のみを返してください。余計な挨拶や説明は不要です。\n"
        "- チャンクに関連情報が含まれていない場合は、'UNRELATED'という文字列だけを返してください。"
      )
  )

if __name__ == "__main__":
  for chunk in research_agent.stream(
    {"messages": [{"role": "user", "content": "https://webedge.jp/information/8469.html\nLLMの開発ができる人が欲しいです"}]}
):
    pretty_print_messages(chunk)
