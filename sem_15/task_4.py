# Семинар 15. Обзор стандартной библиотеки Python.

# Задание №4. Опции и флаги.

# Условие:
# Напишите скрипт,
# который принимает два аргумента командной строки:
# число и строку.
# Добавьте следующие опции:
# - --verbose, если этот флаг установлен, скрипт должен выводить
#   дополнительную информацию о процессе.
# - --repeat, если этот параметр установлен, он должен указывать,
#   сколько раз повторить строку в выводе.

# Решение:
import argparse
def func():
    parser = argparse.ArgumentParser()
    parser.add_argument("text", type=str)
    parser.add_argument("number", type=int)
    parser.add_argument("--verbose", action="store_true")
    parser.add_argument("repeat", type=int, default=1)
    args = parser.parse_args()
    if args.verbose:
        print(f'Полученные аргументы: '
              f'number={args.number}, text = "{args.text}", repeat = {args.repeat}')
    print(f'Число: {args.number}, Строка: {args.text *args.repeat}')


if __name__ == '__main__':
    func()
