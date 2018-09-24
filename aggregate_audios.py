import urllib2
import boto3
import logging

s3 = boto3.client('s3')

def lambda_handler(event, context):
    logger = logging.getLogger()
    urls = event['urls']  # converts list as string to list
    key = event['filename']
    bucket = event['bucket']
    aggregated_mp3s = ""  # would store audio bytes as string
    
    for url in urls:
        try:
            aggregated_mp3s += urllib2.urlopen(url).read()  # concatenating mp3s here
        except Exception as exc:
            logger.error("Got error while trying to read url: {0} error: {1}".format(url, exc))
            raise
    
    response = s3.put_object(
            ACL='public-read',
            Body=aggregated_mp3s,
            Bucket=bucket,
            Key=key,
            ContentType="audio/mpeg"
        )

    return response