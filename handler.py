"""
This lambda function utilizes the AWS SDK to generate
a presigned POST requests for an associated S3 bucket.

@author Wayne Manselle
Copyright 2019 Glue Architectures
"""
import json
import logging
import boto3
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    """
    Response to triggered lambda function
    :param event: 
    :param context:
    """
    #Replace bucketName with your unique S3 bucket name
    bucketName = 'analysis_requests'
    
    return {
        'statusCode': 200,
        'body': json.dumps(generatePresignedURL(bucketName,event['object']))
    }

def generatePresignedURL(bucket, object):
    """
    Generates the presigned POST request to be returned
    to the requesting party.
    
    ExpiresIn is defaulted to 3000 to match the bucket settings from the tutorial
    
    :param bucket: String describing the bucket to attach to the presigned URL
    :param object: String describing the bucket to attach to the presigned URL
    :return: String containing the presigned URL, None if the URL could not be generated
    """
    
    s3_client = boto3.client('s3')
    
    try:
        url = s3_client.generate_presigned_post(bucket, object, ExpiresIn = 3000)
    except ClientError as error:
        logging.error(error)
        return None
        
    return url
