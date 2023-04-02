import json
import ai_api
import db
import validation

print('Loading function')


def error_response(message):
    return {
        'statusCode': '400',
        'body': message,
        'headers': {
            'Content-Type': 'application/json',
        },
    }


def success_response(message):
    return {
        'statusCode': '200',
        'body': message,
        'headers': {
            'Content-Type': 'application/json',
        },
    }


def lambda_handler(event, context):
    '''
    This function processes chat messages and saves them to DynamoDB
    '''
    if not validation.validate_request(event):
        return error_response('Invalid request')
    message = json.loads(event['body'])
    if not validation.validate_body(message):
        return error_response('Invalid body')

    message['role'] = 'user'
    print("Message: " + json.dumps(message, indent=2))

    conversation = db.get_conversation(message['conversation_id'])

    if conversation:
        messages = conversation['messages']
        messages.append({
            'content': message['content'],
            'role': message['role']
        })
        conversation['messages'] = messages
        db.update_conversation(conversation)
    else:
        conversation = ai_api.initialize_conversation(
            message['conversation_id'],
            message
        )
        db.create_conversation(conversation)
    conversation = db.get_conversation(message['conversation_id'])

    print("conversation: " + json.dumps(conversation, indent=2))

    response = ai_api.converse(conversation['messages'])

    print("response: " + response)
    db.update_conversation({
        'conversation_id': conversation['conversation_id'],
        'messages': conversation['messages'] + [{
            'content': response,
            'role': 'assistant'
        }]
    })

    return success_response(
        json.dumps({
            'conversation_id': conversation['conversation_id'],
            'content': response,
        })
    )
