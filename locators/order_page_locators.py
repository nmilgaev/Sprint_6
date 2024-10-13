from selenium.webdriver.common.by import By

class OrderPageLocators:
    # Локаторы для полей формы заказа
    NAME_INPUT = By.XPATH, '//*[@placeholder="* Имя"]'
    SURNAME_INPUT = By.XPATH, '//*[@placeholder="* Фамилия"]'
    ADDRESS_INPUT = By.XPATH, '//*[@placeholder="* Адрес: куда привезти заказ"]'
    STATION_INPUT = By.XPATH, '//*[@placeholder="* Станция метро"]'
    PHONE_INPUT = By.XPATH, '//*[@placeholder="* Телефон: на него позвонит курьер"]'
    NEXT_BUTTON = By.XPATH, '//button[contains(@class, "Button_Button__ra12g")][text()="Далее"]'
    DELIVERY_DATE_INPUT = By.XPATH, '//*[@placeholder="* Когда привезти самокат"]'
    RENTAL_PERIOD_DROPDOWN = By.XPATH, '//div[contains(@class, "Dropdown-placeholder")][text()="* Срок аренды"]'
    RENTAL_PERIOD_OPTION_SUTKI = By.XPATH, '//div[@class="Dropdown-menu"]/div[text()="сутки"]'
    RENTAL_PERIOD_OPTION_DVOE_SUTOK = By.XPATH, '//div[@class="Dropdown-menu"]/div[text()="двое суток"]'
    BLACK_COLOR_CHECKBOX = By.ID, 'black'
    GREY_COLOR_CHECKBOX = By.ID, 'grey'
    COMMENT_INPUT = By.XPATH, '//*[@placeholder="Комментарий для курьера"]'
    ORDER_BUTTON = By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM" and text()="Заказать"]'
    CONFIRM_BUTTON = By.XPATH, '//button[contains(@class, "Button_Button__ra12g")][text()="Да"]'
    SUCCESS_MESSAGE = By.XPATH, '//button[contains(@class, "Button_Button__ra12g")][text()="Посмотреть статус"]'
    SCOOTER_LOGO = By.XPATH, '//img[@alt="Scooter"]'
    YANDEX_LOGO = By.XPATH, '//a[contains(@href, "//yandex.ru")]//img'
