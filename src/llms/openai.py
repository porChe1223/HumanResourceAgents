from langchain_openai import ChatOpenAI
from config.config import Config

llm_openai = ChatOpenAI(
    model="gpt-4o-mini", # ty: ignore[unknown-argument]
    temperature=0,
    api_key=Config.OPENAI_API_KEY # ty: ignore[unknown-argument]
)
