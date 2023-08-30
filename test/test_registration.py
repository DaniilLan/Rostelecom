import pytest
from config import *
from time import sleep


# Тест - 73
def test_register_valid(auth):
    first_name, last_name = generate_FL_name()
    auth.click_element(auth.LINK_REGISTER)
    auth.input_data(auth.INPUT_FIRST_NAME, first_name)
    auth.input_data(auth.INPUT_LAST_NAME, last_name)
    random_email = generate_email()
    auth.input_data(auth.INPUT_EMAIL_PHONE, random_email)
    auth.input_data(auth.INPUT_PASSWORD, valid_password)
    auth.input_data(auth.INPUT_PASS_CONFIM, valid_password)
    auth.click_element(auth.BTN_REGISTER)
    assert auth.find_element(auth.ID_INPUT_CODE_REG)


# Тест - 76, 77
class TestSelectionRegion:

    def test_select_click(self, auth):
        auth.click_element(auth.LINK_REGISTER)
        auth.click_element(auth.DROP_DAWN_REGION)
        auth.click_element_by_text('Самарская обл')
        assert 'Самарская обл' in auth.get_text_content(auth.VALUE_REGION)

    def test_select_input(self, auth):
        auth.click_element(auth.LINK_REGISTER)
        auth.input_data(auth.DROP_DAWN_REGION, 'Самарская')
        auth.click_element(auth.REGIONS)
        assert 'Самарская обл' in auth.get_text_content(auth.VALUE_REGION)


# Тест 78, 79, 80
class TestRegister:

    # Использовать почту существующего клиента Ростелком
    def test_existing_mail(self, auth):
        first_name, last_name = generate_FL_name()
        auth.click_element(auth.LINK_REGISTER)
        auth.input_data(auth.INPUT_FIRST_NAME, first_name)
        auth.input_data(auth.INPUT_LAST_NAME, last_name)
        auth.input_data(auth.INPUT_EMAIL_PHONE, valid_email)
        auth.input_data(auth.INPUT_PASSWORD, valid_password)
        auth.input_data(auth.INPUT_PASS_CONFIM, valid_password)
        auth.click_element(auth.BTN_REGISTER)
        assert auth.find_element(auth.BTN_LOGIN_IN_WINDOW)
        assert auth.find_element(auth.BTN_RECOVER_IN_WINDOW)

    # Использовать номер существующего клиента Ростелком
    def test_existing_phone(self, auth):
        first_name, last_name = generate_FL_name()
        auth.click_element(auth.LINK_REGISTER)
        auth.input_data(auth.INPUT_FIRST_NAME, first_name)
        auth.input_data(auth.INPUT_LAST_NAME, last_name)
        auth.input_data(auth.INPUT_EMAIL_PHONE, valid_phone)
        auth.input_data(auth.INPUT_PASSWORD, valid_password)
        auth.input_data(auth.INPUT_PASS_CONFIM, valid_password)
        auth.click_element(auth.BTN_REGISTER)
        assert auth.find_element(auth.BTN_LOGIN_IN_WINDOW)
        assert auth.find_element(auth.BTN_REGISTER_IN_WINDOW)

    # Использовать имя+фамилия+номер существующего клиента Ростелком
    def test_existing_phone_FL_name(self, auth):
        auth.click_element(auth.LINK_REGISTER)
        auth.input_data(auth.INPUT_FIRST_NAME, existing_first_name)
        auth.input_data(auth.INPUT_LAST_NAME, existing_last_name)
        auth.input_data(auth.INPUT_EMAIL_PHONE, valid_phone)
        auth.input_data(auth.INPUT_PASSWORD, valid_password)
        auth.input_data(auth.INPUT_PASS_CONFIM, valid_password)
        auth.click_element(auth.BTN_REGISTER)
        assert auth.find_element(auth.BTN_LOGIN_IN_WINDOW)
        assert auth.find_element(auth.BTN_RECOVER_IN_WINDOW)
        assert auth.find_element(auth.BTN_REGISTER_IN_WINDOW)




