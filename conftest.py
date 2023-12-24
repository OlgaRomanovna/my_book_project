import pytest
from selene import browser


@pytest.fixture(scope="function", autouse=True)
def browser_management():
    browser.config.base_url = "https://mybook.ru"
    browser.config.window_width = 1200
    browser.config.window_height = 1080