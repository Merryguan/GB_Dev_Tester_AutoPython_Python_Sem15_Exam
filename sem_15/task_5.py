# Семинар 15. Обзор стандартной библиотеки Python.

# Задание №5. Запуск из командной строки.

# Условие:
# Напишите код,
# который запускается из командной строки
# и получает на вход путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# - имя файла без расширения или название каталога,
# - расширение, если это файл,
# - флаг каталога,
# - название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя логирование.

# Решение:
from collections import namedtuple
from pathlib import Path
from os import walk, path
import logging
import argparse
_PATH_2 = Path.cwd() / "output" / "task_5" / "info.log"
logging.basicConfig(filename=str(_PATH_2), filemode='a', encoding="utf-8",
                    format="{levelname} - {asctime}s: {msg}",
                    style='{',
                    level=logging.INFO)
file = namedtuple("file",
                  ["name", "extension", "is_directory", "parent_directory"])
files = list()
def get_file_info(path_to_dir):
    if not path.isdir(path_to_dir):
        raise ValueError(f"Указанный путь {path_to_dir} не является директорией.")
    for dir_path, dir_names, file_names in walk(path_to_dir):
        for name in dir_names + file_names:
            file_path = path.join(dir_path, name)
            file_info = file(name.split('.')[0],
                             name.split('.')[1] if path.isfile(file_path) else None,
                             True if path.isdir(file_path) else False,
                             path.basename(dir_path))
            logging.info(f'{file_info.name} | '
                         f'{file_info.extension if file_info.extension else "N/A"} | '
                         f'{"Directory" if file_info.is_directory else "File"} | '
                         f'{file_info.parent_directory}')
            print(file_info)

def main():
    parser = argparse.ArgumentParser(description="Принимает путь до директории на ПК")
    parser.add_argument("path", type=str, help="Путь до директории для анализа")
    args = parser.parse_args()
    try:
        get_file_info(args.path)
        print(f'Информация о содержимом директории "{args.path}" '
              f'успешно записана в файл "directory_contents.log".')
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()