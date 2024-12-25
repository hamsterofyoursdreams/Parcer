from bs4 import BeautifulSoup
from utils.string_utils import re_search
from utils.logger import setup_logger
from utils.session_manager import create_session


def fetch_links_to_file1():
    logger = setup_logger('scrapper', 'logs/file_export.log')
    # logger.info("Начало парсинга ссылок с сайта: %s", base_url)

    session = create_session()  # Создание сессии
    links = []  # Список для сохранения ссылок и категорий

    page_count = 1
    url = "https://dzen.ru/topic/beauty?tab=articles"

    while True:
        try:
            logger.info("Обработка страницы: %s", url)

            response = session.get(url)

            # Поиск ссылки на следующую страницу
            if page_count == 1:

                soup = BeautifulSoup(response.text, 'lxml')

                article_list = soup.find('div', class_="desktop2--adaptive-card-grid__container-2l desktop2--adaptive-card-grid__isNewGridFloorsDesktop-2R desktop2--adaptive-card-grid__isGridDense-2I desktop2--adaptive-card-grid__noVerticalSpace-2r")
                if not article_list:
                    logger.warning("Не удалось найти список с содержимым на странице %s", url)
                    break

                # Поиск новостей на текущей странице
                link_on_page = 1  # Счётчик ссылок на странице
                for item in article_list.find_all('a', rel = "opener dofollow"):
                    link = item.get('href')

                    # Формат записи: "page:link_on_page | ссылка | категории"
                    link_number = f"{page_count}:{link_on_page}"

                    links_line = f"{link_number} | {link} "
                    links.append(links_line)
                    logger.info("Ссылка №%s обработана.", link_number)

                    link_on_page += 1
                try:
                    script = soup.find_all('script')[13].text
                    url = re_search(script, r'"more":\{"link":"(https://[^"]+)"', logger)
                except Exception as e:
                    logger.error("Ошибка при нахождении ссылки на следующую страницу %s: %s", url, str(e))
                    break
            else:
                json_data = response.json()

                link_on_page = 1
                for item in json_data['items']:
                    link = item['shareLink']

                    # Формат записи: "page:link_on_page | ссылка | категории"
                    link_number = f"{page_count}:{link_on_page}"

                    links_line = f"{link_number} | {link} "
                    links.append(links_line)
                    logger.info("Ссылка №%s обработана.", link_number)

                    link_on_page += 1
                try:
                    url = json_data['more']['link']
                except Exception as e:
                    logger.error("Ошибка при нахождении ссылки на следующую страницу %s: %s", url, str(e))
                    break
            page_count += 1

        except Exception as e:
            logger.error("Ошибка при обработке веб-страницы %s: %s", url, str(e))
            break

    # # Сохранение всех ссылок с номерами в файл
    # dir_pass = initialize_folder(output_dir, "КиберЛенинка",logger)
    # news_file = export_list_to_file(links, dir_pass, category, logger)

    # Сохранение текста статей в файл
    #parse_and_replace_links(news_file, 1, 3)