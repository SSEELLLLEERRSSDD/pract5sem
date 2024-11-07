# Работу выполнил Николаев Даниил Дмитриевич МО-221

# Инструкция по запуску:
* Вводим следующие команды в терминал:
* pip install pytest
* pip install playwright
* pip install pytest-html
* pytest tests/
* Открываем файлик "report.html"
* Радуемся, что все тесты прошли
# Тесты:
* "test_empty_login_and_password.py" - Авторизация с пустыми полями логина и пароля
* "test_empty_only_login.py" - Авторизация только с пустым логином
* "test_empty_only_password.py" - Авторизация только с пустым паролем
* "test_fali_order.py" - оформление заказа с пустыми полями "First Name", "Last Name", "Zip/Postal Code"
* "test_uncorrect_password.py" - Авторизация с неверным паролем 
