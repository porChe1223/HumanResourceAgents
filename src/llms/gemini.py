from langchain_google_genai import ChatGoogleGenerativeAI
from config.config import Config

llm_gemini = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0,
    api_key=Config.GOOGLE_API_KEY
)
