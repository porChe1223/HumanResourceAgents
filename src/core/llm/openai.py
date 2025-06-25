from langchain_openai import ChatOpenAI
from core.config.set_env import SetEnv

llm_openai = ChatOpenAI(
    model="gpt-4o-mini", # ty: ignore[unknown-argument]
    temperature=0,
    api_key=SetEnv.OPENAI_API_KEY # ty: ignore[unknown-argument]
)
