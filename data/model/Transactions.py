import decimal


class Transactions:

    def __init__(self):
        self.__transaction_id: int = 0
        self.__amount: decimal = 0.0
        self.__transaction_type: str = ""
        self.__sender: str = ""
        self.__receiver: str = ""

    def set_transaction_id(self, transaction_id):
        self.__transaction_id = transaction_id

    def get_transaction_id(self) -> int:
        return self.__transaction_id

    def set_amount(self, amount):
        self.__amount = amount

    def get_amount(self) -> decimal:
        return self.__amount

    def set_transaction_type(self, transaction_type):
        self.__transaction_type = transaction_type

    def get_last_name(self) -> str:
        return self.__transaction_type

    def set_sender(self, sender):
        self.__sender = sender

    def get_sender(self) -> str:
        return self.__sender

    def set_receiver(self, receiver):
        self.__receiver = receiver

    def get_receiver(self) -> str:
        return self.__receiver
    