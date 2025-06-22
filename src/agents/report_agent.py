from langgraph.prebuilt import create_react_agent
from llms.gemini import llm_gemini
from helpers.pretty_print_message import pretty_print_messages

"""
レポートエージェント
"""
report_agent = create_react_agent(
    name = "report_agent",
    model = llm_gemini,
    tools = [],
    prompt = (
        "You are a report agent.\n\n"
        "INSTRUCTIONS:\n"
        "- Assist ONLY with report-related tasks, DO NOT do any other tasks\n"
        "- 受け取った全ての目ぼしいユーザに対しての調査結果のレポートを作成\n"
        "- 評価結果を受け取ったらそれも合わせたレポートを作成\n"
        "- 人事担当者向けにわかりやすいレポート生成\n"
        "- 作成したレポートを司令に報告\n"
        "- markdown形式で作成\n"
        "- Respond ONLY with the results of your work, do NOT include ANY other text."
      )
  )

if __name__ == "__main__":
  for chunk in report_agent.stream(
    {"messages": [{"role": "user", "content": "ウェブエッジのサイトによると、LLM（大規模言語モデル）の開発に強い以下の企業が紹介されています\n1. **WEBEDGE**\n- サービス特徴:\n- 売上創出と業務改善の両方に重点を置いたDX化のサポートが可能。\n- 300社以上の実績あり。\n- [サービス紹介ページ](https://bansou.webedge.jp/)\n\n2. **NTT**\n- サービス特徴:\n- 薄型で高性能な日本語処理性能を持つ「tsuzumi」を開発。\n- 経済的課題を解決する、ローカル環境での利用が可能。\n- [サービス紹介ページ](https://www.rd.ntt/research/LLM_tsuzumi.html)\n\n3. **株式会社サイバーエージェント**\n- サービス特徴:\n- オープン開発による日本語LLM「CyberAgentLM」を開発。\n- 商用利用可能な対話型AIの開発も可能。\n- [サービス紹介ページ](https://www.cyberagent.co.jp/news/detail/id=30463)\n\n4. **東京大学松尾研究室**\n- サービス特徴:\n- 100億パラメータのLLM「Weblab-10B」を開発。\n- 日本語と英語のデータセットを用いている。\n- [サービス紹介ページ](https://www.t.u-tokyo.ac.jp/press/pr2023-08-18-001)\n\n5. **ストックマーク株式会社**\n- サービス特徴:\n- ビジネス用途向けの「Stockmark-13b」を開発。\n- 商用利用が可能。\n- [サービス紹介ページ](https://stockmark.co.jp/news/20231027)\n\n"}]}
):
    pretty_print_messages(chunk)
