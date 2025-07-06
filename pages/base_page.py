from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 5
        self.wait = WebDriverWait(self.driver, self.timeout)

    def go_to_url(self, url):
        self.driver.get(url)

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)
    
    def click_to_element(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    def format_locators(self, locator_1, num):
        # locator_1 = By.ID, 'accordion__heading-{}'
        method, locator = locator_1
        locator = locator.format(num)
        return method, locator
    
    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def open_new_tab(self):
        # Получаем дескрипторы всех окон
        window_handles = self.driver.window_handles
        # Переключаемся на новую вкладку (последняя добавленная)
        self.driver.switch_to.window(window_handles[-1])

    # # метод перетаскивания элемента для диплома
    # def my_drag_and_drop(self, locator_from,locator_to):
    #     elem_from = self.find_element_with_wait(locator_from)
    #     elem_to = self.find_element_with_wait(locator_to)

    #     self.driver.drag_and_drop(elem_from, elem_to).perform()