import allure
from allure import step
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):
    URL = "https://qa-scooter.praktikum-services.ru/"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(self.URL)

    @allure.step('Кликаем на вопрос')
    def click_to_question(self, num):
        locator_q_formatted = self.format_locator(MainPageLocators.QUESTION_LOCATOR, num)
        locator_8_formatted = self.format_locator(MainPageLocators.QUESTION_LOCATOR_8, 7)
        self.scroll_to_element(locator_8_formatted)
        self.click_to_element(locator_q_formatted)

    @allure.step('Получаем текст с ответа')
    def get_answer_text(self, num):
        locator_a_formatted = self.format_locator(MainPageLocators.ANSWER_LOCATOR, num)
        self.click_to_question(num)
        return self.get_text_from_element(locator_a_formatted)

    @allure.step('Нажимаем на кнопку принятия куков')
    def click_cookie_button(self):
        self.click_to_element(MainPageLocators.COOKIE_BUTTON)

    @allure.step('Нажимаем на верхнюю кнопку заказать')
    def click_order_button_top(self):
        self.click_to_element(MainPageLocators.ORDER_BUTTON_TOP_LOCATOR)

    @allure.step('Нажимаем на нижнюю кнопку заказать')
    def click_order_button_bottom(self):
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_BOTTOM_LOCATOR)
        self.click_to_element(MainPageLocators.ORDER_BUTTON_BOTTOM_LOCATOR)
