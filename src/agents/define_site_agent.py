from langgraph.prebuilt import create_react_agent
from llms.openai import llm_openai_4o
from tools.research.tavily_research import tavily_research
from helpers.read_text import read_text
from helpers.pretty_print_message import pretty_print_messages
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import List

"""
サイト決定エージェント
"""
define_site_agent = create_react_agent(
    name = "define_site_agent",
    model = llm_openai_4o,
    tools = [tavily_research],
    prompt = read_text("prompts/define_site_prompt.txt")
  )

# サイト情報のPydanticモデル
class Site(BaseModel):
    name: str = Field(..., description="サイト名")
    url: str = Field(..., description="サイトのURL")
    description: str = Field(..., description="サイトの説明")

class SiteList(BaseModel):
    sites: List[Site] = Field(..., title="サイトリスト")

if __name__ == "__main__":
    output_parser = PydanticOutputParser(pydantic_object=SiteList)
    format_instructions = output_parser.get_format_instructions()
    
    # プロンプトにformat_instructionsを埋め込む（promptの内容に応じて要調整）
    user_input = read_text("prompts/user_input_samples/llm_developer.txt")
    prompt = read_text("prompts/define_site_prompt.txt") + f"\n{format_instructions}"
    
    for chunk in define_site_agent.stream(
        {"messages": [{"role": "user", "content": user_input}]}
    ):
        try:
            # chunk["content"]など、実際の出力構造に応じて修正
            parsed = output_parser.invoke(chunk["content"])
            print(parsed.sites)  # Pythonリストとして出力
        except Exception as e:
            print("Parse error:", e)
            print(chunk)

