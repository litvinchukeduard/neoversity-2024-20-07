'''
Написати декоратор, який буде аргументи-рядки перетворювати на datetime
'''
from datetime import datetime
from functools import wraps

def convert_str_to_datetime(func):
    @wraps(func)
    def internal(first_date, second_date):
        if type(first_date) == str and type(second_date) == str:
            first_datetime = datetime.strptime(first_date, '%Y-%m-%d')
            second_datetime = datetime.strptime(second_date, '%Y-%m-%d')
            return func(first_datetime, second_datetime)
        return func(first_date, second_date)
    return internal


# calculate_difference_between_dates('2024-07-20', '2024-07-25')
@convert_str_to_datetime
def calculate_difference_between_dates(first_date: datetime, second_date: datetime) -> int:
    return (second_date - first_date).days

# print(calculate_difference_between_dates('2024-07-20', '2024-07-25'))
# calculate_difference_between_dates()
# print(dir(calculate_difference_between_dates))
print(calculate_difference_between_dates.__name__)