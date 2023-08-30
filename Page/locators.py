from selenium.webdriver.common.by import By
from Rostelecom.Page.base_page import BasePage


class Locators(BasePage):

    # Кнопка в табе 'Телефон'
    TAB_PHONE = (By.ID, "t-btn-tab-phone")

    # Кнопка в табе 'Почта'
    TAB_EMAIL = (By.ID, "t-btn-tab-mail")

    # Кнопка в табе 'Логин'
    TAB_LOGIN = (By.ID, "t-btn-tab-login")

    # Кнопка в табе 'ЛС'
    TAB_LS = (By.ID, "t-btn-tab-ls")

    # Поле ввода при входе через код
    INPUT_EMAIL_PHONE = (By.ID, 'address')

    # Кнопка "Получить код"
    BTN_GET_CODE = (By.XPATH, '//*[@id="otp_get_code"]')

    # Кнопка "Войти с паролем"
    BTN_LOG_WITH_PASSWORD = (By.ID, "standard_auth_btn")

    # Поле ввода для Почты/Телефона/Логина/Лицевого счёта
    INPUT_USERNAME = (By.ID, 'username')

    # Поле ввода для пароля
    INPUT_PASSWORD = (By.ID, 'password')

    # Кнопка 'Войти'
    BTN_LOGIN = (By.ID, 'kc-login')

    # Кнопка 'Вернуться назад' на стр. восстановления
    BTN_RETURN_TO_AUTH = (By.ID, 'reset-back')

    # Кнопка 'Забыли пароль?'
    LINK_FORGOT_PASSWORD = (By.ID, 'forgot_password')

    # Кнопка 'Зарегистрироваться'
    LINK_REGISTER = (By.XPATH, "//a[@id='kc-register']")

    # Кнопка 'Вконтакте'
    SOC_VK = (By.ID, "oidc_vk")

    # Кнопка 'Одноклассники'
    SOC_OK = (By.ID, "oidc_ok")

    # Кнопка 'Mail.Ru'
    SOC_MAIL = (By.ID, "oidc_mail")

    # Кнопка 'Яндекс'
    SOC_YANDEX = (By.ID, "oidc_ya")

    # Ссылка "пользовательского соглашения" под кнопкой "Войти"
    LINK_USER_AGR = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/a')

    # Поле "Имя"
    INPUT_FIRST_NAME = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/div/input')

    # Поле "Фамилия"
    INPUT_LAST_NAME = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/input')

    # Выпадающий список поля "Регион"
    DROP_DAWN_REGION = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[2]/div/div/input')

    # Поле "Подтверждение пароля"
    INPUT_PASS_CONFIM = (By.ID, 'password-confirm')

    # Кнопка "Зарегистрироваться"
    BTN_REGISTER = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/button')

    # Ссылка "пользовательского соглашения" под кнопкой "Зарегистрироваться"
    LINK_USER_AGR_REG = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[5]/a')

    # Кнопка "Выйти" на странице паспорта авторизованного клиента
    BTN_EXIT = (By.ID, 'logout-btn')

    # Блок сообщения с ошибкой "Неверный логин или пароль"
    ERROR_PASS = (By.XPATH, '//*[@id="form-error-message"]')

    # Идентификатор страницы авторизации через пароль
    ID_AUTH_PASSWORD = (By.XPATH, '//*[@id="page-right"]/div/div/h1[contains(text(),"Авторизация")]')

    # Идентификатор страницы авторизации по коду
    ID_AUTH_CODE = (By.XPATH, '//*[@id="page-right"]/div/div/h1[contains(text(),"Авторизация по коду")]')

    # Идентификатор страницы авторизации через ВК
    VK_ID = (By.XPATH, '//*[@id="root"]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/h1[1]/div[1]')

    # Идентификатор страницы авторизации через Маил.ру
    MAIL_ID = (By.XPATH, '//*[@id="wrp"]/div[1]/span')

    # Идентификатор страницы авторизации через Яндекс
    YANDEX_ID = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/a')

    # Идентификатор страницы авторизации через Одноклассники
    OK_ID = (By.XPATH, '//*[@id="widget-el"]/div[1]/div')

    # Текст в поле "Телефон/Почта/Логин/Лицевой счёт"
    PLACEHOLDER_USERNAME = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]')

    # Идентификатор страницы восстановления пароля
    ID_PASSWORD_RECOVERY = (By.XPATH, '//*[@id="page-right"]/div/div/h1')

    # Идентификатор страницы регистрации
    ID_REGISTER = (By.XPATH, '//*[@id="page-right"]/div/div/h1')

    # Идентификатор страницы ввода кода подтверждения (при регистрации)
    ID_INPUT_CODE_REG = (By.XPATH, '//*[@id="page-right"]/div/div/h1')

    # Идентификатор страницы пользовательского соглашения
    ID_USER_AGR = (By.XPATH, '//*[@id="title"]/h1[contains(text(),"Подтверждение email")]')

    # Идентификатор страницы ввода кода подтверждения (для входа по коду)
    ID_INPUT_CODE_AUTH = (By.XPATH, '//*[@id="page-right"]/div/div/div/p[contains(text(),"Код подтверждения отправлен")]')

    # Ссылка для перехода на страницу изменения телефона или почты (для входа по коду)
    CHANGE_PH_and_EM = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/button')

    # Значение поля 'E-mail или мобильный телефон' при авторизации по коду
    VALUE_PHONE_EMAIL = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div/div')

    # Сообщение об ограничении в отправке кода подтверждения при входе по коду
    MESSAGE_LIMITATIONS = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[2]')

    # Активный тип аутентификации (имеет оранжевый цвет)
    ACTIV_TAB = (By.CSS_SELECTOR, ".rt-tabs .rt-tab--small.rt-tab--active")

    # Локатор окна с регионами в дропдаун
    WINDOW_REGIONS = (By.CLASS_NAME, 'rt-scroll-container.rt-scrollbar.rt-scrollbar-mask')

    # Список регионов
    REGIONS = (By.CLASS_NAME, "rt-select__list-item")

    # Кнопка "Войти" в окне уведомления при регистрации
    BTN_LOGIN_IN_WINDOW = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div/div/div[2]/button')

    # Кнопка "Восстановить пароль" в окне уведомления при регистрации
    BTN_RECOVER_IN_WINDOW = (By.ID, 'reg-err-reset-pass')

    # Кнопка "Зарегистрироваться" в окне уведомления при регистрации
    BTN_REGISTER_IN_WINDOW = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div/div/div[2]/button[2]')

    # Локатор для получения значения поля "Регион"
    VALUE_REGION = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[2]/div/div')





