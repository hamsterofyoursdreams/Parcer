# import logging
# from bs4 import BeautifulSoup
# from utils.logger import create_session, export_dict_to_file, initialize_folder
# from parser_RIA_News.parser import parse_and_replace_links
#
#
# def fetch_and_categorize_links_to_file(base_url, date, categories, output_dir):
#
#     logging.info("Начало парсинга ссылок с сайта: %s", base_url)
#
#     session = create_session()  # Создание сессии
#     links_with_categories = []  # Список для сохранения ссылок и категорий
#
#     page_count = 1
#     last_page_count = None
#     url = f"{base_url}{date}/"
#
#     while True:
#         try:
#             if page_count > 1:
#                 url = f"{base_url}{date}/?page={page_count}"
#             logging.info("Обработка страницы: %s", url)
#             response = session.get(url)
#
#             soup = BeautifulSoup(response.text, 'lxml')
#
#             # Поиск основного блока со ссылками
#             content = soup.find('div', id = "content")
#             if not content:
#                 logging.warning("Не удалось найти блок с содержимым на странице %s", url)
#                 break
#
#             # Определение номера последней страницы
#             if page_count == 1:
#                 try:
#                     last_page_count = content.find_all('a', class_="list-pager__item color-btn")[-1].text
#                 except Exception as e:
#                     logging.error("Ошибка при нахождении номера последней страницы %s: %s", url, str(e))
#                     break
#
#             # Поиск новостей на текущей странице
#             link_on_page = 1  # Счётчик ссылок на странице
#             for item in content.find_all('div', class_="list-item"):
#                 link = item.find('a', class_="list-item__title color-font-hover-only").get('href')
#                 found_categories = []
#
#                 # Классификация ссылки по категориям
#                 for tag in item.find_all('a', class_="list-tag"):
#                     category = tag.text
#                     if category in categories:
#                         if category not in found_categories:
#                             found_categories.append(category)
#
#                 # Формат записи: "page:link_on_page | ссылка | категории"
#                 link_number = f"{page_count}:{link_on_page}"
#                 if found_categories:
#                     category_str = ', '.join(found_categories)
#                 else:
#                     category_str = "Без категории"
#
#                 links_with_categories_line = f"{link_number} | {link} | {category_str}"
#                 links_with_categories.append(links_with_categories_line)
#                 logging.info("Ссылка №%s обработана.", link_number)
#
#                 link_on_page += 1
#
#             # Проверка, достигли ли последней страницы
#             if page_count >= int(last_page_count):
#                 logging.info("Достигнута последняя страница: %s", page_count)
#                 break
#
#             page_count += 1
#
#         except Exception as e:
#             logging.error("Ошибка при обработке веб-страницы %s: %s", url, str(e))
#             break
#
#     # Сохранение всех ссылок с номерами в файл
#     dir_pass = initialize_folder(output_dir, "РИА Новости")
#     news_file = export_dict_to_file(links_with_categories, dir_pass,"Ссылки с категориями", date)
#
#     # Сохранение текста статей в файл
#     parse_and_replace_links(news_file, 1, 3)