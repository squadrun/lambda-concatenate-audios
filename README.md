# lambda-concatenate-audios

We had this not-so-unique usecase where in we had a couple of URLs that pointed to mp3 recordings. We wanted to aggregate these into one recording and save them to our S3 bucket from which we could fetch the recording (and use it in our android app). 

We had the following ways to do it:

1. Download the audios from the URLs, merge them, and upload them to S3.
2. Download the audios from the URLs, upload them to S3. Make Lambda join/merge these audios and save the final audio in another S3 bucket.
3. (cool way) Lambda downloads the audios, merges them, and saves the final audio to S3.

We, of course, decided to take the cool way because anything else wasn't challenging enough (actually because this was the most efficient way, as it allowed our server to take zero load for this function).

## How it works:
1. Set up Lambda from [here](https://ap-northeast-1.console.aws.amazon.com/lambda/home?region=ap-northeast-1#/create?step=1). Skip blueprint.
2. Copy code from `aggregate_audios.py` to the lambda code editor.
3. Set your role to `S3 execution role` and set up [permissions](https://console.aws.amazon.com/iam/home?region=ap-northeast-1#roles) to include `AmazonS3FullAccess`.
4. Use the code in `invoke_lambda.py` to invoke your lambda function.
