from selenium.webdriver.common.by import By


class MainPageLocators:
    FAQ = [By.XPATH, "//div[text()='Вопросы о важном']"]
    OPEN_QUESTION = [By.ID, 'accordion__heading-{}']
    TEXT_ANSWER = [By.ID, 'accordion__panel-{}']