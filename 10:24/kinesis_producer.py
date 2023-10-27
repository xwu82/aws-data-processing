from uuid import uuid4 
import json
import time
from kiner.producer import KinesisProducer

name = ("John", "Jane", "Bob", "Alice")
age = (25, 30, 35, 40)
gender = ("male", "female", "male", "female")
id = (1, 2, 3, 4)
data = {
    "name": name,
    "age": age,
    "gender": gender,
    "id": id
}
peopledata =json.dumps(data)
encode_data = bytes(peopledata.encode("utf-8"))


# def on_flush(count, last_flushed_at, Data=b'', PartitionKey='', Metadata=()):
#     print (f"""
#         Flushed {count} messages at timestamp {last_flushed_at}
#         Last message was {Metadata['id']} paritioned by {PartitionKey} ({len(Data)} bytes)
#     """)

p = KinesisProducer ('kinesis-test')

# for i in range (5):
p.put_record(encode_data)

p.close ()





