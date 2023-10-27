import os
import time
import json
import boto3

# AWS Kinesis Stream Name
stream_name = "kinesis-test"

# Initialize Kinesis Producer
#producer = KinesisProducer(stream_name)

# Initialize Boto3 Kinesis client
kinesis_client = boto3.client('kinesis')

# Send a single record to the Kinesis stream
def send_record(data):
    try:
        # Generate a unique partition key (optional, but improves distribution)
        partition_key = str(time.time())

        # Send the record to the Kinesis stream
        kinesis_client.put_record(StreamName=stream_name, Data=data, PartitionKey=partition_key)
        
        print("Record sent successfully.")
    except Exception as e:
        print(f"Error sending record: {e}")

# Example data to send
sample_data = {
    "sensor_id": 1,
    "timestamp": int(time.time()),
    "value": 42.0
}

# Send the sample data to the Kinesis stream
data =json.dumps(sample_data)
encode_data = bytes(data.encode("utf-8"))
send_record(encode_data)
# Cleanup and close the producer
#producer.close()
