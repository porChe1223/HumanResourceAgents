from langchain_core.tools import tool
from tools.scraping.beautiful_soup_scraping import beautiful_soup_scraping
import re
from urllib.parse import urljoin, urlparse

@tool
def multi_page_scraping(base_url: str, search_purpose: str = "", max_pages: int = 3) -> str:
    """複数ページのWebスクレイピング（効率的な情報収集）"""
    try:
        # メインページをスクレイピング
        main_content = beautiful_soup_scraping.invoke({"url": base_url})
        
        if not main_content:
            return "メインページのスクレイピングに失敗しました。"
        
        # 関連ページのURLを抽出
        related_urls = extract_related_urls(base_url, main_content, search_purpose)
        
        # 結果を統合
        all_content = [main_content]
        
        # 関連ページをスクレイピング（制限付き）
        for i, url in enumerate(related_urls[:max_pages-1]):  # メインページを除く
            try:
                page_content = beautiful_soup_scraping.invoke({"url": url})
                if page_content:
                    all_content.append(f"\n\n=== 関連ページ {i+1}: {url} ===\n{page_content}")
            except Exception as e:
                continue  # エラーが発生しても続行
        
        # 統合されたコンテンツを処理
        combined_content = "\n\n".join(all_content)
        
        # 目的に応じた情報抽出
        if search_purpose:
            relevant_content = extract_relevant_from_multiple(combined_content, search_purpose)
            if relevant_content:
                return relevant_content
        
        # 構造化された要約を返す
        return create_multi_page_summary(combined_content, base_url)
        
    except Exception as e:
        return f"マルチページスクレイピング中にエラーが発生しました: {str(e)}"

def extract_related_urls(base_url: str, content: str, purpose: str) -> list:
    """関連ページのURLを抽出"""
    try:
        # 人材関連のキーワードを含むリンクを探す
        hr_keywords = [
            "採用", "求人", "募集", "人材", "メンバー", "チーム", "プロフィール",
            "研究者", "エンジニア", "開発者", "実績", "業績", "論文", "発表"
        ]
        
        # 目的に含まれるキーワードも追加
        purpose_keywords = re.findall(r'\w+', purpose)
        all_keywords = hr_keywords + purpose_keywords
        
        # リンクパターンを検索（簡易版）
        link_patterns = [
            r'https?://[^\s<>"]+',
            r'/[^\s<>"]*\.html',
            r'/[^\s<>"]*\.php',
            r'/[^\s<>"]*\.asp'
        ]
        
        found_urls = []
        for pattern in link_patterns:
            urls = re.findall(pattern, content)
            for url in urls:
                # 同じドメインのURLのみ
                if is_same_domain(base_url, url):
                    # キーワードを含むURLを優先
                    if any(keyword in url.lower() for keyword in all_keywords):
                        found_urls.append(url)
        
        return list(set(found_urls))[:5]  # 重複除去して最大5個
        
    except Exception:
        return []

def is_same_domain(base_url: str, url: str) -> bool:
    """同じドメインかチェック"""
    try:
        base_domain = urlparse(base_url).netloc
        if url.startswith('http'):
            url_domain = urlparse(url).netloc
        else:
            url_domain = urlparse(urljoin(base_url, url)).netloc
        return base_domain == url_domain
    except Exception:
        return False

def extract_relevant_from_multiple(content: str, purpose: str) -> str:
    """複数ページから関連情報を抽出"""
    try:
        # 目的に基づくキーワード抽出
        keywords = extract_keywords_from_purpose(purpose)
        
        # 関連性の高い段落を抽出
        sections = content.split('\n\n')
        relevant_sections = []
        
        for section in sections:
            if any(keyword.lower() in section.lower() for keyword in keywords):
                relevant_sections.append(section)
        
        if relevant_sections:
            # 関連セクションを結合
            result = '\n\n'.join(relevant_sections)
            if len(result) > 8000:
                result = result[:8000] + "... (関連部分のみ表示)"
            return result
        
        return ""
        
    except Exception:
        return ""

def extract_keywords_from_purpose(purpose: str) -> list:
    """目的からキーワードを抽出"""
    hr_keywords = [
        "スキル", "経験", "実績", "プロジェクト", "技術", "開発", "エンジニア",
        "研究者", "論文", "発表", "業績", "職歴", "経歴", "専門", "分野",
        "LLM", "AI", "機械学習", "自然言語処理", "プログラミング", "コード"
    ]
    
    found_keywords = []
    for keyword in hr_keywords:
        if keyword in purpose:
            found_keywords.append(keyword)
    
    general_keywords = re.findall(r'\w+', purpose.lower())
    found_keywords.extend(general_keywords[:5])
    
    return found_keywords

def create_multi_page_summary(content: str, base_url: str) -> str:
    """複数ページの構造化された要約を作成"""
    try:
        # ページごとに分割
        pages = content.split('=== 関連ページ')
        
        summary_parts = []
        
        # メインページの処理
        main_content = pages[0]
        main_summary = create_page_summary(main_content, "メインページ")
        summary_parts.append(main_summary)
        
        # 関連ページの処理
        for i, page_content in enumerate(pages[1:], 1):
            if len(summary_parts) >= 3:  # 最大3ページまで
                break
            page_summary = create_page_summary(page_content, f"関連ページ{i}")
            summary_parts.append(page_summary)
        
        result = "\n\n".join(summary_parts)
        
        # トークン制限内に収める
        if len(result) > 8000:
            result = result[:8000] + "\n\n... (要約のみ表示)"
        
        return result
        
    except Exception:
        return content[:8000] + "..." if len(content) > 8000 else content

def create_page_summary(content: str, page_name: str) -> str:
    """個別ページの要約を作成"""
    try:
        lines = content.split('\n')
        important_lines = []
        
        for line in lines:
            line = line.strip()
            if line and len(line) > 20:  # 意味のある行のみ
                # 見出しや重要な情報を特定
                if (line.endswith('：') or line.endswith(':') or 
                    'について' in line or 'とは' in line or
                    'スキル' in line or '経験' in line or '実績' in line):
                    important_lines.append(f"【{line}】")
                else:
                    important_lines.append(line)
        
        if important_lines:
            summary = f"=== {page_name} ===\n" + '\n'.join(important_lines[:10])  # 最大10行
            return summary
        
        return f"=== {page_name} ===\n(重要な情報なし)"
        
    except Exception:
        return f"=== {page_name} ===\n(エラーが発生しました)" 
