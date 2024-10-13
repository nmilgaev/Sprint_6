import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.common.by import By

class OrderPage(BasePage):
    @allure.step("Заполняем первую часть формы заказа")
    def fill_order_form(self, name, surname, address, metro_station, phone):
        self.add_text_to_element(OrderPageLocators.NAME_INPUT, name)
        self.add_text_to_element(OrderPageLocators.SURNAME_INPUT, surname)
        self.add_text_to_element(OrderPageLocators.ADDRESS_INPUT, address)

        self.click_to_element(OrderPageLocators.STATION_INPUT)
        metro_option_locator = (
            By.XPATH, f'//div[contains(@class, "Order_Text__2broi") and text()="{metro_station}"]'
        )
        self.click_to_element(metro_option_locator)
        self.add_text_to_element(OrderPageLocators.PHONE_INPUT, phone)

    @allure.step("Заполняем вторую часть формы заказа")
    def fill_order_form_second_part(self, date, comment, color, rental_period):
        self.add_text_to_element(OrderPageLocators.DELIVERY_DATE_INPUT, date)

        if color == 'black':
            self.click_to_element(OrderPageLocators.BLACK_COLOR_CHECKBOX)
        elif color == 'grey':
            self.click_to_element(OrderPageLocators.GREY_COLOR_CHECKBOX)

        self.add_text_to_element(OrderPageLocators.COMMENT_INPUT, comment)
        self.click_to_element(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)

        if rental_period == 'сутки':
            self.click_to_element(OrderPageLocators.RENTAL_PERIOD_OPTION_SUTKI)
        else:
            self.click_to_element(OrderPageLocators.RENTAL_PERIOD_OPTION_DVOE_SUTOK)

    @allure.step("Нажимаем кнопку Далее")
    def click_next_button(self):
        self.click_to_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Нажимаем кнопку Заказать")
    def click_order_button(self):
        self.click_to_element(OrderPageLocators.ORDER_BUTTON)

    @allure.step("Подтверждаем заказ")
    def confirm_order(self):
        self.click_to_element(OrderPageLocators.CONFIRM_BUTTON)

    @allure.step("Получаем сообщение об успешном заказе")
    def get_success_message(self):
        return self.get_text_from_element(OrderPageLocators.SUCCESS_MESSAGE)

    @allure.step("Нажимаем кнопку 'Посмотреть статус'")
    def click_success_message_button(self):
        self.click_to_element(OrderPageLocators.SUCCESS_MESSAGE)


    @allure.step("Нажимаем на логотип Самоката")
    def click_scooter_logo(self):
        self.click_to_element(OrderPageLocators.SCOOTER_LOGO)

    @allure.step("Нажимаем на логотип Яндекса")
    def click_yandex_logo(self):
        self.click_to_element(OrderPageLocators.YANDEX_LOGO)
        self.driver.switch_to.window(self.driver.window_handles[1])