import json
import os

def get_cors_headers(origin):
    return {
        'Access-Control-Allow-Origin': origin,
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
    }

def lambda_handler(event, context):
    origin = event["headers"].get("origin")

    allowed_origins = os.environ.get("ALLOWED_ORIGINS", "").split(',')

    if origin in allowed_origins:
        cors_headers = get_cors_headers(origin)

        return {
            "statusCode": 200,
            "body": json.dumps({
                "item": "hello lambda!",
            }),
            "headers": cors_headers
        }
    else:
        return {
            "statusCode": 403,
            "body": json.dumps({
                "message": "Origin not allowed.",
            }),
        }