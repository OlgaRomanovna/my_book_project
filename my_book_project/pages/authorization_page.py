import allure
from selene import browser, have

from helpers.user import olga


class AuthorizationPage:

    def fill_email(self, email):
        with allure.step("Заполнение поля Электронная почта"):
            browser.element('.cy-login-email-input').send_keys(email)

    def fill_password(self, password):
        with allure.step("Заполнение поля Пароль"):
            browser.element(".cy-login-password-input input.ant-input").send_keys(password)

    def button_authorize(self):
        with allure.step("Кнопка Зарегистрироваться"):
            browser.element(".ant-btn-primary").click()

    def should_be_visible_email(self):
        with allure.step("Проверяем, что авторизация прошла успешно"):
            browser.element(".ant-col-lg-offset-0 .ffCvOR").click()
            browser.element(".sc-1au9i1l-5.jqIPic").should(have.exact_text("o.lgaro...@yandex.ru"))

    def should_be_error(self):
        with allure.step("проверить, что ошибка появляется"):
            browser.element("div.ant-form-item-has-error > div.ant-form-item-control > div.ant-form-item-explain > div").should(have.exact_text("Неверно введен пароль."))