>## ИТОГОВЫЙ ПРОЕКТ ПО АВТОМАТИЗАЦИИ ТЕСТИРОВАНИЯ

### Необходимо протестировать новый интерфейс авторизации в личном кабинете от заказчика Ростелеком.


→ Объект тестирования: https://b2c.passport.rt.ru
→ [Требования по проекту](https://docs.google.com/document/d/16EDl8nK3VFl4S_qI33oK14_C5EkT_X6b/edit?usp=drive_link&ouid=112298827689842558654&rtpof=true&sd=true)


#### Задача:
  1. Протестировать требования.
  2. Разработать тест-кейсы (не менее 15). Необходимо применить несколько техник тест-дизайна.
  3. Провести автоматизированное тестирование продукта (не менее 20 автотестов). Заказчик ожидает по одному автотесту на каждый написанный тест-кейс. Оформите свой набор автотестов в GitHub.
  4. Оформить описание обнаруженных дефектов. Во время обучения вы работали с разными сервисами и шаблонами, используйте их для оформления тест-кейсов и обнаруженных дефектов. (если дефекты не будут обнаружены, то составить описание трех дефектов)



#### Ожидаемый результат:
  1. Перечислены инструменты, которые применялись для тестирования.
  
     * Почему именно этот инструмент и эту технику.
     * Что им проверялось.
     * Что именно в нем сделано.
     
  2. К выполненному заданию прикреплены:
  
     * Набор тест-кейсов;
     * Набор автотестов на GitHub. Обратите внимание, что в репозитории должен находиться файл README.md, где будет описано, что именно проверяют данные тестовые сценарии и какие команды необходимо выполнить для запуска   
       тестов. Описанные команды должны работать на любом компьютере с установленными Python3 и PyTest;
     * Описание оформленных дефектов.

***
#### В корневом каталоге проекта содержаться:
* [Driver](https://github.com/DaniilLan/Rostelecom/tree/main/Driver) - веб-драйвер и его лицензия;
* [Page](https://github.com/DaniilLan/Rostelecom/tree/main/Page) - локаторы и основные функцыи для тестов;
* [tests](https://github.com/DaniilLan/Rostelecom/tree/main/test) - тесты на каждую страницу.
***
#### Директория Driver содержит:
* [LICENSE.chromedriver](https://github.com/DaniilLan/Rostelecom/blob/main/Driver/LICENSE.chromedriver) - лицензия;
* [chromedriver.exe](https://github.com/DaniilLan/Rostelecom/blob/main/Driver/chromedriver.exe) - драйвер для управления браузером Chrome.
***
#### Директория Page содержит:
* [base_page.py](https://github.com/DaniilLan/Rostelecom/blob/main/Page/base_page.py) - базовый класс, который содержит объект страницы и функции для выполнения тестов;
* [config.py](https://github.com/DaniilLan/Rostelecom/blob/main/Page/config.py) - данные для работы тестов;
* [locators.py](https://github.com/DaniilLan/Rostelecom/blob/main/Page/locators.py) - описание локаторов страниц.
***
#### Директория tests содержит:
* [conftest.py](https://github.com/DaniilLan/Rostelecom/blob/main/test/conftest.py) -  условия для выполнения тестов;
* [test_authorization_code.py](https://github.com/DaniilLan/Rostelecom/blob/main/test/test_authorization_code.py) - тесты для страницы авторизации по временному коду;
* [test_authorization_pass.py](https://github.com/DaniilLan/Rostelecom/blob/main/test/test_authorization_pass.py) - тесты для страницы авторизации по паролю;
* [test_recovery.py](https://github.com/DaniilLan/Rostelecom/blob/main/test/test_recovery.py) - тесты для страницы восстановления пароля;
* [test_registration.py](https://github.com/DaniilLan/Rostelecom/blob/main/test/test_registration.py) - тесты для страницы регистрации.
***


### → [Тест-кейсы, баг-репорты](https://docs.google.com/spreadsheets/d/1h-1wUtpINn6I14Mhtua02kMSiNghaw_u39PlyeyAXOk/edit#gid=0)

### При разработке тест-кейсов были применены следующие техники тест-дизайна: 
 
* Анализ граничных значений
* Классы эквивалентности
* Диаграмма перехода состояния

### Инструменты, которые применялись для тестирования.

* Для тестирования сайта был использован 
инсрумент [Selenium](https://www.selenium.dev/);
* Для создания и проектирования тестов была использована IDE PyCharm;
* Для определения локаторов использовался DevTools.

### Запуск тестов:
* Установить все библиотеки и зависимости из requirements.txt;
* В файле [config.py](https://github.com/DaniilLan/Rostelecom/blob/main/Page/config.py) заполнить все переменные соответствующими данными
* Загрузите [Selenium WebDriver](https://chromedriver.chromium.org/downloads) (выберите версию, совместимую с вашим браузером) и прописать путь к драйверу в переменную PATH_DRIVER в файле config.py;
* Запустить тест: `python -m pytest -v --driver Chrome --driver-path <путь файла>`.
* При ошибке импортирования файлов из папки [Page](https://github.com/DaniilLan/Rostelecom/tree/main/Page) пометить её как Sources Root



