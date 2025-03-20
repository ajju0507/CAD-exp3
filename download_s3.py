import boto3
import os

# Load AWS credentials from environment variables
AWS_REGION = os.getenv("AWS_REGION", "us-west-1")

# Create the S3 client
s3 = boto3.client("s3")

# Define the bucket name
bucket_name = "exp3implementingcloudstorage"  # Change to your bucket name

try:
    response = s3.list_objects_v2(Bucket=bucket_name)
    if "Contents" in response:
        for obj in response["Contents"]:
            print(f"📂 Object: {obj['Key']}")
    else:
        print("🛑 Bucket is empty")
except Exception as e:
    print(f"❌ Error listing objects: {e}")
