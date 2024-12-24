from bs4 import BeautifulSoup
from utils.logger import setup_logger
from utils.session_manager import create_session
from utils.string_utils import re_search
from utils.file_manager import initialize_folder, export_list_to_file



def fetch_links_to_file(base_url, category, output_dir):
    logger = setup_logger('scrapper', 'logs/file_export.log')
    logger.info("Начало парсинга ссылок с сайта: %s", base_url)

    session = create_session()  # Создание сессии
    links = []  # Список для сохранения ссылок и категорий

    page_count = 1
    last_page_count = None
    url = f"{base_url}{category}"

    while True:
        try:
            if page_count > 1:
                url = f"{base_url}{category}/{page_count}"
            logger.info("Обработка страницы: %s", url)
            response = session.get(url)

            soup = BeautifulSoup(response.text, 'lxml')

            # Поиск основного блока со ссылками
            content = soup.find('div', class_ = "content")
            if not content:
                logger.warning("Не удалось найти блок с содержимым на странице %s", url)
                break

            # Определение номера последней страницы
            if page_count == 1:
                try:
                    paginator = content.find('ul', class_="paginator")
                    last_page_count = re_search(paginator.find('a', class_="icon").get('href'),r'(\d+)$', logger)
                except Exception as e:
                    logger.error("Ошибка при нахождении номера последней страницы %s: %s", url, str(e))
                    break

            article_list = content.find('ul', class_ = "list")
            if not article_list:
                logger.warning("Не удалось найти список с содержимым на странице %s", url)
                break

            # Поиск новостей на текущей странице
            link_on_page = 1  # Счётчик ссылок на странице
            for item in article_list.find_all('a'):
                link = item.get('href')

                # Формат записи: "page:link_on_page | ссылка | категории"
                link_number = f"{page_count}:{link_on_page}"

                links_line = f"{link_number} | {link} "
                links.append(links_line)
                logger.info("Ссылка №%s обработана.", link_number)

                link_on_page += 1

            # Проверка, достигли ли последней страницы
            if page_count >= last_page_count:
                logger.info("Достигнута последняя страница: %s", page_count)
                break

            page_count += 1

        except Exception as e:
            logger.error("Ошибка при обработке веб-страницы %s: %s", url, str(e))
            break

    # Сохранение всех ссылок с номерами в файл
    dir_pass = initialize_folder(output_dir, "КиберЛенинка",logger)
    news_file = export_list_to_file(links, dir_pass, category, logger)

    # Сохранение текста статей в файл
    #parse_and_replace_links(news_file, 1, 3)