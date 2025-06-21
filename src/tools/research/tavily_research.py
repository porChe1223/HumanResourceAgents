from langchain_tavily import TavilySearch
from langchain_core.tools import tool
from tenacity import retry, stop_after_attempt, wait_fixed

@tool
def tavily_research(query: str) -> str:
  """Tavily Search APIを使用してWeb検索を行う
  
  Args:
    query (str): 検索クエリ

  Returns:
    result (str): 検索結果のリスト
  """
  # 検索エンジン
  search = TavilySearch(max_results = 3)

  # リトライ処理
  @retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
  def research_with_retry(q):
    return search.invoke(q)
  
  return research_with_retry(query)
