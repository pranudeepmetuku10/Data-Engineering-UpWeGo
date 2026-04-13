# Exercise 3: Boto3 AWS + S3 + Python

## Objective

Learn to interact with AWS S3 using Boto3 to download data from cloud storage in a production-like scenario.

## Problem Description

You need to build a data pipeline that:

1. Authenticates with AWS using credentials or IAM roles
2. Lists objects in an S3 bucket
3. Filters objects based on patterns (e.g., specific prefixes or file types)
4. Downloads multiple objects from S3
5. Processes the downloaded data
6. Uploads results back to S3

This is a critical skill for modern data engineers working with cloud infrastructure.

## Requirements

- Use Boto3 to interact with AWS S3
- List and filter S3 objects
- Download files from S3
- Handle S3 API errors gracefully
- Work with both public and private S3 buckets
- Implement efficient batch operations
- Process downloaded data

## Hints

- Use `boto3.client('s3')` to create an S3 client
- Use `list_objects_v2()` to list objects with pagination
- Use `download_file()` or `get_object()` for downloads
- Use `put_object()` to upload files
- Use `paginator` for handling large result sets
- Handle `ClientError` exceptions
- For testing without AWS, use LocalStack or MinIO

## Data

The exercise uses sample data from a public S3 bucket. Credentials are provided or you can use mock AWS services for testing.

## Expected Output

After running your solution, you should have:
- Downloaded files in a `s3_data/` directory
- Processed data saved locally
- Results uploaded back to S3
- Logs showing all operations

## Testing Your Solution

For local testing without AWS credentials:

```bash
docker-compose build
docker-compose run app python solution.py
```

For testing against real AWS (requires credentials):

```bash
docker-compose build
AWS_ACCESS_KEY_ID=your_key AWS_SECRET_ACCESS_KEY=your_secret docker-compose run app python solution.py
```

## Bonus Challenges

1. **Batch Processing** - Process large numbers of files using batching
2. **Multipart Upload** - Implement multipart upload for large files
3. **S3 Sync** - Build an S3 sync tool similar to AWS CLI
4. **Encryption** - Handle encrypted S3 objects
5. **Access Control** - Work with S3 bucket policies and ACLs
6. **CloudWatch Integration** - Log operations to CloudWatch

## Resources

- [Boto3 S3 Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html)
- [AWS S3 User Guide](https://docs.aws.amazon.com/s3/index.html)
- [LocalStack for Testing](https://localstack.cloud/)
- [Boto3 Examples](https://github.com/aws/aws-sdk-python-examples)

## Next Steps

Once you complete this exercise, move to Exercise 4 to learn about JSON/CSV conversion and directory traversal.
