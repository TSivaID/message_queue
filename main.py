from message_queue.client import MessageQueue
from message_queue.client import DummyMessageQueueClient
from message_queue.client import AnotherDummyMessageQueueClient


def main():
    message_queue = MessageQueue(DummyMessageQueueClient("test"))
    message_queue.send_message("test_message", {'blah': "Blah"})
    message_queue.receive_messages(1, 10)

    message_queue = MessageQueue(AnotherDummyMessageQueueClient("test"))
    message_queue.send_message("test_message", {'blah': "Blah"})
    message_queue.receive_messages(1, 10)

if __name__ == "__main__":
    main()