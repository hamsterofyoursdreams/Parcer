from setuptools import setup, find_packages

setup(
    name="parser_RIA_News",  # Имя проекта
    version="0.1.0",  # Версия проекта
    packages=find_packages(),
    install_requires=[  # Список зависимостей
        'beautifulsoup4==4.12.3',
        'certifi==2023.11.17',
        'charset-normalizer==3.3.2',
        'fake-useragent==1.5.1',
        'idna==3.6',
        'lxml==5.3.0',
        'requests==2.31.0',
        'setuptools==75.6.0',
        'soupsieve==2.6',
        'tqdm==4.66.1',
        'urllib3==2.1.0',
    ],
)