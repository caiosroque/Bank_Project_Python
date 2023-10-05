from typing import List
import time
from models.client import Client
from models.account import Account

accounts: List[Account] = []

def main() -> None:
    menu()

def menu() -> None:
    print("================================================")
    print("======================BANK======================")
    print("================================================")
    print("Select an option from the menu:")
    print('1 - Create an account')
    print('2 - Withdraw')
    print('3 - Deposit')
    print('4 - Transfer')
    print('5 - List accounts')
    print('6 - Exit the system')
    print("================================================")

    option: int = int(input("Enter an option -> "))
    
    if option == 1:
        print("Option 1 selected")
        time.sleep(1)
        create_account()
    elif option == 2:
        withdraw()
    elif option == 3:
        deposit()
    elif option == 4:
        transfer()
    elif option == 5:
        list_accounts()
    elif option == 6:
        print("Thanks for using our services...")
        time.sleep(2)
        print("Ending session...")
        time.sleep(6)
        exit(0)
    else:
        print("Invalid option")
        time.sleep(2)
        menu()

def create_account() -> None:
    print("Provide customer information:")

    name: str = input('Customer name: ')
    email: str = input('Customer email: ')
    cpf: str = input('Customer CPF: ')
    date_of_birth: str = input("Customer date of birth: ")

    client: Client = Client(name, email, cpf, date_of_birth)
    account: Account = Account(client)
    accounts.append(account)
    print("Account created successfully")
    print("Account details:")
    print("-----------------------")
    print(account)
    time.sleep(2)
    menu()

def withdraw() -> None:
    if len(accounts) > 0:
        number: int = int(input("Enter your account number: "))
        account: Account = find_account_by_number(number)

        if account: 
            amount: float = float(input("Enter the withdrawal amount: "))
            account.withdraw(amount)
        else:
            print(f"Account with number {number} not found")

    else:
        print('No accounts registered yet')
    time.sleep(2)
    menu()

def deposit() -> None:
    if len(accounts) > 0:
        number: int = int(input("Enter your account number: "))
        account: Account = find_account_by_number(number)

        if account:
            amount: float = float(input("Enter the deposit amount: "))
            account.deposit(amount)

        else:
            print(f'Account with number {number} not found')
    
    else:
        print("")
    time.sleep(2)
    menu()

def transfer() -> None:
    if len(accounts) > 0:
        source_number = int(input("Enter your account number: "))
        source_account: Account = find_account_by_number(source_number)

        if source_account:
            destination_number: int = int(input("Enter the destination account number: "))
            destination_account: Account = find_account_by_number(destination_number)

            if destination_account:
                amount: float = float(input("Enter the transfer amount: "))
                source_account.transfer(destination_account, amount)
            else:
                print(f"Destination account with number {destination_number} not found")

        else:
            print(f"Source account with number {source_number} not found")
    else:
        print("No accounts registered yet")
    time.sleep(2)
    menu()

def list_accounts() -> None:
    if len(accounts) > 0:
        print('List of accounts')

        for account in accounts:
            print(account)
            print('-----------------------------------------------')
            time.sleep(1)
    else:
        print("No accounts registered yet.")
    time.sleep(2)
    menu()

def find_account_by_number(number: int) -> Account:
    found_account: Account = None

    if len(accounts) > 0:
        for account in accounts:
            if account.number == number: 
                found_account = account
    return found_account 

if __name__ == '__main__':
    main()
