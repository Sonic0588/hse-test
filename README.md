### Создание базы данных и юзера:

* `sudo -u postgres psql -c "create user hseuser with login password 'hsepass' superuser;"`
* `sudo -u postgres psql -c "create database hsetest owner hseuser encoding = 'UTF8';"`

### Запуск

* `python3 app.py`

### Работа с API

* Отправка POST запроса с файлом csv или xls на путь http://host/upload

### Основные модули, библиотека и логику их работы

* Flask - фреймворк для создания сервера и организации роутинга
* pandas - библиотека для работы с данными
* SQLAlchemy - библиотке для подключения к базе данных работы с сервером postgres
* csv - библиотека для парсинга csv
* xlrd - библиотека для парсинга xls
