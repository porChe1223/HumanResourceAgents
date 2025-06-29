from langgraph.prebuilt import create_react_agent
from core.llm.openai import llm_openai
from shared.helper.read_text import read_text

"""
追加調査エージェント

- スクレイピング結果から、人材に関する追加情報情報を取得する
"""
additional_research_agent = create_react_agent(
    name = "additional_research_agent",
    model = llm_openai,
    tools = [],
    prompt = read_text("research/prompt/additional_research_prompt.txt")
)
