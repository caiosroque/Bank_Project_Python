from datetime import date
from utils.helper import date_to_str, str_to_date

class Client:
    counter: int = 101

    def __init__(self: object, name: str, email: str, cpf: str, date_of_birth: str) -> None:
        self.__code: int = Client.counter
        self.__name: str = name
        self.__email: str = email
        self.__cpf: str = cpf
        self.__date_of_birth: date = str_to_date(date_of_birth)
        self.__registration_date: date = date.today()
        Client.counter += 1

    @property
    def code(self: object) -> int:
        return self.__code

    @property
    def name(self: object) -> str:
        return self.__name

    @property
    def email(self: object) -> str:
        return self.__email

    @property
    def cpf(self: object) -> str:
        return self.__cpf

    @property
    def date_of_birth(self: object) -> str:
        return date_to_str(self.__date_of_birth)

    @property
    def registration_date(self: object) -> str:
        return date_to_str(self.__registration_date)

    def __str__(self: object) -> str:
        return f'Code: {self.code} \nName: {self.name} \nDate of Birth: {self.date_of_birth} \nRegistration Date: {self.registration_date}'

