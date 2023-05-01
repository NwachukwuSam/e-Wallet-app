import decimal


class TransferRequest:

    def __init__(self):
        self.__senders_account: str = ""
        self.__receivers_account: str = ""
        self.__amount_to_transfer: decimal = 0.00
        self.__remark: str = ""

    def set_receivers_account(self, receivers_account: str):
        self.__receivers_account = receivers_account

    def get_receivers_account_number(self) -> str:
        return self.__receivers_account

    def set_senders_account(self, senders_account: str):
        self.__senders_account = senders_account

    def get_senders_account_number(self) -> str:
        return self.__senders_account

    def set_amount_to_transfer(self, amount: decimal):
        self.__amount_to_transfer = amount

    def get_amount_to_transfer(self) -> decimal:
        return self.__amount_to_transfer

    def set_remark(self, remark: str):
        self.__remark = remark

    def get_purpose(self) -> str:
        return self.__remark
