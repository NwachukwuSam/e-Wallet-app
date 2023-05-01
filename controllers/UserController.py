from dtos.request import UserRegistrationRequest
from services.UserServiceImpl import UserServiceImpl


class UserController:
    def __init__(self):
        self.user_services = UserServiceImpl()

    def create_account(self, create_account_request: UserRegistrationRequest):
        try:
            response = self.user_services.create_account(create_account_request)
            return response
        except ValueError as err:
            return str(err)

    def login(self, account_number, password):
        try:
            response = self.user_services.login(account_number, password)
            return response
        except ValueError as err:
            return str(err)

    def close_account(self, account_number, password):
        delete = self.user_services.close_account(account_number,password)
        return delete
    

