# import time
# import logging
# from utils.logger import create_session
# from bs4 import BeautifulSoup
# import textwrap
#
# def parse_and_replace_links(input_file, sleep_time, sleep_each):
#     sleep_count = 1
#     session = create_session()
#
#     # Чтение исходного файла
#     with open(input_file, 'r', encoding='utf-8') as f_in:
#         lines = f_in.readlines()
#
#     with open(input_file, 'w', encoding='utf-8') as f_out:
#         for line in lines:
#             # Считываем номер, ссылку и категорию
#             parts = line.split(' | ')
#             count = parts[0].strip()
#             url = parts[1].strip()
#             category = parts[2].strip()
#
#             # Отправляем запрос на статью
#             news_resp = session.get(url)
#             news_soup = BeautifulSoup(news_resp.text, 'lxml')
#
#             # Заголовок статьи
#             try:
#                 article_title = news_soup.find('div', class_="article__title").text.strip()
#             except AttributeError:
#                 article_title = news_soup.find('h1', class_="article__title").text.strip()
#
#             # Текст статьи
#             article_text = ''
#             for news_text in news_soup.find_all('div', class_="article__text"):
#                 wrapped_news_text = textwrap.wrap(news_text.text, width=70)
#                 article_text += '\n'.join(wrapped_news_text) + '\n'
#
#             # Записываем номер, тег и статью в новый файл
#             f_out.write(f"{count} | {category}\n")
#             f_out.write(f"{article_title}\n")
#             f_out.write(f"{article_text}\n")
#             logging.info("Ссылка №%s заменена на текст.", count)
#
#             # Пауза между запросами, чтобы избежать блокировки
#             if sleep_count == sleep_each:
#                 sleep_count = 0
#                 time.sleep(sleep_time)
#             sleep_count += 1
#
#     logging.info("Запись новостей в файл завершена")