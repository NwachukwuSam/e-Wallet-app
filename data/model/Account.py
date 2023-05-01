import decimal


class Account:

    def __init__(self):
        self.__balance: decimal = 0.0
        self.__deposit: decimal = 0.0
        self.__withdraw: decimal = 0.0
        self.__transfer: decimal = 0.0

    def get_balance(self) -> decimal:
        return self.__balance

    def set_deposit(self, amount):
        self.__balance = self.__balance + amount

    def get_deposit(self) -> decimal:
        return self.__deposit

    def set_withdraw(self, amount):
        self.__balance = self.__balance - amount

    def get_withdraw(self) -> decimal:
        return self.__withdraw

    def set_transfer(self, amount):
        self.__transfer = amount

    def get_transfer(self) -> decimal:
        return self.__transfer
