import os

class SetEnv:
    """環境変数を管理するクラス
    
    Attributes:
        OPENAI_API_KEY: OpenAIのAPIキー
        GOOGLE_API_KEY: GeminiのAPIキー
        TAVILY_API_KEY: TavilyのAPIキー
        AWS_ACCESS_KEY_ID: AWSのアクセスキーID
        AWS_SECRET_ACCESS_KEY: AWSのシークレットアクセスキー
        AWS_SESSION_TOKEN: AWSのセッショントークン
        AWS_REGION: AWSのリージョン
    """
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_SESSION_TOKEN = os.getenv("AWS_SESSION_TOKEN")
    AWS_REGION = os.getenv("AWS_REGION")

    @classmethod
    def set_env(self):
        """環境変数が設定されているかを確認"""
        required_keys = [
            self.OPENAI_API_KEY,
            self.GOOGLE_API_KEY,
            self.TAVILY_API_KEY,
            self.AWS_ACCESS_KEY_ID,
            self.AWS_SECRET_ACCESS_KEY,
            self.AWS_SESSION_TOKEN,
            self.AWS_REGION,
        ]

        for key in required_keys:
            if key is None:
                raise ValueError(f"{key}が設定されていません")

