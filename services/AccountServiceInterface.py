from abc import abstractmethod

from dtos.request.DepositRequest import DepositRequest
from dtos.request.TransferRequest import TransferRequest
from dtos.request.WithdrawalRequest import WithdrawalRequest
from dtos.response.DepositResponse import DepositResponse
from dtos.response.TransferResponse import TransferResponse
from dtos.response.WithdrawalResponse import WithdrawalResponse


class AccountServiceInterface:

    @abstractmethod
    def deposit(self, deposit_request: DepositRequest) -> DepositResponse:
        pass

    @abstractmethod
    def withdraw(self, withdrawal_request: WithdrawalRequest) -> WithdrawalResponse:
        pass

    @abstractmethod
    def transfer(self, transfer_request: TransferRequest) -> TransferResponse:
        pass

    @abstractmethod
    def check_balance(self, account_number, password) -> str:
        pass
