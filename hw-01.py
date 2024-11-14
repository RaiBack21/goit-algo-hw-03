import re
from datetime import datetime
from random import sample

 # Task 1
def get_days_from_today(date):
    """
    Calculates the number of days between the given date and the current date.
    """
    today = datetime.today().date()
    try:
        date = datetime.strptime(date, "%Y-%m-%d").date()
        result = date - today
        return result.days
    except ValueError:
        return "Неправильний формат вхідних даних"

 # Task 2
def get_numbers_ticket(min, max, quantity):
    """
    Generates a random set of numbers within the given parameters.
    """
    if 1 <= min < max <= 1000 and (max + 1) - min >= quantity:
        numbers_ticket = sample(range(min, max+1), quantity)
        numbers_ticket.sort()
        return numbers_ticket
    else:
        return []

 # Task 3
def normalize_phone(number):
    """
    Normalizes the phone number
    """
    number = re.sub('[^0-9,+]', "", number)
    if number.startswith("38"):
        number = '+' + number
    elif number.startswith("0"):
        number = '+38' + number
    else:
        number = number

    return number


print(get_days_from_today('2024-11-14'))

# print(get_numbers_ticket(51, 55, 5))

# raw_numbers = [
#     "067\\t123 4567",
#     "(095) 234-5678\\n",
#     "+380 44 123 4567",
#     "380501234567",
#     "    +38(050)123-32-34",
#     "     0503451234",
#     "(050)8889900",
#     "38050-111-22-22",
#     "38050 111 22 11   ",
# ]

# sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
# print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)