from data import url_samokat, order_data_1, order_data_2, text_sucsses
from selenium import webdriver
from pages.zakaz_page import ZakazPage
from locators.order_page_locators import OrderPageLocators
import allure 
import pytest


class TestZakazSamokata:

    driver = None

    @classmethod
    def setup_class(cls):
        # создали драйвер для браузера Firefox
        cls.driver = webdriver.Firefox()


    @allure.title('Создание заказа')
    @allure.description('')
    @pytest.mark.parametrize('locator, order_data', 
        [
            (OrderPageLocators.ZAKAZ_UP, order_data_1),
            (OrderPageLocators.ZAKAZ__DOWN, order_data_2)
        ])
    def test_create_order(self, locator, order_data):
        zakaz_page = ZakazPage(self.driver)
        zakaz_page.go_to_url(url_samokat)
        zakaz_page.scroll_to_element(locator)
        zakaz_page.click_to_element(locator)
        zakaz_page.set_data_who(order_data)
        zakaz_page.next_click()
        zakaz_page.input_data_when(order_data)
        zakaz_page.zakaz_and_yes_click()
        text = zakaz_page.check_status_order_sucsses()
        assert text_sucsses in text

    @classmethod
    def teardown_class(cls):
        # Закрой браузер
        cls.driver.quit()