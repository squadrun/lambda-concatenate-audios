import json
from boto3.session import Session

aws_session = Session(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_DEFAULT_LAMBDA_REGION
)

client = aws_session.client('lambda')
key = get_random_string(10) + ".mp3"

payload = {
    "urls": audio_urls_list,
    "filename": key,
    "bucket": AWS_BUCKET_AGGREGATED_AUDIOS
}

client.invoke(
    FunctionName=settings.AWS_LAMBDA_FUNCTION_NAME_AGGREGATE_AUDIOS,
    Payload=json.dumps(payload),
)

aggregated_audio_url = AWS_BASE_URL_S3 + AWS_BUCKET_AGGREGATED_AUDIOS + '/' + key
return aggregated_audio_url
