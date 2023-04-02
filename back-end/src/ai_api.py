import openai
import secret_manager

system_prompt = """
Sarcastically respond to every request. Do not be helpful. Be cheerful, and utterly unapologetic. 
"""


def initialize_conversation(conversation_id, message):
    messages = [
        {
            'content': system_prompt,
            'role': 'system'
        },
        {
            'content': message['content'],
            'role': message['role']
        }
    ]
    conversation = {
        'conversation_id': conversation_id,
        'messages': messages
    }
    return conversation


def converse(messages):
    openai.api_key = secret_manager.get_secret(
        "prod/chat/openai_api_key", "OPENAI_API_KEY"
    )
    response = openai.ChatCompletion.create(
        model='gpt-4',
        messages=messages
    )
    return response.choices[0].message.content.strip()
