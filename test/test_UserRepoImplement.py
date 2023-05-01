from unittest import TestCase

from data.model.User import User
from data.repository.UserRepoImplement import UserRepoImplement


class TestUserRepoImplement(TestCase):

    def test_save_user(self):
        user_repository = UserRepoImplement()
        user = User()
        user.set_phone_number("08064615767")
        user_repository.save_user(user)
        print(user.get_account_number())
        self.assertEqual(1, user_repository.count())
        print(user_repository.count())

    def test_that_more_than_one_user_can_be_saved(self):
        user_repository = UserRepoImplement()
        first_user = User()
        second_user = User()
        first_user.set_phone_number("0901234567")
        second_user.set_phone_number("0801234567")

        user_repository.save_user(first_user)
        user_repository.save_user(second_user)
        self.assertEqual(2, user_repository.count())

    def test_find_user(self):
        user_repository = UserRepoImplement()
        user = User()
        user.set_phone_number("0901234567")
        user_repository.save_user(user)
        self.assertEqual(user, user_repository.find_user_by_account_number("901234567"))

    def test_that_users_can_be_deleted(self):
        user_repository = UserRepoImplement()
        user = User()
        user.set_phone_number("0901234567")
        user_repository.save_user(user)
        user_repository.delete_user_by_account_number("901234567")
        self.assertEqual(0, user_repository.count())

    def test_that_one_of_two_users_can_be_deleted(self):
        user_repository = UserRepoImplement()
        first_user = User()
        second_user = User()
        first_user.set_phone_number("0901234567")
        second_user.set_phone_number("0801234567")
        user_repository.save_user(first_user)
        user_repository.save_user(second_user)
        user_repository.delete_user_by_account_number("801234567")
        self.assertEqual(1, user_repository.count())

