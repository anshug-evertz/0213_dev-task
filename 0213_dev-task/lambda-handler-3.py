import json
import boto3

client = boto3.client('dynamodb')
REGION = "us-east-1"

def add(x, y):
    return x + y

def publish_to_sns(result):
    try:
        sns = boto3.client('sns')
        topic_arn = 'arn:aws:sns:us-east-1:944486121133:anshug_0227_MySNSTopic'
    
        message = {
            'default': 'from lambda-handler-3',
            'sns': result
        }
        
        message_json = json.dumps(message)
        
        print(message_json)
        
        response = sns.publish(
            TopicArn = topic_arn,
            Message = message_json,
            MessageStructure='json'
        )
    except Exception:
        print("Exception caught in publish_to_sns")
    
def calc_helper(num1, num2, operation, record):
    try:
        if operation == '+':
            result = add(num1, num2)
            handle_modify(record, result)
            publish_to_sns(result)
        else:
            print("Invalid Input, in calc_helper")    
    except Exception:
        print("Exception caught in calc_helper")
    
def handle_insert(record):
    try:
        print('Handling the INSERT event')
        
        newImage = record['dynamodb']['NewImage']
        value_1 = newImage['value_1']['S']
        
        newImage = record['dynamodb']['NewImage']
        value_2 = newImage['value_2']['S']
        
        newImage = record['dynamodb']['NewImage']
        operation = newImage['operation']['S']
        
        calc_helper(float(value_1), float(value_2), operation, record)
        
    except Exception:
        print("Exception caught in handle_insert")

def handle_modify(record, result):
    try:
        print("updating...")
        dynamodb = boto3.resource('dynamodb', region_name=REGION)
        table = dynamodb.Table('anshug_0227-2')
        
        table.update_item(
            Key={'id': '1'},
            AttributeUpdates={
                'result': result
            }
        )
    except Exception:
        print("Exception caught in handle_modify")
    
def lambda_handler(event, context):
    # TODO implement
    print(event)
    
    try:
        for record in event['Records']:
            # handle on the basis of event type
            if record['eventName'] == 'INSERT':
                handle_insert(record)
    except Exception:
        print("Exception caught")
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
