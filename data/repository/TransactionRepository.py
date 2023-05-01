from abc import abstractmethod

from data.model.Transactions import Transactions


class TransactionRepository:
    @abstractmethod
    def save_transactions(self, transaction: Transactions) -> Transactions:
        raise NotImplementedError

    def count(self) -> int:
        raise NotImplementedError
