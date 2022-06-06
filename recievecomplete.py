
from azure.servicebus import ServiceBusClient, ServiceBusMessage

from connection import connstr,queue_name

with ServiceBusClient.from_connection_string(connstr) as client:
    with client.get_queue_receiver(queue_name) as reciever:
        for msg in reciever:
            print(str(msg))
            reciever.complete_message(msg)