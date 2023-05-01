from abc import ABC, abstractmethod

from data.model.Transactions import Transactions
from data.repository.TransactionRepository import TransactionRepository


class TransactionRepoImplement(TransactionRepository, ABC):
    transactions = []
    counter = 0

    @abstractmethod
    def save_transactions(self, transaction: Transactions) -> Transactions:
        self.transactions.append(transaction)
        self.counter += 1
        return transaction

    def count(self) -> int:
        return self.counter
