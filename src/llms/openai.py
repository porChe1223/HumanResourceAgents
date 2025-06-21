from langchain_openai import ChatOpenAI
from config.config import Config

llm_openai = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
    api_key=Config.OPENAI_API_KEY
)
