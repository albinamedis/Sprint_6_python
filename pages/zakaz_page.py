import pytest
import allure
# from data import url_samokat
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class ZakazPage(BasePage):

    @allure.step("Заполнение формы об арендателе")
    def set_data_who(self, data):
        self.click_to_element(OrderPageLocators.NAME)
        self.add_text_to_element(OrderPageLocators.NAME, data['name'])
        self.click_to_element(OrderPageLocators.SURNAME)
        self.add_text_to_element(OrderPageLocators.SURNAME, data['surname'])
        self.click_to_element(OrderPageLocators.ADRESS)
        self.add_text_to_element(OrderPageLocators.ADRESS, data['adress'])
        self.click_to_element(OrderPageLocators.METRO_LIST)
        self.click_to_element(OrderPageLocators.METRO_STATION)
        self.click_to_element(OrderPageLocators.PHONE)
        self.add_text_to_element(OrderPageLocators.PHONE, data['phone'])

    @allure.step("Нажать далее")
    def next_click(self):
        self.click_to_element(OrderPageLocators.BUTTON_NEXT)
        self.find_element_with_wait(OrderPageLocators.TITLE_ARENDA)    

    @allure.step("Заполнение формы когда и какой самокат нужен")
    def input_data_when(self, data):
        self.click_to_element(OrderPageLocators.OPEN_KALENDAR)
        self.click_to_element(OrderPageLocators.DATE)
        self.click_to_element(OrderPageLocators.OPEN_PERIOD_ARENDA)
        self.click_to_element(OrderPageLocators.TWO_DAYS)
        self.click_to_element(OrderPageLocators.COLOR)
        self.click_to_element(OrderPageLocators.COMMENT)
        self.add_text_to_element(OrderPageLocators.COMMENT, data['comment'])
    
    @allure.step("Оформить и подтвердить заказ")
    def zakaz_and_yes_click(self):
        # Нажать заказать
        self.click_to_element(OrderPageLocators.BUTTON_ZAKAZ)
        self.find_element_with_wait(OrderPageLocators.MODAL_AGREE)
        # Подтвердить заказ
        self.click_to_element(OrderPageLocators.BUTTON_YES)
        
    @allure.step("Проверяем, что заказ успешно оформлен")
    def check_status_order_sucsses(self):
        return self.get_text_from_element(OrderPageLocators.TITLE_SUCSSES)
        
    