# Семинар 15. Обзор стандартной библиотеки Python.
#
# Задание №1. Логирование с использованием нескольких файлов.
#
# Напишите скрипт,
# который логирует разные типы сообщений в разные файлы.
# Логи уровня DEBUG и INFO должны сохраняться в debug_info.log,
# а логи уровня WARNING и выше — в warnings_errors.log.
#
# Решение:
from pathlib import Path
import logging
_PATH_1 = Path.cwd() / "output" / "task_1" / "debug_info.log"
_PATH_2 = Path.cwd() / "output" / "task_1" / "warnings_errors.log"
logging.basicConfig(format="{asctime}s – {name}s – {levelname}s – {message}s",
                    style='{',
                    level=logging.DEBUG)
log_format = logging.Formatter('%(asctime)s – %(name)s – %(levelname)s – %(message)s', datefmt='%H:%M:%S')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
debug_file_handler = logging.FileHandler(str(_PATH_1), 'a', encoding="utf-8")
debug_file_handler.setLevel(logging.DEBUG)
debug_file_handler.setFormatter(log_format)
logger.addHandler(debug_file_handler)
warning_file_handler = logging.FileHandler(str(_PATH_2), 'a', encoding="utf-8")
warning_file_handler.setLevel(logging.WARNING)
warning_file_handler.setFormatter(log_format)
logger.addHandler(warning_file_handler)
logger.debug("DEBAG message")
logger.info("INFO message")
logger.warning("WARNING message")
logger.error("ERROR mesage")
logger.critical("CRITICAL message")
