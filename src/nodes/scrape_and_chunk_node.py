from states.workflow_state import WorkflowState
from tools.scraping.beautiful_soup_scraping import beautiful_soup_scraping

def scrape_and_chunk_node(state: WorkflowState) -> dict:
    """Webページをスクレイピングし、テキストをチャンクに分割する
    
    Args:
        state: WorkflowState
        
    Returns:
        dict: チャンクのリスト
    """
    sites = state['sites']
    all_chunks = []
    
    for site in sites:
        try:
            chunks = beautiful_soup_scraping.invoke(site)
            all_chunks.extend(chunks)

        except Exception as e:
            print(f"Error scraping {site}: {e}")

    existing_scrapes = state.get("scrapes") or []

    print(f"scrapes: {all_chunks}")
    return {"scrapes": existing_scrapes + all_chunks}
