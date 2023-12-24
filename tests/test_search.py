from my_book_project.pages.main_page import MainPage
from my_book_project.pages.search_page import SearchPage


def test_search_string():
    main_page = MainPage()
    main_page.open()
    search_page = SearchPage()
    search_page.fill_search_string()
    search_page.choose_first_book()
    search_page.should_be_visible_name_book()