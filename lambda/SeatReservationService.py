import json

def lambda_handler(event, context):
    if ("simulateBookingFailure" in event and event["simulateBookingFailure"] == "seats"):
        return {
            'statusCode': 500,
            'body': json.dumps("ErrorSeatsNotAvailable")
        }
        
    reservation = "1234"
    return {
    'statusCode': 200,
    "headers": {"content-type": "application/json"},
    'body': json.dumps(reservation)
    }
    

