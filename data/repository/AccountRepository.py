from abc import abstractmethod


class AccountRepository:

    @abstractmethod
    def view_balance(self):
        pass
