from langgraph.prebuilt import create_react_agent
from llms.openai import llm_openai
from helpers.log.pretty_print_message import pretty_print_messages

"""
評価エージェント
"""
score_agent = create_react_agent(
    name = "score_agent",
    model = llm_openai,
    tools = [],
    prompt = (
        "You are a score agent.\n\n"
        "INSTRUCTIONS:\n"
        "- Assist ONLY with score-related tasks, DO NOT do any other tasks\n"
        "- 調査結果をもとに評価を行う\n"
        "- 評価結果を教えて。\n"
        "- Respond ONLY with the results of your work, do NOT include ANY other text."
      )
  )

if __name__ == "__main__":
  for chunk in score_agent.stream(
    {"messages": [{"role": "user", "content": "ウェブエッジのサイトによると、LLM（大規模言語モデル）の開発に強い以下の企業が紹介されています\n1. **WEBEDGE**\n- サービス特徴:\n- 売上創出と業務改善の両方に重点を置いたDX化のサポートが可能。\n- 300社以上の実績あり。\n- [サービス紹介ページ](https://bansou.webedge.jp/)\n\n2. **NTT**\n- サービス特徴:\n- 薄型で高性能な日本語処理性能を持つ「tsuzumi」を開発。\n- 経済的課題を解決する、ローカル環境での利用が可能。\n- [サービス紹介ページ](https://www.rd.ntt/research/LLM_tsuzumi.html)\n\n3. **株式会社サイバーエージェント**\n- サービス特徴:\n- オープン開発による日本語LLM「CyberAgentLM」を開発。\n- 商用利用可能な対話型AIの開発も可能。\n- [サービス紹介ページ](https://www.cyberagent.co.jp/news/detail/id=30463)\n\n4. **東京大学松尾研究室**\n- サービス特徴:\n- 100億パラメータのLLM「Weblab-10B」を開発。\n- 日本語と英語のデータセットを用いている。\n- [サービス紹介ページ](https://www.t.u-tokyo.ac.jp/press/pr2023-08-18-001)\n\n5. **ストックマーク株式会社**\n- サービス特徴:\n- ビジネス用途向けの「Stockmark-13b」を開発。\n- 商用利用が可能。\n- [サービス紹介ページ](https://stockmark.co.jp/news/20231027)\n\n"}]}
):
    pretty_print_messages(chunk)
