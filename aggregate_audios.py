import urllib2
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    urls = event['urls']  # converts list as string to list
    key = event['filename']
    bucket = event['bucket']
    aggregated_mp3s = ""  # would store audio bytes as string
    
    print urls
    
    for url in urls:
        print url
        try:
            aggregated_mp3s += urllib2.urlopen(url).read()  # concatenating mp3s here
        except urllib2.URLError as e:
            print e.reason
        except ValueError as e:
            print "Not a Valid URL"
    
    response = s3.put_object(
            ACL='public-read',
            Body=aggregated_mp3s,
            Bucket=bucket,
            Key=key,
            ContentType="audio/mpeg"
        )
        
    print response
