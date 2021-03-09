from abc import ABC, abstractmethod

class SMSBase(ABC):
    @abstractmethod
    def build_msg_request(self, message, phone_number):
        ...

    @abstractmethod
    def send_msg(self, payload):
        ...