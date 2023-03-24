# add your save-note function here
import json
import boto3

dynamodb_resource = boto3.resource("dynamodb")
table = dynamodb_resource.Table("lotion-30140722")

def lambda_handler(event, context):
    body = json.loads(event["body"])
    try:
        table.put_item(Item=body)
        return{
            "StatusCode": 201,
            "body": "success"
        }
    except Exception as exp:
        return{
            "StatusCode": 500,
            "body": json.dumps(
            {
            "message:": str(exp)
            }
            )
        }