import urllib2
import boto3
import ast

s3 = boto3.client('s3')

def lambda_handler(event, context):
    urls = ast.literal_eval(event['urls'])  # converts list as string to list
    key = event['filename']
    bucket = event['bucket']
    aggregated_mp3s = ""  # would store audio bytes as string
        
    for url in urls:
        print url
        try:
            aggregated_mp3s += urllib2.urlopen(url).read()  # concatenating mp3s here
        except urllib2.URLError as e:
            pass
    
    response = s3.put_object(
            ACL='public-read',
            Body=aggregated_mp3s,
            Bucket=bucket,
            Key=key,
            ContentType="audio/mpeg"
        )
        
    print response
