import fake_useragent
from requests import Session

def create_session():
    # Создает сессию с рандомным User-Agent.
    session = Session()
    user_agent = fake_useragent.UserAgent().random
    session.headers.update({'User-Agent': user_agent})
    return session