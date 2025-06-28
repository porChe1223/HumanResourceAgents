from langgraph.prebuilt import create_react_agent
from core.llm.openai import llm_openai
from shared.helper.read_text import read_text

"""
JSON変換エージェント

- スクレイピング結果から人材の情報を取得
- 人材の情報をJSON形式に変換する
- 重複している人材はまとめる
"""
parse_json_agent = create_react_agent(
    name = "parse_json_agent",
    model = llm_openai,
    tools = [],
    prompt = read_text("research/prompt/parse_json_prompt.txt")
)
