import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('contactus')


def lambda_handler(event, context):
    print(event)
    name = event['name']
    email = event['email']
    message = event['message']
    table.put_item(
        Item={
            'name': name,
            'email': email,
            'message': message,
        }
    )
    submit = 'Hello {}! Your Data Sucessfully Recorded. We will contact you soon'.format(name)
    return submit
