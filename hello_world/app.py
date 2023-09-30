import json

def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "item": "hello lambda!",
            # "location": ip.text.replace("\n", "")
        }),
        "headers": {
            'Access-Control-Allow-Origin': '*',
        },
    }