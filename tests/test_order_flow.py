import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import ORDER_DATA
import time

class TestOrderFlow:

    @allure.description("Проверяем позитивный сценарий заказа самоката с двумя наборами данных и разными точками входа")
    @pytest.mark.parametrize("order_data, button_position", [
        (ORDER_DATA[0], "top"),
        (ORDER_DATA[1], "bottom"),
    ])
    def test_order_flow(self, driver, order_data, button_position):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.click_cookie_button()

        if button_position == "top":
            main_page.click_order_button_top()
        else:
            main_page.click_order_button_bottom()

        order_page.fill_order_form(
            name=order_data["name"],
            surname=order_data["surname"],
            address=order_data["address"],
            metro_station=order_data["metro_station"],
            phone=order_data["phone"]
        )

        order_page.click_next_button()

        order_page.fill_order_form_second_part(
            comment=order_data["comment"],
            date = order_data["date"],
            color=order_data["color"],
            rental_period=order_data["rental_period"]
        )

        order_page.click_order_button()

        order_page.confirm_order()

        success_message = order_page.get_success_message()
        assert "Посмотреть статус" in success_message

        order_page.click_success_message_button()

        order_page.click_scooter_logo()
        time.sleep(5)
        assert driver.current_url == "https://qa-scooter.praktikum-services.ru/"
        driver.back()

        order_page.click_yandex_logo()
        time.sleep(5)
        driver.switch_to.window(driver.window_handles[1])
        assert driver.current_url == "https://dzen.ru/?yredirect=true"