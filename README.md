1>FOR adding:

Go to AWS Lambda Console
Click "Create Function" → Author from scratch
Enter Name: add_two_numbers
Runtime: Python 3.x
Execution Role: Select an existing IAM Role
Upload the lambda_function.py file
Click "Deploy"

2> FOR Uploading File:

Go to AWS Lambda Console
Click "Create Function" → Author from scratch
Enter Name: upload_to_s3
Runtime: Python 3.x
Execution Role: Select an existing IAM Role (with S3 permissions)
Upload the lambda_function.py file
Click "Deploy"

Using AWS Console
Open AWS Lambda Console
Select your function → Test
Enter input JSON → Click "Test"
Run Lambda function using:
aws lambda invoke --function-name add_two_numbers --payload '{"num1":5, "num2":3}' response.json

Create an API Gateway → Add Lambda as an integration
Deploy API → Get an HTTP endpoint to call
