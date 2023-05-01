from abc import ABC

from data.model.User import User
from data.repository.UserRepoImplement import UserRepoImplement
from dtos.request import UserRegistrationRequest

from dtos.response import UserResponse
from services.UserService import UserService
from utils.Mapper import Mapper


class UserServiceImpl(UserService, ABC):
    user_repository = UserRepoImplement()
    user = User()

    def __init__(self):
        pass

    def create_account(self, create_request: UserRegistrationRequest) -> UserResponse:
        if self.phone_number_exist(create_request.get_phone_number()):
            raise ValueError(create_request.get_phone_number() + " " + "already Exist")

        account = Mapper.map_user_request(create_request)
        saved_account = self.user_repository.save_user(account)
        response = Mapper.map_user_response(saved_account)
        return response

    def phone_number_exist(self, phone_number):
        phone_number = self.user_repository.find_user_by_account_number(phone_number)
        if phone_number is not None:
            return True
        return False

    def login(self, account_number: str, password: str):
        account = self.user_repository.find_user_by_account_number(account_number)
        if account.get_password() == password:
            return True
        else:
            raise ValueError("Invalid Account or Password")

    def close_account(self, account_number: str, password: str):
        account = self.user_repository.find_user_by_account_number(account_number)
        if account.get_password() == password:
            self.user_repository.delete_user_by_account_number(account_number)
