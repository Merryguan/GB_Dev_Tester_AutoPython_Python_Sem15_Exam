# Семинар 15. Обзор стандартной библиотеки Python.

# Задание №3. Планирование задач.

# Условие:
# Напишите функцию,
# которая принимает количество дней от текущей даты
# и возвращает дату, которая наступит через указанное количество дней.
# Дополнительно, выведите эту дату в формате YYYY-MM-DD.

# Решение:
from datetime import datetime, timedelta
def future_date(days_from_now):
    return (datetime.now() + timedelta(days=days_from_now)).strftime('%Y-%m-%d')


if __name__ == '__main__':
    days = 30 # Количество дней для вычисления
    print(f'Date {days} days from now: {future_date(days)}')