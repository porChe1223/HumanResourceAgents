from langgraph.prebuilt import create_react_agent
from core.llm.openai import llm_openai
from shared.helper.read_text import read_text

"""
データ整形エージェント

- 調査結果を、人材の名前をキーにしたJSONデータに変換する
- 重複している人材はまとめる
"""
data_shape_agent = create_react_agent(
    name = "data_shape_agent",
    model = llm_openai,
    tools = [],
    prompt = read_text("research/prompt/data_shape_prompt.txt")
)
