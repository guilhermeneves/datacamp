# Putting Files in the Cloud

### S3
```
import boto3

s3 = boto3.client('s3',
                  region_name='us-east-1',
                  aws_access_key=AWS_KEY_ID,
                  aws_secret_access_key=AWS_SECRET)

response = s3.list_buckets()

#or multiple objects

reponse = s3.list_objects(Bucket='test', MaxKeys=2, Prefix='gid_requests_201')

```

Creating a bucket: `bucket = s3.create_bucket(Bucket='gid-requests')`
Deleting a bucket: `bucket = s3.delete_bucket('gid-requests')`
Uploading a file: 
```
s3.upload_file(Filename='asdas.csv', Bucket='asdasd', Key='asdasd.csv')
```

Getting Object Metadata:

```
response = s3.head_object(
  Bucket='test',
  Key='gid_request.csv'
)

```

### SNS

```

import boto3

s3 = boto3.client('sns',
                  region_name='us-east-1',
                  aws_access_key=AWS_KEY_ID,
                  aws_secret_access_key=AWS_SECRET)

response = s3.list_topics()
```