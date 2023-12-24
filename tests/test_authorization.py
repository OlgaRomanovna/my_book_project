from helpers.user import olga
from my_book_project.pages.authorization_page import AuthorizationPage
from my_book_project.pages.main_page import MainPage


def test_authorization_form():
    main_page = MainPage()
    main_page.open()
    main_page.button_enter()
    authorization_page = AuthorizationPage()
    authorization_page.fill_email(olga.email)
    authorization_page.fill_password(olga.password)
    authorization_page.button_authorize()
    authorization_page.should_be_visible_email()

def test_authorization_form_with_wrong_password():
    main_page = MainPage()
    main_page.open()
    main_page.button_enter()
    authorization_page = AuthorizationPage()
    authorization_page.fill_email(olga.email)
    authorization_page.fill_password(olga.password[-1])
    authorization_page.button_authorize()
    authorization_page.should_be_error()
