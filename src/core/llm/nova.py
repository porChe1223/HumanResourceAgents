from langchain_aws import ChatBedrock
from core.config.set_env import SetEnv

llm_nova = ChatBedrock(
    model_id="us.amazon.nova-lite-v1:0",
    temperature=0,
    aws_access_key_id=SetEnv.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=SetEnv.AWS_SECRET_ACCESS_KEY,
    aws_session_token=SetEnv.AWS_SESSION_TOKEN,
    aws_region=SetEnv.AWS_REGION,
)

