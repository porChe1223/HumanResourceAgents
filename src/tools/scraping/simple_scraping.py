from langchain_core.tools import tool
from tools.scraping.beautiful_soup_scraping import beautiful_soup_scraping

@tool
def simple_scraping(url: str) -> str:
    """シンプルなWebスクレイピング（トークン制限対応版）"""
    try:
        # invokeメソッドを使用してスクレイピング
        full_content = beautiful_soup_scraping.invoke({"url": url})
        
        if not full_content or len(full_content.strip()) == 0:
            return "スクレイピングできませんでした。コンテンツが空です。"
        
        # トークン制限を考慮して長さを制限（約4000トークン相当）
        max_length = 12000  # 文字数で制限
        if len(full_content) > max_length:
            # 重要な部分を保持するため、最初と最後の部分を取得
            first_part = full_content[:max_length//2]
            last_part = full_content[-(max_length//2):]
            truncated_content = first_part + "\n\n... (中略) ...\n\n" + last_part
            return truncated_content
        
        return full_content
        
    except Exception as e:
        return f"スクレイピング中にエラーが発生しました: {str(e)}" 
