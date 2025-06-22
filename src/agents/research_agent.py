from langgraph.prebuilt import create_react_agent
from llms.openai import llm_openai
from tools.research.scrape_and_summarize import scrape_and_summarize
from helpers.pretty_print_message import pretty_print_messages

"""
調査エージェント
"""
research_agent = create_react_agent(
    name = "research_agent",
    model = llm_openai,
    tools = [scrape_and_summarize],
    prompt = (
        "You are a research agent. Your goal is to investigate a topic on a given website and provide a summary.\n\n"
        "INSTRUCTIONS:\n"
        "1. You will be given a message history. Identify the user's original request or question from the beginning of the history.\n"
        "2. You will also be given a URL to a website. This is your target for research.\n"
        "3. Use the `scrape_and_summarize` tool to get a summary of the website's content. \n"
        "4. You MUST provide both the `url` and the original `request` to the tool.\n"
        "5. Respond ONLY with the summary you receive from the tool. Do not add any other text."
      )
  )

if __name__ == "__main__":
  for chunk in research_agent.stream(
    {"messages": [{"role": "user", "content": "https://webedge.jp/information/8469.html\nLLMの開発ができる人が欲しいです"}]}
):
    pretty_print_messages(chunk)
