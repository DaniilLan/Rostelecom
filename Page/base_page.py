from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Rostelecom.Page.config import URL
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.url = URL
        self.urlCODE = "https://start.rt.ru"

    def get_site(self):
        """Переход на URL."""
        return self.driver.get(self.url)

    def get_site_auth_code(self):
        """Переход на URL."""
        return self.driver.get(self.urlCODE)

    def find_element(self, locator, time=10):
        """Поиск элемента страницы по локатору."""
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator), message=f"Не удалось найти элемент {locator}"
        )

    def click_element(self, locator):
        """Клик по элементу локатора."""
        self.find_element(locator).click()

    def input_data(self, locator, text):
        """Ввод данных в поле ввода."""
        field = self.find_element(locator)
        field.send_keys(Keys.CONTROL + "a")
        field.send_keys(Keys.DELETE)
        field.send_keys(text)

    def get_text_content(self, locator, time=10):
        """Получить текст элемента"""
        return WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located(locator)).get_attribute("textContent")

    def get_url(self):
        """Получить url активного окна"""
        return self.driver.current_url

    def switch_to_new_window(self):
        """Переключение фокуса на новое окно страницы"""
        return self.driver.switch_to.window(self.driver.window_handles[1])

    def get_color_element(self, locator):
        """Получить цвет элемента"""
        return self.find_element(locator).get_attribute("color")

    def click_element_by_text(self, text):
        """Кликнуть по элементу с определённым текстом"""
        locator = (By.XPATH, f"//div[text()='{text}']")
        self.find_element(locator).click()

    def get_xpath(self, locator):
        """Получить XPATH элемента"""
        element = self.find_element(locator)
        return element.get_attribute("xpath")

