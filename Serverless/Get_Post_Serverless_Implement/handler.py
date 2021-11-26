import json


def hello(event, context):
    if event['httpMethod'] == 'GET' and event['queryStringParameters']['query']:
        body = {
        "message": "Your query is " +event['queryStringParameters']['query'],
        # "input": event,
        }
        response = {
            "statusCode": 200, 
            "body": json.dumps(body)
        }

    if event['httpMethod'] == 'POST' and event['body']:
        body = {
        "message": "Received Your body text", 
        'msgBody': event['body']
        # "input": event,
        }
        response = {
            "statusCode": 200, 
            "body": json.dumps(body)
        }
    

    return response
