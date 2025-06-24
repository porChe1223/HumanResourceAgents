from langgraph.types import Command
from langchain_core.messages import HumanMessage
from core.helper.runnable_retry import runnable_retry
from orchestrate.agent.orchestrate_agent import orchestrate_agent


def orchestrate_chain(state):
    """
    司令チェーン

    - 司令エージェントを呼び出し、パイプラインのステップを決定する
    """
    result = runnable_retry(orchestrate_agent).invoke(state)

    return Command(
        update={
            "messages": [
                HumanMessage(content=result["messages"][-1].content, name="orchestrate_chain")
            ]
        },
    )
