import json
import logging
import os
import boto3
import pandas as pd

# setup logger
logger = logging.getLogger()
logger.setLevel(os.environ.get('LOG_LEVEL', 'INFO').upper())

def lambda_handler(event, context):

    for records in event.get('Records'):
        s3_event = json.loads(records['body'])

        logger.debug("##### s3_event")
        logger.debug(s3_event)

    s3_bucket = s3_event.get("bucket")
    s3_key = s3_event.get("key")

    boto_client = boto3.client('s3', aws_access_key_id='key', aws_secret_access_key='secret', endpoint_url='http://localstack:4572')

    obj = boto_client.get_object(Bucket=s3_bucket,
                        Key=s3_key)

    csv_file_df = pd.read_csv(obj['Body'])
    logger.info(csv_file_df)

    return {
        "statusCode": 200,
        "body": csv_file_df.to_json()
    }
