import json
import boto3
import random

def lambda_handler(event, context):
    # TODO implement
    try:
        MessageBody = {
            'value_1': str(random.random()),
            'value_2': str(random.random()),
            'operation': '+'
        }
        
        MessageBody_json = json.dumps(MessageBody)
        
        sqs = boto3.client('sqs')
        sqs.send_message(
            QueueUrl = 'https://sqs.us-east-1.amazonaws.com/944486121133/0227-MyQueue',
            MessageBody = MessageBody_json
        )
        
    except Exception:
        print("Exception caught")
    
    return {
        'statusCode': 200,
        'body': json.dumps(MessageBody_json)
    }
