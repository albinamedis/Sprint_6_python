from data import  url_main_page, answers_data 
from selenium import webdriver
from pages.main_page import MainPage
import pytest
import allure 


class TestMainPage:

    driver = None

    @classmethod
    def setup_class(cls):
        # создали драйвер для браузера Firefox
        cls.driver = webdriver.Firefox()

    @allure.title('Проверка ответа на вопрос')
    @allure.description('')
    @pytest.mark.parametrize('num', [0,1,2,3,4,5,6,7])
    def test_question_and_answer(self, num):
        main_page = MainPage(self.driver)
        main_page.go_to_url(url_main_page)
        text = main_page.check_question_and_answer(num)
        assert text  == answers_data[num], f'Ответ на вопрос №{num} не совпадает с ожидаемым'

    @classmethod
    def teardown_class(cls):
        # Закрой браузер
        cls.driver.quit()