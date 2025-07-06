import pytest
import allure
from locators.logo_page_locators import LogoPageLocators
from pages.base_page import BasePage


class LogoPage(BasePage):

    @allure.step("Нажать на лого Самокат")
    # переход на главную по лого Самокат
    def open_page_by_logo_samokat(self):
        self.click_to_element(LogoPageLocators.LOGO_SAMOKAT)
        element = self.find_element_with_wait(LogoPageLocators.TITLE_SAMOKAT)
        return element.is_displayed()
    
    @allure.step("Нажать на лого Яндекс")       
    # переход в дзен по лого Яндекс
    def open_page_by_logo_yandex(self):
        self.click_to_element(LogoPageLocators.LOGO_YANDEX)
        self.open_new_tab()
        element = self.find_element_with_wait(LogoPageLocators.TITLE_DZEN)
        return element.is_displayed()