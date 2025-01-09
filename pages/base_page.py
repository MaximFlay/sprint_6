import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Проскроллить до элемента')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    @allure.step('Ожидание  прогрузки элемента')
    def wait_visibility_of_element(self, locator):
        return WebDriverWait(self.driver, 6).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Кликнуть на элемент')
    def click_on_element(self, locator):
        element = WebDriverWait(self.driver, 8).until(expected_conditions.element_to_be_clickable(locator))
        element.click()
        #self.driver.find_element(*locator).click()

    @allure.step('Ввести значение в поле ввода')
    def send_keys_to_input(self, locator, keys):
        self.driver.find_element(*locator).send_keys(keys)

    @allure.step('Получить текст на элементе')
    def get_text_on_element(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step('Перейти на другую вкладку')
    def switch_to_next_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Проверить отображение элемента')
    def check_displaying_of_element(self, locator):
        return self.driver.find_element(*locator).is_displayed()
