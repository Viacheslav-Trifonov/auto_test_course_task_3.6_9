# Запуск автотестов для разных языков интерфейса

Для работы скриптов потребуются установленные библиотеки Selenium и Pytest, и наличие актуального WebDriver для GoogleChrome.

Инструкция по установке:

- Скачайте с сайта https://sites.google.com/chromium.org/driver/ драйвер для вашей версии браузера. Разархивируйте скачанный файл.

- Создайте на диске C: папку chromedriver и положите разархивированный ранее файл chromedriver.exe в папку C:\chromedriver.

- Добавьте в системную переменную PATH папку C:\chromedriver. Как это сделать в разных версиях Windows, описано здесь: https://www.computerhope.com/issues/ch000549.htm.

Для установки зависимостей воспользуйтесь командой:

`pip install -r requirements.txt`
_________________________

В файле conftest.py находится обработчик, который считывает из командной строки параметр "language".
Также файл conftest.py ожержит логику запуска браузера с указанным языком пользователя и ссылку на тестируемую страницу. Браузер объявляется в фикстуре browser и передаётся в тест как параметр.
В файл test_items.py написан тест, который проверяет, что страница товара на сайте содержит кнопку добавления в корзину. 

Пример для запуска теста с параметром "language" в командной строке: 

`pytest --language=es test_items.py`

Данный тест работает только для браузера Chrome.
