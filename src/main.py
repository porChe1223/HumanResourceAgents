import chainlit as cl
from langchain_core.messages import HumanMessage
from langchain_core.runnables import RunnableConfig
from core.pipeline.pipeline import pipeline

@cl.on_chat_start
def on_chat_start():
    # チェーンをセッションに保存
    cl.user_session.set("chain", pipeline)

@cl.on_message
async def on_message(message: cl.Message):
    config = {"configurable": {"thread_id": cl.context.session.id}}
    cb = cl.AsyncLangchainCallbackHandler()

    try:
        res = await pipeline.ainvoke(
            {"messages": [HumanMessage(content=message.content)]},
            config=RunnableConfig(callbacks=[cb], **config),
        )

        await cl.Message(content=res["messages"][-1].content).send()
        
    except Exception as e:
        await cl.Message(content=f"エラーが発生しました: {e}").send()

@cl.on_chat_resume
async def on_chat_resume(thread):
    pass
