import urllib
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    urls = event['urls']
    key = event['filename']
    bucket = event['bucket']
    aggregated_mp3s = ""  # would store audio bytes as string
    
    for url in urls:
        try:
            aggregated_mp3s += urllib.urlopen(url).read()  # concatenating mp3s here
        except URLError as e:
            pass
    
    response = s3.put_object(
            ACL='public-read',
            Body=aggregated_mp3s,
            Bucket=bucket,
            Key=key,
            ContentType="audio/mpeg"
        )
        
    print response
