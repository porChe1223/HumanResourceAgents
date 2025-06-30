import boto3


class DynamoDBCreator:
    """DynamoDBのテーブルを作成するクラス
    
    Attributes:
        dynamodb_client (boto3.client): DynamoDBのクライアント
    
    Methods:
        create_table(): DynamoDBのテーブルを作成する
    
    Tables:
        - human_resources: 人材データを保存するテーブル
    
    """
    def __init__(self, region_name='ap-northeast-1'):
        """DynamoDBの初期化"""
        self.dynamodb_client = boto3.client('dynamodb', region_name=region_name)

    def _create_table(self):
        """DynamoDBのテーブルを作成"""
        try:
            """ラウンドデータ"""
            self.dynamodb_client.create_table(
                TableName='human_resources',
                KeySchema=[
                    {'AttributeName': 'human', 'KeyType': 'HASH'},  # パーティションキー
                ],
                AttributeDefinitions=[
                    {'AttributeName': 'human', 'AttributeType': 'S'},  # 文字列
                ],
                ProvisionedThroughput={
                    'ReadCapacityUnits': 1,
                    'WriteCapacityUnits': 1
                }
            )

        except Exception as e:
            print(f"人材データのDynamoDBテーブル作成に失敗しました->\n {e}")
            raise Exception(f"人材データのDynamoDBテーブル作成に失敗しました->\n {e}")

if __name__ == "__main__":
    dynamo_db_creator = DynamoDBCreator()
    dynamo_db_creator._create_table()
