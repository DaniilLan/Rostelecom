# Путь к драйверу
PATH_DRIVER = "Путь к веб-драйверу"

# URL тестируемого объеката
URL = 'https://b2c.passport.rt.ru'

# Валидные данные
valid_phone = 'Номер телефона'  # -----|
valid_email = 'Электронная почта'  # --|
valid_login = 'Логин'  # --------------|
valid_ls = 'Лицевой счёт'  # ----------| Данные должны принадлежать одному пользователю
valid_password = 'Пароль'  # ----------|
existing_first_name = 'Фамилия'  # ----|
existing_last_name = 'Имя'  # ---------|

# Невалидыне данные
invalid_password = '123'
empty_password = ''


# Генерация email
def generate_email():
    import random
    validchars = 'abcdefghijklmnopqrstuvwxyz1234567890'
    loginlen = random.randint(4, 15)
    login = ''
    for i in range(loginlen):
        pos = random.randint(0, len(validchars) - 1)
        login = login + validchars[pos]
    if login[0].isnumeric():
        pos = random.randint(0, len(validchars) - 10)
        login = validchars[pos] + login
    servers = ['@gmail', '@yahoo', '@redmail', '@hotmail', '@bing']
    servpos = random.randint(0, len(servers) - 1)
    email = login + servers[servpos]
    tlds = ['.com', '.in', '.gov', '.ac.in', '.net', '.org']
    tldpos = random.randint(0, len(tlds) - 1)
    email = email + tlds[tldpos]
    return email


# Генерация имя и фамилия
def generate_FL_name():
    from russian_names import RussianNames
    random_value = RussianNames(patronymic=False).get_person()
    first_name = (random_value.split(' ')[0])
    last_name = (random_value.split(' ')[1])
    return first_name, last_name
