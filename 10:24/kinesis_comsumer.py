import time
import boto3

# AWS Kinesis Stream Name
stream_name = "kinesis-test"

# AWS region
aws_region = "us-east-2"

# Initialize the Kinesis client
kinesis_client = boto3.client('kinesis', region_name=aws_region)

# Get a shard iterator for a Kinesis stream
def get_shard_iterator(stream_name, shard_id, iterator_type):
    response = kinesis_client.get_shard_iterator(
        StreamName=stream_name,
        ShardId=shard_id,
        ShardIteratorType=iterator_type
    )
    return response['ShardIterator']

# Consume records from a Kinesis shard
def consume_stream(stream_name, shard_id):
    shard_iterator = get_shard_iterator(stream_name, shard_id, 'LATEST')

    while True:
        response = kinesis_client.get_records(ShardIterator=shard_iterator, Limit = 2)

        print(response)


        time.sleep(5)

        # for record in response['Records']:
        #     data = record['Data'].decode('utf-8')
        #     print(f"Received record: {data}")

        # Get the next shard iterator
        shard_iterator = response['NextShardIterator']

if __name__ == "__main__":
    # Use DescribeStream to get the shard ID (you can hardcode it if known)
    response = kinesis_client.describe_stream(StreamName=stream_name)
    shard_id = response['StreamDescription']['Shards'][0]['ShardId']

    consume_stream(stream_name, shard_id)

