from langgraph.types import Command
from langchain_core.messages import HumanMessage
from core.helper.runnable_retry import runnable_retry
from strategy.agent.strategy_agent import strategy_agent

def strategy_chain(state):
    """
    戦略決定チェーン

    - 戦略決定エージェントを呼び出す
    """
    result = runnable_retry(strategy_agent).invoke(state)

    return Command(
        update={
            "messages": [
                HumanMessage(content=result["messages"][-1].content, name="strategy_chain")
            ]
        },
    )
