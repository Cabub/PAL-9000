def validate_request(event):
    if event['httpMethod'] != 'POST':
        return False
    if event['headers']['Content-Type'] != 'application/json':
        return False
    return True


def validate_body(body):
    if 'conversation_id' not in body:
        return False
    if 'content' not in body:
        return False
    return True
