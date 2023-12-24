import allure
from selene import browser, have, be
from helpers import resources
from helpers.user import olga


class RegistrationPage:

    def button_registration(self):
        with allure.step("Кнопка Зарегистрироваться"):
            browser.element('.j8igyq-5 button.ant-btn').click()

    def fill_email(self, email):
        with allure.step("Заполнение поля Электронная почта"):
            browser.element('.cy-registration-email-input input.ant-input').send_keys(email)

    def fill_password(self, password):
        with allure.step("Заполнение поля Пароль"):
            browser.element(".cy-registration-password-input input.ant-input").send_keys(password)

    def button_register(self):
        with allure.step("Кнопка Зарегистрироваться"):
            browser.element(".ant-btn-primary").click()

    def should_have_text(self):
        with allure.step("Проверяем, что регистрация прошла успешно"):
            browser.element(".ant-btn.ant-btn-link").should(
                be.visible)

    def should_be_error(self):
        with allure.step(""):
            browser.element("div:nth-child(1) > div.ant-form-item-control > div.ant-form-item-explain > div").should(have.exact_text("Введите правильный адрес электронной почты."))