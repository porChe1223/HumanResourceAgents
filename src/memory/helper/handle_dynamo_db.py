import boto3

class DynamoDBHandler:
    """DynamoDBを操作するハンドラークラス"""
    
    def __init__(self, table_name: str, region_name: str) -> None:
        """DynamoDBハンドラーの初期化
        
        Args:
            table_name: 操作するDynamoDBテーブル名
        """
        self.client = boto3.client('dynamodb', region_name=region_name)
        self.table_name = table_name

    def put_item(self, human_name: str, human_info: str) -> None:
        """DynamoDBにアイテムを追加"""
        item = {
            'human': {'S': human_name},
            'info': {'S': human_info},
        }
        self.client.put_item(TableName=self.table_name, Item=item)

    def put_items(self, items: dict) -> None:
        """複数のアイテムをDynamoDBに追加"""
        for human_name, human_info in items.items():
            self.put_item(human_name, human_info)
            print(f"DynamoDBにアイテムを追加: {human_name}")

    def get_item(self, human_name: str) -> dict:
        """DynamoDBからアイテムを取得"""
        key = {
            'human': {'S': human_name}
        }
        response = self.client.get_item(TableName=self.table_name, Key=key)
        print(f"DynamoDBからアイテムを取得: {human_name}")
        return response.get('Item', {})
