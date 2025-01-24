# Семинар 15. Обзор стандартной библиотеки Python.

# Задание №2. Работа с текущим временем и датой.

# Условие:
# Напишите скрипт,
# который получает текущее время и дату,
# а затем выводит их в формате YYYY-MM-DD HH:MM:SS.
# Дополнительно,
# выведите день недели и номер недели в году.

# Решение:
from datetime import datetime
def display_current_datetime():
    data = datetime.now()
    print(f"Текущее время и дата: {data.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"День недели: {data.strftime('%A')}")
    print(f"Номер недели: {data.isocalendar()[1]}")


if __name__ == '__main__':
    display_current_datetime()
