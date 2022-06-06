
from azure.servicebus import ServiceBusClient, ServiceBusMessage

from connection import connstr,queue_name

from data1 import people_string

with ServiceBusClient.from_connection_string(connstr) as client:
    with client.get_queue_sender(queue_name) as sender:
        # Sending a single message
        #single_message = ServiceBusMessage("Single message")
        #sender.send_messages(single_message)

        # Sending a list of messages
        #messages = [ServiceBusMessage("First message"), ServiceBusMessage("Second message")]
        #sender.send_messages(messages)

        # Send json file
        single_message = ServiceBusMessage(people_string)
        sender.send_messages(single_message)
