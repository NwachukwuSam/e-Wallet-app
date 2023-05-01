from dtos.request.DepositRequest import DepositRequest
from dtos.request.TransferRequest import TransferRequest
from dtos.request.WithdrawalRequest import WithdrawalRequest
from services.AccountServiceInterfaceImpl import AccountServiceInterfaceImpl


class AccountController:

    def __init__(self):
        self.account_services = AccountServiceInterfaceImpl()

    def deposit(self, deposit_request: DepositRequest ):
        try:
            response = self.account_services.deposit(deposit_request)
            return response
        except ValueError as err:
            return str(err)

    def withdraw(self, withdraw_request: WithdrawalRequest):
        try:
            response = self.account_services.withdraw(withdraw_request)
            return response
        except ValueError as err:
            return str(err)

    def transfer(self, transfer_request: TransferRequest):
        try:
            response = self.account_services.transfer(transfer_request)
            return response
        except ValueError as err:
            return str(err)

    def check_balance(self, account_number, password):
        try:
            response = self.account_services.check_balance(account_number,password)
            return response
        except ValueError as err:
            return str(err)
