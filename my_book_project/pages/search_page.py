import allure
from selene import browser, have


class SearchPage:
    def fill_search_string(self):
        with allure.step("Заполнение поля Пароль"):
            browser.element(".ant-col-lg-order-2 .ant-input").send_keys("Мартин Иден")

    def choose_first_book(self):
        with allure.step("Выбираем первую книгу"):
            browser.element("div:nth-child(2) > div:nth-child(1) div:nth-child(1) > div.e4xwgl-1.gEQwGK > a").click()

    def should_be_visible_name_book(self):
        with allure.step("Проверяем, что открылась выбранная нами книга"):
            browser.element(".bzVsYa").should(have.exact_text("Мартин Иден"))
