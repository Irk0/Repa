#
# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from .pages.main_page import MainPage
# from .pages.login_page import LoginPage
#
#
# def test_guest_can_go_to_login_page(browser):
#     link = "http://selenium1py.pythonanywhere.com"
#     page = MainPage(browser, link)
#     # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
#     page.open()  # открываем страницу
#     login_page = page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логина
#     # запускаем метод перехода на страницу логина (тест отработал и вернул новый объект Page)
#     login_page.should_be_login_page() # запускаем проверку, что это именно логин пейдж
#
# def test_guest_should_see_login_link(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     page = MainPage(browser, link)
#     # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
#     page.open() # открываем страницу
#     page.should_be_login_link() # выполняем метод страницы — переходим на страницу логина
#
# def test_page_logrega(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
#     page = LoginPage(browser, link)
#     page.open()
#     page.should_be_login_page()

from pages.login_page import LoginPage
from pages.main_page import MainPage

import pytest


link = "http://selenium1py.pythonanywhere.com"


class TestLoginFromMainPage():

    def test_guest_can_go_to_login_page(self, browser):

        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()