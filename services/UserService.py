from data.model.User import User
from dtos.request import UserRegistrationRequest
from dtos.response.UserResponse import UserResponse


class UserService:
    def create_account(self, request: UserRegistrationRequest) -> UserResponse:
        raise NotImplementedError

    def find_account(self, account_number: str) -> User:
        raise NotImplementedError

    def close_account(self, account_number: str, password:str):
        raise NotImplementedError

    def login(self, account_number: str, password: str):
        raise NotImplementedError
