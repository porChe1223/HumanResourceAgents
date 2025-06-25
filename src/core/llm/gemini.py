from langchain_google_genai import ChatGoogleGenerativeAI
from core.config.set_env import SetEnv

llm_gemini = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0,
    api_key=SetEnv.GOOGLE_API_KEY
)
