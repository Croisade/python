import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('guestbook')

response = table.scan()
items = response['Items']
print(items)
