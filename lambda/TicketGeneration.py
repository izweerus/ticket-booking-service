import json
import uuid

def handler(event, context):
    try:
        ticket_id = str(uuid.uuid4())
        response = {
            "statusCode": 200,
            "headers": {
                "content-type": "application/json"
            },
            "body": json.dumps(ticket_id)
        }
        return response
    except Exception as e:
        print("Error:", e)
        response = {
            "statusCode": 500,
            "body": json.dumps({"error": "Internal Server Error"})
        }
        return response
