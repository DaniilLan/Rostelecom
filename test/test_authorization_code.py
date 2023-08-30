import re
import pytest
from config import *
from time import sleep


# Тест - 51, 52 (Прохождение теста может занять > 2 минут)
@pytest.mark.parametrize('phone_email', [valid_phone, valid_email])
def test_get_code_for_login(auth_code, phone_email):
    auth_code.input_data(auth_code.INPUT_EMAIL_PHONE, phone_email)
    if 'Отправка' in auth_code.get_text_content(auth_code.MESSAGE_LIMITATIONS):
        seconds = auth_code.get_text_content(auth_code.MESSAGE_LIMITATIONS)
        seconds = re.search(r'\d+', seconds).group()
        sleep(int(seconds))
    auth_code.click_element(auth_code.BTN_GET_CODE)
    if phone_email == valid_phone:
        assert 'Изменить номер' == auth_code.get_text_content(auth_code.CHANGE_PH_and_EM)
    elif phone_email == valid_email:
        assert 'Изменить почту' == auth_code.get_text_content(auth_code.CHANGE_PH_and_EM)


# Тест - 61, 67 (Прохождение теста может занять > 2 минут)
@pytest.mark.parametrize('phone_email', [valid_phone, valid_email])
def test_change_phone(auth_code, phone_email):
    auth_code.input_data(auth_code.INPUT_EMAIL_PHONE, phone_email)
    if 'Отправка' in auth_code.get_text_content(auth_code.MESSAGE_LIMITATIONS):
        seconds = auth_code.get_text_content(auth_code.MESSAGE_LIMITATIONS)
        seconds = re.search(r'\d+', seconds).group()
        sleep(int(seconds))
    auth_code.click_element(auth_code.BTN_GET_CODE)
    auth_code.click_element(auth_code.CHANGE_PH_and_EM)
    assert auth_code.find_element(auth_code.ID_AUTH_CODE)


# Тест - 54
def test_btn_log_password(auth_code):
    auth_code.click_element(auth_code.BTN_LOG_WITH_PASSWORD)
    assert auth_code.find_element(auth_code.ID_AUTH_PASSWORD)


class TestOpenSocial:

    # Тест - 55
    def test_open_vk(self, auth_code):
        auth_code.click_element(auth_code.SOC_VK)
        assert auth_code.find_element(auth_code.VK_ID)

    # Тест - 56
    def test_open_ok(self, auth_code):
        auth_code.click_element(auth_code.SOC_OK)
        assert auth_code.find_element(auth_code.OK_ID)

    # Тест - 57
    def test_open_mail(self, auth_code):
        auth_code.click_element(auth_code.SOC_MAIL)
        assert auth_code.find_element(auth_code.MAIL_ID)

    # Тест - 58
    def test_open_yandex(self, auth_code):
        auth_code.click_element(auth_code.SOC_YANDEX)
        auth_code.click_element(auth_code.SOC_YANDEX)
        assert auth_code.find_element(auth_code.YANDEX_ID)

