
from azure.servicebus import ServiceBusClient, ServiceBusMessage
from connection import connstr,queue_name

with ServiceBusClient.from_connection_string(connstr) as client:
    with client.get_queue_receiver(queue_name) as reciever:
        for msg in reciever:
            print(str(msg))
            if "Single message" in str(msg):
               reciever.abandon_message(msg)
            else:
                reciever.complete_message(msg)