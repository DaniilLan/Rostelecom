import pytest
from selenium.common.exceptions import TimeoutException
from config import *


@pytest.mark.parametrize('password', [valid_password, invalid_password, empty_password])
class TestAuth:
    # Тест - 29, 30, 31
    def test_auth_phone(self, auth, password):
        auth.click_element(auth.TAB_PHONE)
        auth.input_data(auth.INPUT_USERNAME, valid_phone)
        auth.input_data(auth.INPUT_PASSWORD, password)
        auth.click_element(auth.BTN_LOGIN)
        if password == valid_password:
            assert auth.find_element(auth.BTN_EXIT), "Ошибка авторизации пользователя"
        elif password == invalid_password:
            assert auth.find_element(auth.ERROR_PASS), "Отсутствует или не найден блок с ошибкой"
        elif password == empty_password:
            try:
                assert auth.find_element(auth.ERROR_PASS)
            except TimeoutException:
                pass

    # Тест - 36, 37, 38
    def test_auth_email(self, auth, password):
        auth.click_element(auth.TAB_EMAIL)
        auth.input_data(auth.INPUT_USERNAME, valid_email)
        auth.input_data(auth.INPUT_PASSWORD, password)
        auth.click_element(auth.BTN_LOGIN)
        if password == valid_password:
            assert auth.find_element(auth.BTN_EXIT), "Ошибка авторизации пользователя"
        elif password == invalid_password:
            assert auth.find_element(auth.ERROR_PASS), "Отсутствует или не найден блок с ошибкой"
        elif password == empty_password:
            try:
                assert auth.find_element(auth.ERROR_PASS)
            except TimeoutException:
                pass

    # Тест - 39, 40, 41
    def test_auth_login(self, auth, password):
        auth.click_element(auth.TAB_LOGIN)
        auth.input_data(auth.INPUT_USERNAME, valid_login)
        auth.input_data(auth.INPUT_PASSWORD, password)
        auth.click_element(auth.BTN_LOGIN)
        if password == valid_password:
            assert auth.find_element(auth.BTN_EXIT), "Ошибка авторизации пользователя"
        elif password == invalid_password:
            assert auth.find_element(auth.ERROR_PASS), "Отсутствует или не найден блок с ошибкой"
        elif password == empty_password:
            try:
                assert auth.find_element(auth.ERROR_PASS)
            except TimeoutException:
                pass

    # Тест - 42, 43, 44
    def test_auth_ls(self, auth, password):
        auth.click_element(auth.TAB_LS)
        auth.input_data(auth.INPUT_USERNAME, valid_ls)
        auth.input_data(auth.INPUT_PASSWORD, password)
        auth.click_element(auth.BTN_LOGIN)
        if password == valid_password:
            assert auth.find_element(auth.BTN_EXIT), "Ошибка авторизации пользователя"
        elif password == invalid_password:
            assert auth.find_element(auth.ERROR_PASS), "Отсутствует или не найден блок с ошибкой"
        elif password == empty_password:
            try:
                assert auth.find_element(auth.ERROR_PASS)
            except TimeoutException:
                pass


class TestOpenSocial:

    # Тест - 22
    def test_open_vk(self, auth):
        auth.click_element(auth.SOC_VK)
        assert auth.find_element(auth.VK_ID)

    # Тест - 23
    def test_open_ok(self, auth):
        auth.click_element(auth.SOC_OK)
        assert auth.find_element(auth.OK_ID)

    # Тест - 24
    def test_open_mail(self, auth):
        auth.click_element(auth.SOC_MAIL)
        assert auth.find_element(auth.MAIL_ID)

    # Тест - 25
    def test_open_yandex(self, auth):
        auth.click_element(auth.SOC_YANDEX)
        auth.click_element(auth.SOC_YANDEX)
        assert auth.find_element(auth.YANDEX_ID)


# Тест - 21
class TestPlaceholder:

    def test_placeholder_phone(self, auth):
        auth.click_element(auth.TAB_PHONE)
        text = auth.get_text_content(auth.PLACEHOLDER_USERNAME)
        assert text == "Мобильный телефон"

    def test_placeholder_email(self, auth):
        auth.click_element(auth.TAB_EMAIL)
        text = auth.get_text_content(auth.PLACEHOLDER_USERNAME)
        assert text == "Электронная почта"

    def test_placeholder_login(self, auth):
        auth.click_element(auth.TAB_LOGIN)
        text = auth.get_text_content(auth.PLACEHOLDER_USERNAME)
        assert text == "Логин"

    def test_placeholder_ls(self, auth):
        auth.click_element(auth.TAB_LS)
        text = auth.get_text_content(auth.PLACEHOLDER_USERNAME)
        assert text == "Лицевой счёт"


class TestPageTransition:

    # Тест - 26
    def test_go_to_page_password_recovery(self, auth):
        auth.click_element(auth.LINK_FORGOT_PASSWORD)
        assert auth.find_element(auth.ID_PASSWORD_RECOVERY)

    # Тест - 27
    def test_go_to_page_registration(self, auth):
        auth.click_element(auth.LINK_REGISTER)
        assert auth.find_element(auth.ID_REGISTER)

    # Тест - 28
    def test_go_to_page_user_agr_reg(self, auth):
        auth.click_element(auth.LINK_USER_AGR)
        auth.switch_to_new_window()
        assert auth.get_url() == 'https://b2c.passport.rt.ru/sso-static/agreement/agreement.html'


# Тест - 18
def test_change_color_link(auth):
    element_before = auth.find_element(auth.LINK_FORGOT_PASSWORD)
    color_before = element_before.value_of_css_property('color')
    auth.input_data(auth.INPUT_USERNAME, valid_phone)
    auth.input_data(auth.INPUT_PASSWORD, invalid_password)
    auth.click_element(auth.BTN_LOGIN)
    element_after = auth.find_element(auth.LINK_FORGOT_PASSWORD)
    color_after = element_after.value_of_css_property('color')
    assert color_before != color_after and color_after == 'rgba(255, 79, 18, 1)'


# Тест - 13
def test_default_tab(auth):
    element = auth.find_element(auth.TAB_PHONE)
    assert element.value_of_css_property('color') == 'rgba(255, 79, 18, 1)'


