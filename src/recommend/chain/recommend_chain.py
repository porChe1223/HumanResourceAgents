from langgraph.types import Command
from langchain_core.messages import HumanMessage
from core.helper.runnable_retry import runnable_retry
from recommend.agent.recommend_agent import recommend_agent

def recommend_chain(state):
    """
    推薦チェーン
    
    人材のスコアリングをし、推薦レポートを作成
    """
    result = runnable_retry(recommend_agent).invoke(state)

    return Command(
        update={
            "messages": [
                HumanMessage(content=result["messages"][-1].content, name="recommend_chain")
            ]
        },
    )
