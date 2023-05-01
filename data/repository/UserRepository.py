from abc import abstractmethod, ABC

from data.model.User import User


class UserRepository(ABC):
    @abstractmethod
    def save_user(self, user: User) -> User:
        pass

    @abstractmethod
    def find_user_by_account_number(self, account_number: str) -> User:
        pass

    @abstractmethod
    def delete_user_by_account_number(self, account: str) -> None:
        raise NotImplementedError
