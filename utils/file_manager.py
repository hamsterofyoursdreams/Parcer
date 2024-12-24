import os

def initialize_folder(folder_path, folder_name, logger):
    # Создает папку, если она не существует.
    path = os.path.join(folder_path, folder_name)
    os.makedirs(path, exist_ok=True)
    logger.info(f"Папка '{folder_name}' {'уже существовала' if os.path.exists(path) else 'успешно создана'}.")
    return path


def export_list_to_file(item_list, file_path, file_name, logger):
    # Экспортирует список в текстовый файл.
    file_path = os.path.join(file_path, f"{file_name}.txt")
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines([f"{item}\n" for item in item_list])
    logger.info("Данные из списка '%s' сохранены в файл: %s", repr(item_list), file_name)
    return file_path