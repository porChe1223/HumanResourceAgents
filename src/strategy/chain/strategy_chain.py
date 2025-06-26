from langgraph.types import Command
from langchain_core.messages import HumanMessage
from core.helper.runnable_retry import runnable_retry
from strategy.agent.skill_agent import skill_agent
from strategy.agent.site_agent import site_agent

def strategy_chain(state):
    """
    戦略決定チェーン

    - 要件から必要なスキルを選択
    - スキルから必要なサイトを選択
    """
    skills = runnable_retry(skill_agent).invoke(state)
    sites = runnable_retry(site_agent).invoke(state)

    return Command(
        update={
            "skills": skills,
            "sites": sites
        },
    )
