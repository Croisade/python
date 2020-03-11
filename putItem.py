import time
import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('guestbook')
millis = int(round(time.time() * 1000))

table.put_item(
        Item={
            'date': millis,
            'message': 'tacobell',
        }
)

