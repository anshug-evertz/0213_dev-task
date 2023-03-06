import json
import boto3

client = boto3.client('dynamodb')
REGION = "us-east-1"

def dao_helper(value_1, value_2, operator):
    try:
        dynamodb = boto3.resource('dynamodb', region_name=REGION)
        table = dynamodb.Table('anshug_0227-2')
        
        response = table.scan(Select='COUNT')
        id = response['Count']
        id = id+1
        
        print(id)
        
        table.put_item(
            Item={
                'id': str(id),
                'value_1': value_1,
                'value_2': value_2,
                'operation': operator,
                'result': 'None'
            }
        )
        
    except Exception:
        print("Exception caught in dao_helper")

def lambda_handler(event, context):
    records = event['Records']
    
    for record in records:
        body = record['body']
        json_obj = json.loads(body)
        
        value_1 = json_obj['value_1']
        value_2 = json_obj['value_2']
        operator = json_obj['operation']

        dao_helper(value_1, value_2, operator)
        
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
