from abc import ABC

from data.model.Account import Account
from data.repository.AccountRepository import AccountRepository


class AccountRepositoryImplement(AccountRepository, ABC):
    account_balance = Account()

    def check_balance(self: Account):
        self.get_balance()
