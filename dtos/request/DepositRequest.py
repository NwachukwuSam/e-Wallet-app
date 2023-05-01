import decimal


class DepositRequest:
    def __init__(self):
        self.__senders_account_number: str = ""
        self.__receivers_account_number: str = ""
        self.__amount: decimal = 0.00
        self.__purpose: str = ""

    def set_senders_account_number(self, senders_account: str):
        self.__senders_account_number = senders_account

    def get_senders_account_number(self) -> str:
        return self.__senders_account_number

    def set_receivers_account_number(self, receivers_account: str):
        self.__receivers_account_number = receivers_account

    def get_receivers_account_number(self) -> str:
        return self.__receivers_account_number

    def set_amount(self, amount: decimal):
        self.__amount = amount

    def get_amount(self) -> decimal:
        return self.__amount

    def set_purpose(self, purpose: str):
        self.__purpose = purpose

    def get_purpose(self) -> str:
        return self.__purpose
