import logging
# from parser_RIA_News.scraper import fetch_and_categorize_links_to_file
from parser_Cyberleninka.scraper import fetch_links_to_file
from parser_Dzen.scraper import fetch_links_to_file1
date = 20231122

raw_data_path = './data/raw/'

BASE_URL = "https://ria.ru/"
CATEGORIES = [
    'Политика', 'Экономика', 'Общество', 'Происшествия', 'Армия',
    'Наука', 'Культура', 'Спорт', 'Туризм', 'Религия', 'В мире'
]
BASE_URL2 = "https://cyberleninka.ru/article/c/"

CATEGORIES2 = [
    'basic-medicine', 'clinical-medicine', 'health-sciences', 'health-biotechnology', 'mathematics',
    'computer-and-information-sciences', 'physical-sciences', 'chemical-sciences',
    'earth-and-related-environmental-sciences', 'biological-sciences', 'civil-engineering',
    'electrical-electronic-information-engineering', 'mechanical-engineering', 'chemical-engineering',
    'materials-engineering', 'medical-engineering', 'environmental-engineering', 'environmental-biotechnology',
    'industrial-biotechnology', 'nano-technology', 'history-and-archaeology', 'languages-and-literature',
    'philosophy-ethics-and-religion', 'arts-history-of-arts-performing-arts-music', 'agriculture-forestry-and-fisheries',
    'animal-and-dairy-science', 'veterinary-science', 'agricultural-biotechnology', 'psychology',
    'economics-and-business', 'educational-sciences', 'sociology', 'law',
    'political-science', 'social-and-economic-geography', 'media-and-communications'
]

def main():

    fetch_links_to_file1()
    # try:
    #     fetch_links_to_file(BASE_URL2, "basic-medicine", raw_data_path)
    # except Exception as e:
    #     logging.error("Критическая ошибка: %s", str(e))


if __name__ == "__main__":
    main()