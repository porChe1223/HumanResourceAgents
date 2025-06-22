from bs4 import BeautifulSoup
import re
from langchain_text_splitters import CharacterTextSplitter

def clean_and_split_text(soup: BeautifulSoup) -> list[str]:
    """HTMLから不要な要素を削除してメインコンテンツのみを抽出し、テキストを分割する関数。
    
    Args:
        soup (BeautifulSoup): BeautifulSoupオブジェクト
        
    Returns:
        list[str]: 分割されたテキストのリスト
    """
    # --- 不要なタグを削除 ---
    unwanted_tags = [
        'script', 'style', 'nav', 'header', 'footer', 'aside', 
        'noscript', 'iframe', 'embed', 'object', 'form', 'img'
    ]
    
    for tag in unwanted_tags:
        for element in soup.find_all(tag):
            element.decompose()
    
    # --- 不要なクラス名やID要素を削除 ---
    unwanted_patterns = [
        'advertisement', 'ad-', 'ads', 'banner', 'popup', 'modal',
        'sidebar', 'menu', 'navigation', 'breadcrumb', 'social',
        'share', 'comment', 'related', 'recommend', 'footer',
        'header', 'cookie', 'privacy'
    ]
    
    for pattern in unwanted_patterns:
        # クラス名で検索
        for element in soup.find_all(class_=re.compile(pattern, re.IGNORECASE)):
            element.decompose()
        # ID名で検索
        for element in soup.find_all(id=re.compile(pattern, re.IGNORECASE)):
            element.decompose()
    
    # --- 空のタグや改行のみのタグを削除 ---
    for element in soup.find_all():
        if not element.get_text(strip=True):
            element.decompose()
    
    # --- テキストのみを抽出 ---
    text = soup.get_text(separator=' ', strip=True)

    # --- 複数空白を1つに ---
    text = re.sub(r'\s+', ' ', text)

    # --- 複数改行を1つに ---
    text = re.sub(r'\n+', '\n', text)

    # --- テンプレートタグを削除 ---
    text = re.sub(r'\{\{.*?\}\}', '', text)

    # --- テキストを分割 ---
    text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
        encoding_name="cl100k_base", chunk_size=2000, chunk_overlap=100
    )
    texts = text_splitter.split_text(text)

    return texts
