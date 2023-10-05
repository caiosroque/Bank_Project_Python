from models.client import Client
from models.account import Account

Caio: Client = Client('Caio Roque', 'caiosroque@gmail.com', '123.456.78-01', '28/02/2003')
CaioFelipe: Client = Client('Caio Felipe', 'caiofelipe@gmail.com', '123.456.78-01', '28/02/2003')

contaf: Account = Account(Caio)
contaa: Account = Account(CaioFelipe)

print(contaa)
print(contaf)
