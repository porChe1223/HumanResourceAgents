from langchain_core.messages import BaseMessage
from typing import List

def parse_list(message: BaseMessage) -> List[str]:
    """AIMessageのcontentから改行区切りのリストをパースする
    
    Args:
        message: AIMessage
        
    Returns:
        List[str]: 改行区切りのリスト
    """
    return message.content.strip().split('\n')
