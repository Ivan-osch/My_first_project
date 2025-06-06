import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    options = Options()
    language = request.config.getoption("language")
    if language:
        print("\nstart chrome browser for test..")
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("укажите язык интерфейса")
    yield browser
    print("\nquit browser..")
    browser.quit()
