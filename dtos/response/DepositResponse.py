import decimal

from data.model.User import User
from data.repository.UserRepoImplement import UserRepoImplement


class DepositResponse:
    user_repository = UserRepoImplement()
    user = User()

    def __init__(self):
        self.__receivers_account_number: str = ""
        self.__amount: decimal = 0.00
        self.__purpose: str = ""

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

    def __str__(self):
        return f"""
                    GEE-WALLET NIGERIA
        ==================================
        Account Name: {self.user.get_first_name()+" "+ self.user.get_last_name()}
        Receiver's Account: {self.__receivers_account_number}
        Amount Deposited: {self.__amount}
        Account Balance : {self.user_repository.check_balance()}
        ==================================
        """
