import json
import boto3

rekognition = boto3.client('rekognition')

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key    = event['Records'][0]['s3']['object']['key']

    response = rekognition.detect_labels(
        Image={'S3Object': {'Bucket': bucket, 'Name': key}},
        MaxLabels=10
    )

    print(json.dumps(response['Labels'], indent=2))

    return {
        'statusCode': 200,
        'body': json.dumps(response['Labels'])
    }
