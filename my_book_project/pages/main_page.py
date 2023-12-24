import allure
from selene import browser, have


class MainPage:

    def open(self):
        with allure.step("Открыть браузер"):
            browser.open("/")

    def button_enter(self):
        with allure.step("Кнопка Войти"):
            browser.element('.ant-col-lg-offset-0 a.cy-login-button').click()


