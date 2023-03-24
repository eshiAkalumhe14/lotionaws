# add your delete-note function here
import boto3
import json

dynamodb_resource = boto3.resource("dynamodb")
table = dynamodb_resource.Table("lotion-30140722")

def delete_item(email, note_id):
    return table.delete_item(
        Key = {
        "email": email,
        "id": note_id
        }
    )

def lambda_handler(event, context):
    body = json.loads(event["body"])
    note_id = body["id"]
    email = body["email"]

    try: 
        delete_item(email, note_id)
        return{
            "statusCode": 201,
            "body": json.dumps({
                    "message": "success"
            })
        }
    except Exception as exp:
        print(exp)
        return{
            "statusCode": 500,
                "body": json.dumps({
                    "message": str(exp)
                })
        }
