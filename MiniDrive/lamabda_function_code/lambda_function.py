import json
import boto3
import os
import base64

s3 = boto3.client('s3')
BUCKET_NAME = os.environ.get("BUCKET_NAME", "minidrive-files")

def lambda_handler(event, context):
    method = event.get("httpMethod")

    if method == "GET": 
        response = s3.list_objects_v2(Bucket=BUCKET_NAME)
        files = []
        for item in response.get("Contents", []):
            files.append({
                "filename": item["Key"],
                "url": f"https://{BUCKET_NAME}.s3.amazonaws.com/{item['Key']}"
            })
        return {
            "statusCode": 200,
            "body": json.dumps(files)
        }
    
    elif method == "POST":
        try:
            body = json.loads(event['body'])
            filename = body.get("filename")
            filedata = body.get("filedata")

            # Validate input
            if not filename or not filedata:
                return {
                    "statusCode": 400,
                    "body": json.dumps({"error": "Missing filename or filedata"})
                }

            # Decode and upload AFTER validation
            file_content = base64.b64decode(filedata)
            s3.put_object(Bucket=BUCKET_NAME, Key=filename, Body=file_content)

            return {
                "statusCode": 200,
                "body": json.dumps({"message": f"File '{filename}' uploaded successfully"})
            }

        except Exception as e:
            return {
                "statusCode": 500,
                "body": json.dumps({"error": str(e)})
            }



    return {
        "statusCode": 400,
        "body": json.dumps({"error": "Unsupported method"})
    }
