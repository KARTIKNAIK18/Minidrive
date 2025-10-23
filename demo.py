import boto3
import os

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = os.environ['BUCKET_NAME']
    
    # Extract user identifier and file name from the request
    user_id = event['queryStringParameters']['user_id']
    file_name = event['queryStringParameters']['file_name']
    
    # Create user-specific folder in S3
    s3_key = f"{user_id}/{file_name}"
    
    # Generate presigned URL
    presigned_url = s3.generate_presigned_url(
        'put_object',
        Params={'Bucket': bucket_name, 'Key': s3_key},
        ExpiresIn=3600
    )
    
    return {
        'statusCode': 200,
        'body': presigned_url
    }