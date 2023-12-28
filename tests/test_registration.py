import allure
from helpers import resources
from my_book_project.pages.main_page import MainPage
from my_book_project.pages.registration_page import RegistrationPage


@allure.id("28434")
@allure.title("Проверка формы регистрации")
@allure.tag("registration")
@allure.label("suite", "Регистрация")
@allure.label("owner", "allure8")
def test_registration_form():
    main_page = MainPage()
    main_page.open()
    main_page.button_enter()
    registration_page = RegistrationPage()
    registration_page.button_registration()
    registration_page.fill_email(resources.email)
    registration_page.fill_password(resources.password)
    registration_page.button_register()
    registration_page.should_have_text()


@allure.id("28435")
@allure.title("Проверка формы регистрации с невалидной электронной почтой")
@allure.tag("registration")
@allure.label("suite", "Регистрация")
@allure.label("owner", "allure8")
def test_registration_form_with_invalid_email():
    main_page = MainPage()
    main_page.open()
    main_page.button_enter()
    registration_page = RegistrationPage()
    registration_page.button_registration()
    registration_page.fill_email(resources.email[3])
    registration_page.fill_password(resources.password)
    registration_page.button_register()
    registration_page.should_be_error()

