import chainlit as cl
from langchain_core.messages import HumanMessage
from workflows.workflow import workflow
from langchain.schema.runnable import RunnableConfig

@cl.on_chat_start
def on_chat_start():
    # チェーンをセッションに保存
    cl.user_session.set("chain", workflow)

@cl.on_message
async def on_message(msg: cl.Message):
    config = {"configurable": {"thread_id": cl.context.session.id}}
    # cb = cl.LangchainCallbackHandler()  # 一旦外す

    final_answer = cl.Message(content="")

    for msg, metadata in workflow.stream(
        {"messages": [HumanMessage(content=msg.content)]},
        stream_mode="messages",
        config=RunnableConfig(**config),  # callbacksを渡さない
    ):
        if (
            msg.content
            and not isinstance(msg, HumanMessage)
            and metadata.get("langgraph_node") == "agent"
        ):
            await final_answer.stream_token(msg.content)

    await final_answer.send()


