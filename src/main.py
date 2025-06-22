import chainlit as cl
from langchain_core.messages import HumanMessage
from workflows.workflow import workflow

@cl.on_chat_start
def on_chat_start():
    # チェーンをセッションに保存
    cl.user_session.set("chain", workflow)

@cl.on_message
async def on_chat_message(message: cl.Message):
    # チェーンを取得
    chain = cl.user_session.get("chain")

    try:
        # チェーンを呼び出し
        res = await chain.ainvoke(
            {"messages": [HumanMessage(content=message.content)]},
            config={"callbacks": [cl.AsyncLangchainCallbackHandler()]},
        )

        # チェーンの応答を送信
        await cl.Message(content=res["messages"][-1].content).send()

        # pretty_print_message(res) # resはグラフの最終状態であり、単一メッセージではないため、この関数は期待通りに動作しません。
    except Exception as e:
        # リトライが最終的に失敗した場合、エラーをターミナルとUIに表示します
        error_message = f"エラーが発生しました: \n{e}"
        print(f"最終的なエラー: \n{error_message}")
        await cl.Message(content=error_message).send()


