import json
from azure.servicebus import ServiceBusClient, ServiceBusMessage

from connection import connstr,queue_name

with ServiceBusClient.from_connection_string(connstr) as client:
    with client.get_queue_receiver(queue_name, max_wait_time=30) as reciever:
     for msg in reciever:
         print(str(msg))
         json_object = json.loads(str(msg))
         print(json_object)