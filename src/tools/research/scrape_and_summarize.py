from langchain_core.tools import tool
from langchain_core.prompts import ChatPromptTemplate
from llms.openai import llm_openai
from tools.scraping.beautiful_soup_scraping import beautiful_soup_scraping
from langchain_core.pydantic_v1 import BaseModel, Field

# --- LLM Chain ---
summarizer_prompt = ChatPromptTemplate.from_template(
    "You are a summarization expert. Your task is to create a concise summary of the provided text chunks based on the user's original request.\n\n"
    "USER REQUEST:\n"
    "{request}\n\n"
    "TEXT CHUNKS:\n"
    "{chunks}\n\n"
    "Focus on extracting information that directly answers the user's request and ignore irrelevant details. "
    "The summary should be objective and informative."
)
summarizer_chain = summarizer_prompt | llm_openai

class ScrapeAndSummarizeArgs(BaseModel):
    url: str = Field(description="The URL of the website to scrape.")
    request: str = Field(description="The user's original request to guide the summarization.")

@tool("scrape_and_summarize", args_schema=ScrapeAndSummarizeArgs)
def scrape_and_summarize(url: str, request: str) -> str:
    """
    Scrapes a website, summarizes the content based on the user's request, and returns the summary.
    This tool is useful when you need to process a large amount of text from a webpage and extract only the relevant information.
    """
    # Scrape the website to get text chunks
    chunks = beautiful_soup_scraping.invoke(url)
    
    if not chunks or (len(chunks) == 1 and "Error" in chunks[0]):
        return "Failed to retrieve content from the website."
        
    # Join chunks for summarization
    document = "\n\n---\n\n".join(chunks)
    
    # Summarize the content
    summary = summarizer_chain.invoke({
        "request": request,
        "chunks": document
    })
    
    return summary.content 
