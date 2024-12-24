import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name, log_file, level=logging.INFO):
    # Создаем каталог для логов, если его нет
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    # Очищаем файл логов при старте
    with open(log_file, 'w', encoding="utf-8"):
        pass

    # Создаем логгер
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Удаляем предыдущие обработчики, чтобы избежать дублирования сообщений
    if logger.hasHandlers():
        logger.handlers.clear()

    # Формат сообщений
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # Обработчик записи в файл с ротацией и кодировкой UTF-8
    file_handler = RotatingFileHandler(
        log_file, maxBytes=5 * 1024 * 1024, backupCount=3, encoding="utf-8"
    )
    file_handler.setFormatter(formatter)

    # Обработчик для вывода логов в консоль
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # Добавляем обработчики к логгеру
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger