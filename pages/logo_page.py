import pytest
import allure
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class LogoPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Нажать на лого Самокат")
    # переход на главную по лого Самокат
    def open_page_by_logo_samokat(self):
        self.click_to_element(OrderPageLocators.LOGO_SAMOKAT)
        element = self.find_element_with_wait(OrderPageLocators.TITLE_SAMOKAT)
        return element.is_displayed()
    
    @allure.step("Нажать на лого Яндекс")       
    # переход в дзен по лого Яндекс
    def open_page_by_logo_yandex(self):
        self.click_to_element(OrderPageLocators.LOGO_YANDEX)
        # Получаем дескрипторы всех окон
        window_handles = self.driver.window_handles
        # Переключаемся на новую вкладку (последняя добавленная)
        self.driver.switch_to.window(window_handles[-1])
        element = self.find_element_with_wait(OrderPageLocators.TITLE_DZEN)
        return element.is_displayed()