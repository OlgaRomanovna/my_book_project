import allure
from helpers.user import olga
from my_book_project.pages.authorization_page import AuthorizationPage
from my_book_project.pages.main_page import MainPage


@allure.id("28432")
@allure.title("Проверка формы авторизации")
@allure.tag("authorization")
@allure.label("suite", "Авторизация")
@allure.label("owner", "allure8")
def test_authorization_form():
    main_page = MainPage()
    main_page.open()
    main_page.button_enter()
    authorization_page = AuthorizationPage()
    authorization_page.fill_email(olga.email)
    authorization_page.fill_password(olga.password)
    authorization_page.button_authorize()
    authorization_page.should_be_visible_email()


@allure.id("28433")
@allure.title("Проверка формы авторизации с невалидным паролем")
@allure.tag("authorization")
@allure.label("suite", "Авторизация")
@allure.label("owner", "allure8")
def test_authorization_form_with_wrong_password():
    main_page = MainPage()
    main_page.open()
    main_page.button_enter()
    authorization_page = AuthorizationPage()
    authorization_page.fill_email(olga.email)
    authorization_page.fill_password(olga.password[-1])
    authorization_page.button_authorize()
    authorization_page.should_be_error()
