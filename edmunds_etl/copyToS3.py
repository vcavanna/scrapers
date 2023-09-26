# Sets up s3 connection

import boto3
boto3.setup_default_session(profile_name='vincentEdmunds-powerUser')
s3 = boto3.resource('s3')

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)

# Upload a new file
data = open('car_entries.csv', 'rb')
s3.Bucket('edmunds-cars').put_object(Key='load/car_entries.csv', Body=data)