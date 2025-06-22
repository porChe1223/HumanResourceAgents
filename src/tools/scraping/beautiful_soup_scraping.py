from langchain_core.tools import tool
from helpers.clean_html import clean_and_split_text
import requests
from bs4 import BeautifulSoup

@tool
def beautiful_soup_scraping(url: str) -> list[str]:
    """BeautifulSoupでWebスクレイピングし、内容を分割して返す関数。
    
    Args:
        url (str): スクレイピング対象のURL
        
    Returns:
        list[str]: スクレイピング結果のテキストチャンクのリスト
    """
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=20)
        response.raise_for_status()
        
        html_content = response.content.decode('utf-8', 'ignore')
        soup = BeautifulSoup(html_content, 'html.parser')
        
        texts = clean_and_split_text(soup)
        
        return texts
    except requests.RequestException as e:
        return [f"Error scraping {url}: {e}"]
    except Exception as e:
        return [f"An unexpected error occurred: {e}"]

if __name__ == "__main__":
    result = beautiful_soup_scraping("https://researchmap.jp/press_releases/press_releases/index/633014/research_area_discipline_number:A289/sort:PressRelease.publish_start/direction:DESC/limit:10?frame_id=1601185")
    print(result)
