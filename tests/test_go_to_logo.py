from data import url_zakaz
from selenium import webdriver
from pages.logo_page import LogoPage
import allure 
import pytest

class TestLogo:

    driver = None

    @classmethod
    def setup_class(cls):
        # создали драйвер для браузера Firefox
        cls.driver = webdriver.Firefox()

    @allure.title('Переход по лого на Главную')
    def test_go_to_logo_samokat(self):
        logo_page = LogoPage(self.driver)
        logo_page.go_to_url(url_zakaz)
        assert logo_page.open_page_by_logo_samokat() == True

    @allure.title('Переход по лого в Дзен')
    def test_go_to_logo_yandex(self):
        logo_page = LogoPage(self.driver)
        logo_page.go_to_url(url_zakaz)
        assert logo_page.open_page_by_logo_yandex() == True

    @classmethod
    def teardown_class(cls):
        # Закрой браузер
        cls.driver.quit()