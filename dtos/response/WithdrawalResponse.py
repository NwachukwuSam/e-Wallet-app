import decimal

from data.repository.UserRepoImplement import UserRepoImplement


class WithdrawalResponse:
    user_repository = UserRepoImplement()

    def __init__(self):
        self.__account_number: str = ""
        self.__pin: int = 0
        self.__amount: decimal = 0.00

    def set_account_number(self, account_number: str):
        self.__account_number = account_number

    def get_account_number(self) -> str:
        return self.__account_number

    def set_pin(self, pin: int):
        self.__pin = pin

    def get_pin(self) -> int:
        return self.__pin

    def set_amount(self, amount: decimal):
        self.__amount = amount

    def get_amount(self) -> decimal:
        return self.__amount

    def __str__(self):
        return f"""
                     GEE-WALLET NIGERIA
        ==================================
        Account NUmber:{self.__account_number}
        Amount Withdrawn: {self.__amount}
        Account Balance : {self.user_repository.check_balance()}
        ==================================
        """
    