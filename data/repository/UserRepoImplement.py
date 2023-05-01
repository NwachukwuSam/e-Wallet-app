from abc import ABC

from data.model.User import User
from data.repository.UserRepository import UserRepository


class UserRepoImplement(UserRepository, ABC):
    users: list[User] = []
    counter = 0

    # def save_user(self, user: User) -> User:
    #     if user.get_id() == 0:
    #         new_user = user.set_id(self.generate_user_id())
    #         account_number = self.generate_account_number(user.get_phone_number())
    #         user.set_account_number(account_number)
    #         self.users.append(new_user)
    #         self.counter += 1
    #         return user

    def save_user(self, user: User) -> User:
        if user.get_id() == 0:
            user.set_id(self.generate_user_id())
            account_number = self.generate_account_number(user.get_phone_number())
            user.set_account_number(account_number)
        self.users.append(user)
        self.counter += 1
        return user

    def generate_user_id(self) -> int:
        return self.counter + 1

    @staticmethod
    def generate_account_number(phone_number: str) -> str:
        account_number = phone_number.lstrip("0")
        return account_number

    def find_user_by_account_number(self, account_number: str) -> User:
        for user in self.users:
            if user.get_account_number() == account_number:
                return user

    def check_balance(self, ) -> User:
        for user in self.users:
            return user.get_balance()

    def delete_user_by_account_number(self, account_number: str) -> None:
        for user in self.users:
            if user.get_account_number() == account_number:
                self.users.remove(user)
                self.counter -= 1
                break

    def count(self):
        return self.counter
