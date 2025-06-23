from langchain_core.tools import tool
from tools.scraping.beautiful_soup_scraping import beautiful_soup_scraping
from llms.openai import llm_openai_4o
import re

@tool
def smart_scraping(url: str, search_purpose: str = "") -> str:
    """スマートなWebスクレイピング（目的に応じた情報抽出）"""
    try:
        # スクレイピング実行
        full_content = beautiful_soup_scraping.invoke({"url": url})
        
        if not full_content or len(full_content.strip()) == 0:
            return "スクレイピングできませんでした。コンテンツが空です。"
        
        # 検索目的に基づいて重要な部分を抽出
        if search_purpose:
            # 目的に関連する部分を特定
            relevant_content = extract_relevant_content(full_content, search_purpose)
            if relevant_content:
                return relevant_content
        
        # 目的が指定されていない場合は、構造化された要約を返す
        return create_structured_summary(full_content)
        
    except Exception as e:
        return f"スクレイピング中にエラーが発生しました: {str(e)}"

def extract_relevant_content(content: str, purpose: str) -> str:
    """目的に応じて関連コンテンツを抽出"""
    try:
        # 目的に基づくキーワード抽出
        keywords = extract_keywords_from_purpose(purpose)
        
        # 関連性の高い段落を抽出
        paragraphs = content.split('\n\n')
        relevant_paragraphs = []
        
        for paragraph in paragraphs:
            if any(keyword.lower() in paragraph.lower() for keyword in keywords):
                relevant_paragraphs.append(paragraph)
        
        if relevant_paragraphs:
            # 関連段落を結合（トークン制限内に収める）
            result = '\n\n'.join(relevant_paragraphs)
            if len(result) > 8000:
                result = result[:8000] + "... (関連部分のみ表示)"
            return result
        
        return ""
        
    except Exception:
        return ""

def extract_keywords_from_purpose(purpose: str) -> list:
    """目的からキーワードを抽出"""
    # 人材検索に関連するキーワード
    hr_keywords = [
        "スキル", "経験", "実績", "プロジェクト", "技術", "開発", "エンジニア",
        "研究者", "論文", "発表", "業績", "職歴", "経歴", "専門", "分野",
        "LLM", "AI", "機械学習", "自然言語処理", "プログラミング", "コード",
        "GitHub", "研究", "開発", "実装", "設計", "アーキテクチャ"
    ]
    
    # 目的に含まれるキーワードを抽出
    found_keywords = []
    for keyword in hr_keywords:
        if keyword in purpose:
            found_keywords.append(keyword)
    
    # 目的に含まれる一般的なキーワードも追加
    general_keywords = re.findall(r'\w+', purpose.lower())
    found_keywords.extend(general_keywords[:5])  # 最初の5個
    
    return found_keywords

def create_structured_summary(content: str) -> str:
    """構造化された要約を作成"""
    try:
        # 基本的な構造化
        lines = content.split('\n')
        structured_content = []
        
        # 見出しや重要な部分を特定
        for line in lines:
            line = line.strip()
            if line and len(line) > 10:  # 意味のある行のみ
                # 見出しっぽい行を特定
                if len(line) < 100 and (line.endswith('：') or line.endswith(':') or 
                                       'について' in line or 'とは' in line):
                    structured_content.append(f"【{line}】")
                else:
                    structured_content.append(line)
        
        result = '\n'.join(structured_content)
        
        # トークン制限内に収める
        if len(result) > 8000:
            # 重要な部分を保持
            important_parts = []
            current_length = 0
            
            for line in structured_content:
                if current_length + len(line) < 8000:
                    important_parts.append(line)
                    current_length += len(line)
                else:
                    break
            
            result = '\n'.join(important_parts) + "\n\n... (続きは省略)"
        
        return result
        
    except Exception:
        return content[:8000] + "..." if len(content) > 8000 else content 
