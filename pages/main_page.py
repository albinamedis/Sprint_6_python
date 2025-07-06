from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
import allure 

class MainPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
    
    @allure.step('Нажать на вопрос')
    def click_to_question(self, num):
        self.scroll_to_element(MainPageLocators.FAQ)
        locator_q_formated = self.format_locators(MainPageLocators.OPEN_QUESTION, num)
        self.click_to_element(locator_q_formated)

    @allure.step('Получить ответ на вопрос')
    def get_answer_text(self, num):
        locator_a_formated =  self.format_locators(MainPageLocators.TEXT_ANSWER, num)
        return self.get_text_from_element(locator_a_formated)
    
    @allure.step('Проверить ответ на вопрос')
    def check_question_and_answer(self, num):
        self.click_to_question(num)
        return self.get_answer_text(num)