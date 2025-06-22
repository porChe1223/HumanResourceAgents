from openai import RateLimitError
from google.api_core.exceptions import ResourceExhausted
from langchain_core.runnables import Runnable


def runnable_retry(runnable: Runnable) -> Runnable:
    """
    LangChainのRunnableにリトライ処理を追加

    例外の種類:
    - OpenAIのRateLimit例外
    - GeminiのRateLimit例外
    """
    return runnable.with_retry(
        retry_if_exception_type=(
            RateLimitError,
            ResourceExhausted,
        ),
        wait_exponential_jitter=True,  # 指数バックオフを利用する設定
        stop_after_attempt=2,  # 2回試行する
        exponential_jitter_params={
            "initial": 60,  # 最初の待機時間を60秒（1分）に設定
            "max": 60,  # 最大待機時間も60秒に設定
            "exp_base": 1,  # 指数的な増加をなくす
            "jitter": 0,  # 時間の揺らぎをなくす
        },
    )
