from datetime import date
from datetime import datetime

def date_to_str(dt: date) -> str:
    return dt.strftime('%d/%m/%Y')

def str_to_date(dt: str) -> date:
    return datetime.strptime(dt, '%d/%m/%Y')

def format_float_as_currency(value: float) -> str:
    return f'R${value:,.2f}'

