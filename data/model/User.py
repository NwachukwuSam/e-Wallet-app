import decimal


class User:

    def __init__(self):
        self.__id = 0
        self.__first_name: str = " "
        self.__last_name: str = ""
        self.__phone_number: str = ""
        self.__email_address: str = ""
        self.__account_number: str = ""
        self.__password: str = ""
        self.__balance: decimal = 0.0
        self.__deposit: decimal = 0.0
        self.__withdraw: decimal = 0.0
        self.__transfer: decimal = 0.0

    def set_id(self, identity_number: int):
        self.__id = identity_number

    def get_id(self) -> int:
        return self.__id

    def set_first_name(self, first_name: str):
        self.__first_name = first_name

    def get_first_name(self) -> str:
        return self.__first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def get_last_name(self) -> str:
        return self.__last_name

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def get_phone_number(self) -> str:
        return self.__phone_number

    def set_email_address(self, email_address):
        self.__email_address = email_address

    def get_email_address(self) -> str:
        return self.__email_address

    def set_account_number(self, account_number: str):
        self.__account_number = account_number

    def get_account_number(self) -> str:
        return self.__account_number

    def set_password(self, password):
        self.__password = password

    def get_password(self) -> str:
        return self.__password

    def get_balance(self) -> decimal:
        return self.__balance

    def set_deposit(self, amount: decimal):
        if amount > 0:
            self.__balance = self.__balance + amount
        else:
            self.__balance = self.__balance

    def get_deposit(self) -> decimal:
        return self.__deposit

    def set_withdraw(self, amount):
        if 0 < amount < self.__balance:
            self.__balance = self.__balance - amount
        else:
            self.__balance = self.__balance

    def get_withdraw(self) -> decimal:
        return self.__withdraw

    def set_transfer(self, amount ):
        self.__transfer = amount

    def get_transfer(self) -> decimal:
        return self.__transfer
