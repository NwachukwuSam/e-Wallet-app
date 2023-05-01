from abc import ABC

from data.repository.UserRepoImplement import UserRepoImplement
from dtos.request.DepositRequest import DepositRequest
from dtos.request.TransferRequest import TransferRequest
from dtos.request.WithdrawalRequest import WithdrawalRequest
from dtos.response.DepositResponse import DepositResponse
from dtos.response.TransferResponse import TransferResponse
from dtos.response.WithdrawalResponse import WithdrawalResponse
from services.AccountServiceInterface import AccountServiceInterface
from utils.Mapper import Mapper


class AccountServiceInterfaceImpl(AccountServiceInterface, ABC):
    user_repository = UserRepoImplement()

    def deposit(self, deposit_request: DepositRequest) -> DepositResponse:
        if not self.account_not_found(deposit_request.get_receivers_account_number()):
            raise ValueError("Account Not found..")
        receiver_account = self.user_repository.find_user_by_account_number(
            deposit_request.get_receivers_account_number())
        response = Mapper.map_deposit(deposit_request)
        receiver_account.set_deposit(deposit_request.get_amount())
        return response

    def account_not_found(self, account):
        account_number = self.user_repository.find_user_by_account_number(account)
        if account_number is not None:
            return True
        return False

    def check_balance(self, account_number, password) -> str:
        account = self.user_repository.find_user_by_account_number(account_number)
        if account.get_password() == password:
            return account.get_first_name()+"  " + account.get_last_name() + " " + \
                   "Your Account Balance is "+str(account.get_balance())
        else:
            raise ValueError("Invalid Account Details or Password")

    def withdraw(self, withdrawal_request: WithdrawalRequest) -> WithdrawalResponse:
        if not self.account_not_found(withdrawal_request.get_account_number()):
            raise ValueError("Account Not Found..")
        account = self.user_repository.find_user_by_account_number(withdrawal_request.get_account_number())
        response = Mapper.map_withdrawal(withdrawal_request)
        account.set_withdraw(withdrawal_request.get_amount())
        return response

    def transfer(self, transfer_request: TransferRequest) -> TransferResponse:
        sender_account = self.user_repository.find_user_by_account_number(transfer_request.get_senders_account_number())
        receiver_account = self.user_repository.find_user_by_account_number(transfer_request.get_receivers_account_number())
        if sender_account is None and receiver_account is None:
            raise ValueError("Account Not Found")
        if sender_account is receiver_account:
            raise ValueError("Sender's Account cannot be same as Receiver's Account")
        sender_account.set_withdraw(transfer_request.get_amount_to_transfer())
        receiver_account.set_deposit(transfer_request.get_amount_to_transfer())
        transfer_response = Mapper.map_transfer(transfer_request)
        return transfer_response
