import requests
from bs4 import BeautifulSoup
from tenacity import retry, stop_after_attempt, wait_fixed
from research.helper.clean_html import clean_html

def beautiful_soup_scrape(url: str) -> str:
    """BeautifulSoupでWebスクレイピングする関数。
    
    Args:
        url (str): スクレイピング対象のURL
        
    Returns:
        result (str): スクレイピング結果
    """
    # スクレイピングブロック対策として、ユーザーエージェントを設定
    ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    headers = {'User-Agent': ua}

    # リトライ処理
    @retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
    def scrape_with_retry():
        # Webページにアクセス
        response = requests.get(url, headers=headers)
        response.encoding = response.apparent_encoding  # 文字化け回避

        # BeautifulSoupでスクレイピング
        soup = BeautifulSoup(response.text, "html.parser")
        result = clean_html(soup)
        return result
    
    return scrape_with_retry()
