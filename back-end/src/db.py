import json
import boto3
from boto3.dynamodb.types import TypeDeserializer, TypeSerializer

dynamodb = boto3.client('dynamodb')


# Define a custom deserializer to convert DynamoDB items to Python dictionaries
deserializer = TypeDeserializer()

# Define a custom serializer to convert Python dictionaries to DynamoDB items
serializer = TypeSerializer()


def create_conversation(conversation):
    response = dynamodb.put_item(
        TableName='chats',
        Item={
            'conversation_id': serializer.serialize(conversation['conversation_id']),
            'messages': serializer.serialize(conversation['messages'])
        }
    )
    return response


def update_conversation(conversation):
    response = dynamodb.update_item(
        TableName='chats',
        Key={
            'conversation_id': serializer.serialize(conversation['conversation_id'])
        },
        UpdateExpression='SET messages = :messages',
        ExpressionAttributeValues={
            ':messages': serializer.serialize(conversation['messages'])
        }
    )
    return response


def get_conversation(conversation_id):
    response = dynamodb.get_item(
        TableName='chats',
        Key={
            'conversation_id': serializer.serialize(conversation_id)
        }
    )
    item = response.get('Item')
    if item:
        return {
            'conversation_id': deserializer.deserialize(item['conversation_id']),
            'messages': deserializer.deserialize(item['messages'])
        }
    return None
