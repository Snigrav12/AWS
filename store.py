import json
import boto3
import base64

s3 = boto3.client('s3')

BUCKET_NAME = "your-bucket-name"

def lambda_handler(event, context):
    try:
        file_content = event.get("file_content")
        file_name = event.get("file_name") 

        if not file_content or not file_name:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Missing file content or file name."})
            }
        
        decoded_file = base64.b64decode(file_content)

        # Upload the file to S3
        s3.put_object(
            Bucket=BUCKET_NAME,
            Key=file_name,
            Body=decoded_file,
            ContentType="application/pdf"
        )

        return {
            "statusCode": 200,
            "body": json.dumps({"message": "File uploaded successfully", "file_name": file_name})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
