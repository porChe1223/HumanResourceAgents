import os

class SetEnv:
    """環境変数を管理するクラス
    
    Attributes:
        OPENAI_API_KEY: OpenAIのAPIキー
        GOOGLE_API_KEY: GeminiのAPIキー
        TAVILY_API_KEY: TavilyのAPIキー
    """
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

    @classmethod
    def set_env(self):
        """環境変数が設定されているかを確認"""
        required_keys = [self.OPENAI_API_KEY, self.GOOGLE_API_KEY, self.TAVILY_API_KEY]

        if not required_keys[0]:
            raise ValueError("OPENAI_API_KEYが設定されていません")
        if not required_keys[1]:
            raise ValueError("GOOGLE_API_KEYが設定されていません")
        if not required_keys[2]:
            raise ValueError("TAVILY_API_KEYが設定されていません")


