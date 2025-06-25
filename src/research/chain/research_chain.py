from langgraph.types import Command
from langchain_core.messages import HumanMessage
from core.helper.runnable_retry import runnable_retry
from research.agent.research_agent import research_agent

def research_chain(state):
    """
    調査チェーン

    - 調査エージェントを呼び出す
    """
    result = runnable_retry(research_agent).invoke(state)

    return Command(
        update={
            "messages": [
                HumanMessage(content=result["messages"][-1].content, name="research_chain")
            ]
        },
    )
