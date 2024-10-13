import allure
import pytest
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from data import ANSWERS



class TestMainPage:

    @allure.description('Проверяем, что при клике на вопрос ответ правильный')
    @pytest.mark.parametrize(
        'num, result',
        [(i, ANSWERS[i]) for i in range(8)]  # Параметризуем тест для всех вопросов
    )
    def test_questions_and_answers(self, driver, num, result):
        main_page = MainPage(driver)
        assert main_page.get_answer_text(num) == result  # Проверяем, что текст ответа соответствует ожиданиям

