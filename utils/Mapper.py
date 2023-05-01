from data.model.User import User
from dtos.request import UserRegistrationRequest
from dtos.request.DepositRequest import DepositRequest
from dtos.request.TransferRequest import TransferRequest
from dtos.request.WithdrawalRequest import WithdrawalRequest
from dtos.response.DepositResponse import DepositResponse
from dtos.response.TransferResponse import TransferResponse
from dtos.response.UserResponse import UserResponse
from dtos.response.WithdrawalResponse import WithdrawalResponse


class Mapper:

    @staticmethod
    def map_user_request(request: UserRegistrationRequest) -> User:
        user = User()
        user.set_first_name(request.get_first_name())
        user.set_last_name(request.get_last_name())
        user.set_phone_number(request.get_phone_number())
        user.set_email_address(request.get_email_address())
        user.set_account_number(request.get_account_number())
        user.set_id(request.get_id())
        user.set_password(request.get_password())
        return user

    @staticmethod
    def map_user_response(user: User):
        response = UserResponse()
        response.set_full_name(user.get_first_name()+" " + user.get_first_name())
        response.set_id(user.get_id())
        response.set_phone_number(user.get_phone_number())
        response.set_email_address(user.get_email_address())
        response.set_password(user.get_password())
        response.set_account_number(user.get_account_number())
        return response

    @staticmethod
    def map_deposit(deposit: DepositRequest):
        dep_response = DepositResponse()
        dep_response.set_receivers_account_number(deposit.get_receivers_account_number())
        dep_response.set_amount(deposit.get_amount())
        dep_response.set_purpose(deposit.get_purpose())
        return dep_response

    @staticmethod
    def map_withdrawal(withdraw: WithdrawalRequest):
        with_response = WithdrawalResponse()
        with_response.set_account_number(withdraw.get_account_number())
        with_response.set_amount(withdraw.get_amount())
        return with_response

    @staticmethod
    def map_transfer(transfer: TransferRequest):
        trans_response = TransferResponse()
        trans_response.set_senders_account(transfer.get_senders_account_number())
        trans_response.set_receivers_account(transfer.get_receivers_account_number())
        trans_response.set_amount_to_transfer(transfer.get_amount_to_transfer())
        trans_response.set_remark(transfer.get_purpose())
        return trans_response
