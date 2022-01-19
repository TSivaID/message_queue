from abc import ABC, abstractmethod


class AbstractMessageQueueClient(ABC):
    def __init__(self, queue, **kwargs):
        self.queue = queue

    @abstractmethod
    def send_message(self, payload: str, metadata: dict):
        """
        Send a message to the queue.
        :param payload: str, The body text of the message
        :param metadata: dict, Custom attributes of the message. 
          These are key-value pairs that can be whatever you want.
        :return: The response from Queue that contains the assigned message ID.
        """
        pass

    @abstractmethod
    def receive_messages(self, max_number: int, wait_time: int):
        """
        Receive a batch of messages in a single request from the queue.
        :param max_number: int, The maximum number of messages to receive. The actual number
                                of messages received might be less.
        :param wait_time: int, The maximum time to wait (in seconds) before returning. When
                                this number is greater than zero, long polling is used. This
                                can result fewer false empty responses.
        :return: list, A list of messages. Each message is a dictionary with the following
                            keys:
                            - payload: str, The body text of the message
                            - metadata: dict, Custom attributes of the message. These are key-value
                                                  pairs that can be whatever you want.
        """
        pass


class MessageQueue:
  def __init__(self, client: AbstractMessageQueueClient):
    self.client = client

  def send_message(self, payload: str, metadata: dict):
    self.client.send_message(payload, metadata)

  def receive_messages(self, max_number: int, wait_time: int):
    self.client.receive_messages(max_number, wait_time)


class DummyMessageQueueClient(AbstractMessageQueueClient):
  def send_message(self, payload: str, metadata: dict):
    print("DummyMessageQueueClient: sent")

  def receive_messages(self, max_number: int, wait_time: int):
    print("DummyMessageQueueClient: received")


class AnotherDummyMessageQueueClient(AbstractMessageQueueClient):
  def send_message(self, payload: str, metadata: dict):
    print("AnotherDummyMessageQueueClient: sent")

  def receive_messages(self, max_number: int, wait_time: int):
    print("AnotherDummyMessageQueueClient: received")