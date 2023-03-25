# add your get-notes function here
import json
import boto3
from boto3.dynamodb.conditions import Key

dynamodb_resource = boto3.resource("dynamodb")
table = dynamodb_resource.Table("lotion-30140722")

def handler(event, context):
    email = event["queryStringParameters"]["email"]

    try:
        res = table.query(KeyConditionExpression = Key("email").eq(email))
        return{
            "statusCode": 201,
            "body": json.dumps(
                res["items"]
            )
        }
    except Exception as exp:
        print(f"exception: {exp}")
        return{
            "StatusCode": 500,
            "body": json.dumps(
            {
                "message:": str(exp)
            })
        }

