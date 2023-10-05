from models.client import Client
from utils.helper import format_float_as_currency

class Account:

    code: int = 1001

    def __init__(self: object, client: Client) -> None:
        self.__number: int = Account.code
        self.__client: Client = client
        self.__balance: float = 0.0
        self.__limit: float = 100.0
        self.__total_balance: float = self._calculate_total_balance
        Account.code += 1

    def __str__(self: object) -> str:
        return f'Account Number: {self.number} \nClient: {self.client.name} \nTotal Balance: {format_float_as_currency(self.total_balance)}'

    @property
    def number(self: object) -> int:
        return self.__number

    @property
    def client(self: object) -> Client:
        return self.__client

    @property
    def balance(self: object) -> float:
        return self.__balance

    @balance.setter
    def balance(self: object, value: float) -> None:
        self.__balance = value

    @property
    def limit(self: object) -> float:
        return self.__limit

    @limit.setter
    def limit(self: object, value: float) -> None:
        self.__limit = value

    @property
    def total_balance(self: object) -> float:
        return self.__total_balance

    @total_balance.setter
    def total_balance(self: object, value: float) -> None:
        self.__total_balance = value

    @property
    def _calculate_total_balance(self: object) -> float:
        return self.balance + self.limit

    def deposit(self: object, value: float) -> None:
        if value > 0:
            self.balance += value
            self.total_balance = self._calculate_total_balance()
            print("Deposit successful")
        else:
            print('Error: Unable to make the deposit. Please try again.')

    def withdraw(self: object, value: float) -> None:
        if value > 0 and self.total_balance >= value:
            if self.balance >= value:
                self.balance -= value
                self.total_balance = self._calculate_total_balance()
            else:
                remaining: float = self.balance - value
                self.limit += remaining
                self.balance = 0
                self.total_balance = self._calculate_total_balance()
                print('Withdrawal successful')
        else:
            print('Withdrawal not performed. Please try again.')

    def transfer(self: object, destination: object, value: float) -> None:
        if value > 0 and self.total_balance >= value:
            if self.balance >= value:
                self.balance -= value
                self.total_balance = self._calculate_total_balance()
                destination.balance += value
                destination.total_balance = destination._calculate_total_balance()
            else:
                remaining: float = self.balance - value
                self.balance = 0
                self.limit += remaining
                self.total_balance = self._calculate_total_balance()
                destination.balance += value
                destination.total_balance = destination._calculate_total_balance()
            print("Transfer successful")
        else:
            print("Transfer not performed. Please try again.")
