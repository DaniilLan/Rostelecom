
# Тест -  100
class TestSavingTabAuth:

    def test_tab_phone(self, auth):
        auth.click_element(auth.TAB_PHONE)
        color_tab_auth = auth.get_color_element(auth.ACTIV_TAB)
        auth.click_element(auth.LINK_FORGOT_PASSWORD)
        assert color_tab_auth == auth.get_color_element(auth.TAB_PHONE)

    def test_tab_email(self, auth):
        auth.click_element(auth.TAB_EMAIL)
        color_tab_auth = auth.get_color_element(auth.ACTIV_TAB)
        auth.click_element(auth.LINK_FORGOT_PASSWORD)
        assert color_tab_auth == auth.get_color_element(auth.TAB_EMAIL)

    def test_tab_login(self, auth):
        auth.click_element(auth.TAB_LOGIN)
        color_tab_auth = auth.get_color_element(auth.ACTIV_TAB)
        auth.click_element(auth.LINK_FORGOT_PASSWORD)
        assert color_tab_auth == auth.get_color_element(auth.TAB_LOGIN)

    def test_tab_ls(self, auth):
        auth.click_element(auth.TAB_LS)
        color_tab_auth = auth.get_color_element(auth.ACTIV_TAB)
        auth.click_element(auth.LINK_FORGOT_PASSWORD)
        assert color_tab_auth == auth.get_color_element(auth.TAB_LS)


# Тест - 105
class TestPlaceholder:

    def test_placeholder_phone(self, auth):
        auth.click_element(auth.TAB_PHONE)
        auth.click_element(auth.LINK_FORGOT_PASSWORD)
        text = auth.get_text_content(auth.PLACEHOLDER_USERNAME)
        assert text == "Мобильный телефон"

    def test_placeholder_email(self, auth):
        auth.click_element(auth.TAB_EMAIL)
        auth.click_element(auth.LINK_FORGOT_PASSWORD)
        text = auth.get_text_content(auth.PLACEHOLDER_USERNAME)
        assert text == "Электронная почта"

    def test_placeholder_login(self, auth):
        auth.click_element(auth.TAB_LOGIN)
        auth.click_element(auth.LINK_FORGOT_PASSWORD)
        text = auth.get_text_content(auth.PLACEHOLDER_USERNAME)
        assert text == "Логин"

    def test_placeholder_ls(self, auth):
        auth.click_element(auth.TAB_LS)
        auth.click_element(auth.LINK_FORGOT_PASSWORD)
        text = auth.get_text_content(auth.PLACEHOLDER_USERNAME)
        assert text == "Лицевой счёт"


# Тест - 110
def test_return_auth(auth):
    auth.click_element(auth.LINK_FORGOT_PASSWORD)
    auth.click_element(auth.BTN_RETURN_TO_AUTH)
    assert auth.find_element(auth.ID_AUTH_PASSWORD)
