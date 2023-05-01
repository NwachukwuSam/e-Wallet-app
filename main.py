import sys
import tkinter as tk
from tkinter import messagebox, simpledialog
import re

from controllers.AccountController import AccountController
from controllers.UserController import UserController
from dtos.request.DepositRequest import DepositRequest
from dtos.request.TransferRequest import TransferRequest
from dtos.request.UserRegistrationRequest import UserRepositoryRequest
from dtos.request.WithdrawalRequest import WithdrawalRequest

user_controller = UserController()
account_controller = AccountController()


def input_collector(prompt):
    root = tk.Tk

    collect_input = tk.simpledialog.askstring(title="Gee-Wallet", prompt=prompt)
    return collect_input


def display(prompt):
    messagebox.showinfo("Gee Wallet Nigeria", prompt)


def register_page():
    page = """
      WELCOME TO GEE-WALLET
    =========================
    1. Login
    2. Create Account
    3. Exit Application
    ========================="""
    user_input = input_collector(page)

    if user_input == "1":
        login()
    elif user_input == "2":
        create_account()
    elif user_input == "3":
        exit_application()
    else:
        register_page()


def login():
    account_number = input_collector("Enter Your Account Number: ")
    password = input_collector("Enter Your Password: ")
    login_response = user_controller.login(account_number, password)
    display(login_response)
    home_page()


def create_account():
    register_user = UserRepositoryRequest()
    first_name = input_collector("Enter Your First Name: ")
    last_name = input_collector("Enter Your Last Name: ")
    email = input_collector("Enter Your Email: ")
    while True:
        phone_number = input_collector("Enter your valid Phone Number")
        if validate_nigerian_phone_number(phone_number):
            break
        else:
            display("Invalid Phone Number. Please Enter a Valid Nigerian Phone Number.")
    password = input_collector("Create A Password: ")
    register_user.set_first_name(first_name)
    register_user.set_last_name(last_name)
    register_user.set_email_address(email)
    register_user.set_phone_number(phone_number)
    register_user.set_password(password)

    response = user_controller.create_account(register_user)
    display(response)
    register_page()


def exit_application():
    display("Thank You For Banking with Gee-Wallet Africa")
    sys.exit()


def home_page():
    home = """
    =============================
    1. Deposit
    2. Withdraw
    3. Transfer
    4. Check Balance
    5. Logout
    =============================="""
    user_input = input_collector(home)
    if user_input == "1":
        deposit()
    elif user_input == "2":
        withdraw()
    elif user_input == "3":
        transfer()
    elif user_input == "4":
        check_balance()
    elif user_input == "5":
        register_page()
    else:
        print("Wrong Input! Enter A Valid Input")
    home_page()


def deposit():
    deposit_request = DepositRequest()
    account_number = input_collector("Enter Your Account Number: ")
    amount = float(input_collector("Enter Amount: "))
    deposit_request.set_receivers_account_number(account_number)
    deposit_request.set_amount(amount)
    response = account_controller.deposit(deposit_request)
    display(response)
    home_page()


def withdraw():
    withdraw_request = WithdrawalRequest()
    account_number = input_collector("Enter Your Account Number: ")
    amount = float(input_collector("Enter The Amount You want to Withdraw: "))
    withdraw_request.set_account_number(account_number)
    withdraw_request.set_amount(amount)
    response = account_controller.withdraw(withdraw_request)
    display(response)
    home_page()


def transfer():
    transfer_request = TransferRequest()
    senders_account = input_collector("Enter Sender's Account: ")
    receivers_account = input_collector("Enter Receiver's Account Number: ")
    amount = float(input_collector("Enter Amount: "))
    remark = input_collector("Add A Remark: ")
    transfer_request.set_senders_account(senders_account)
    transfer_request.set_receivers_account(receivers_account)
    transfer_request.set_amount_to_transfer(amount)
    transfer_request.set_remark(remark)
    response = account_controller.transfer(transfer_request)
    display(response)
    home_page()


def check_balance():
    account_number = input_collector("Enter Account Number: ")
    password = input_collector("Enter Password: ")
    response = account_controller.check_balance(account_number, password)
    display(response)
    home_page()


def validate_nigerian_phone_number(phone_number):
    pattern = r"^(080|081|090|070|091)\d{8}$"
    return bool(re.match(pattern, phone_number))


def validate_email_address(email):
    pat = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pat, email))


if __name__ == '__main__':
    register_page()
