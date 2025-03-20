import boto3
import os

# Load AWS credentials from environment variables
AWS_REGION = os.getenv("AWS_REGION", "us-west-1")
s3 = boto3.client("s3")

# Define bucket and file details
bucket_name = "exp3implementingcloudstorage"  # Change to your bucket name
file_path = "test_file.txt"  # File on local machine
object_name = "uploaded_test_file.txt"  # Name in S3

try:
    s3.upload_file(file_path, bucket_name, object_name)
    print(f"✅ File '{file_path}' uploaded to S3 bucket '{bucket_name}' as '{object_name}'")
except Exception as e:
    print(f"❌ Error uploading file: {e}")
