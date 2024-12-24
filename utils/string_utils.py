import re


def re_search (string, pattern, logger):
    # Используем регулярное выражение для поиска числа в конце строки
    re_pattern = re.compile(pattern)
    match = re_pattern.search(string)
    logger.info("Объект %s извлечен из текста.", match.group(1))
    if match:
        return match.group(1)
    else:
        return None