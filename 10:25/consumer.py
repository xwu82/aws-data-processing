import boto3
import json
import base64

# Define the S3 bucket and object key
bucket_name = 's3-bucket-training2023'
object_key = 'test.json'

def lambda_handler(event, context):   
    print(f"event: {event}")
    for record in event["Records"]:
        encoded_data = record["kinesis"]["data"]
        decoded_data = base64.b64decode(encoded_data)
        print('decoded_data type', type(decoded_data))
        print(decoded_data)
        

        # deserialized_data = json.loads(decoded_data)
        # print('deserialized_data type', type(deserialized_data))
        # print(f'data : {deserialized_data}')
        
        s3 = boto3.client('s3')
        try:
            # Upload the data to the S3 bucket
            s3.put_object(Bucket=bucket_name, Key=object_key, Body=decoded_data)
            return {
                'statusCode': 200,
                'body': json.dumps('Data successfully written to S3')
            }
        except Exception as e:
            return {
                'statusCode': 500,
                'body': json.dumps(f'Error: {str(e)}')
            }
