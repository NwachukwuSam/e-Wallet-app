import decimal


class TransferResponse:
    def __init__(self):
        self.__pin: int = 0
        self.__senders_account: str = ""
        self.__receivers_account: str = ""
        self.__amount_to_transfer: decimal = 0.00
        self.__remark: str = ""

    def set_pin(self, pin: int):
        self.__pin = pin

    def get_pin(self) -> int:
        return self.__pin

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

    def get_remark(self) -> str:
        return self.__remark

    def __str__(self):
        return f"""  GEE-WALLET NIGERIA
        =====================================
        Sender's Account: {self.__senders_account}
        Receiver's Account: {self.__receivers_account}
        Transferred Amount: {self.__amount_to_transfer}
        Remark: {self.__remark}
        =====================================
        """
