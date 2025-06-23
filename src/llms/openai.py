from langchain_openai import ChatOpenAI
from config.config import Config

llm_openai_4o = ChatOpenAI(
    model="gpt-4o-mini", # ty: ignore[unknown-argument]
    temperature=0,
    api_key=Config.OPENAI_API_KEY # ty: ignore[unknown-argument]
)

llm_openai_41 = ChatOpenAI(
    model="gpt-4.1-nano", # ty: ignore[unknown-argument]
    temperature=0,
    api_key=Config.OPENAI_API_KEY # ty: ignore[unknown-argument]
)
