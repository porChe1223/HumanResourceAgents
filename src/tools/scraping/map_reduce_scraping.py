from langchain_core.tools import tool
from langchain_core.documents import Document
from langchain.chains.summarize import load_summarize_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from llms.openai import llm_openai_41
from tools.scraping.beautiful_soup_scraping import beautiful_soup_scraping

@tool
def map_reduce_scraping(url: str) -> str:
    """MapReduceを使用したWebスクレイピング（トークン制限対応版）"""
    try:
        # invokeメソッドを使用してスクレイピング
        full_content = beautiful_soup_scraping.invoke({"url": url})
        
        if not full_content or len(full_content.strip()) == 0:
            return "スクレイピングできませんでした。コンテンツが空です。"
        
        # トークン制限を考慮した小さなチャンクサイズ
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=2000,  # 大幅に小さく
            chunk_overlap=200,  # オーバーラップも調整
            length_function=len,
            separators=["\n\n", "\n", "。", "、", " ", ""]
        )
        
        chunks = text_splitter.split_text(full_content)
        
        # チャンク数が多すぎる場合は最初の数個のみ使用
        if len(chunks) > 10:
            chunks = chunks[:10]
            full_content = "\n\n".join(chunks)
        
        if len(chunks) <= 1:
            return full_content[:8000]  # 長すぎる場合は切り詰め
        
        # Documentオブジェクトに変換
        docs = [Document(page_content=chunk) for chunk in chunks]
        
        # MapReduceで要約（より小さなチャンクで処理）
        summarize_chain = load_summarize_chain(
            llm=llm_openai_41,
            chain_type="map_reduce",
            map_prompt_template="以下のテキストを簡潔に要約してください：\n\n{text}",
            combine_prompt_template="以下の要約を統合して、最終的な要約を作成してください：\n\n{text}"
        )
        
        # invokeメソッドを使用して要約
        summary = summarize_chain.invoke({"input_documents": docs})
        
        # 結果の長さを制限
        summary_text = summary['output_text'][:3000] if 'output_text' in summary else str(summary)[:3000]
        first_chunk = chunks[0][:1000] if chunks else ""
        
        return f"要約: {summary_text}\n\n元のコンテンツ（一部）: {first_chunk}..."
        
    except Exception as e:
        return f"スクレイピング中にエラーが発生しました: {str(e)}" 
