import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

postMethod = 'POST'
routeAdd = '/addition'


def lambda_handler(event, context):
    response = None
    logger.info(event)
    httpMethod = event['httpMethod']
    path = event['path']

    if httpMethod == postMethod and path == routeAdd:
        response = calculateNumbers(json.loads(event['body']))
    return response


def calculateNumbers(requestBody):
    try:
        value_1 = requestBody['Value_1']
        value_2 = requestBody['Value_2']

        body = {
            'Operation': 'ADD',
            'Message': 'SUCCESS',
            'Sum': str(int(value_1) + int(value_2))
        }

        response = {
            'statusCode': '200',
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        }
        response['body'] = json.dumps(body)
        return response
        # return buildResponse(200, body)
    except:
        logger.exception('Handle manually, exception found!')


def buildResponse(statusCode, body=None):
    response = {
        'statusCode': statusCode,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
    }

    if body is not None:
        response['body'] = json.dumps(body)
    return response

# def lambda_handler(event, context):
#     # TODO implement
#     return {
#         'statusCode': 200,
#         'body': json.dumps('Hello from Lambda!')
#     }
