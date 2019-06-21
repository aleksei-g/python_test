# PERX Python test

Проект реализует aiohttp сервер, который считает арифметическую прогрессию в очереди.

У сервера 2 ендпоинта:
1. `/` - выводит информацию по выполняющимся в настоящее время заданиям, а так же по заданиям в очереди.
2. `/tasks/new` - позволяет поставить новую задачу в очередь на выполнение.

Сервер запускается одним процессом. В качестве хранения данных используется память.
Количество одновременно выполняющихся задач регулируется переменной окружения `CONFIG_FILEPATH`.
Значение по умолчанию равно 1. 

## Локальная установка
1. Создать директорию проекта и перейти в нее. Клонировать репозиторий в этот каталог:

    ```
    $ mkdir project_folder
    $ cd project_folder
    $ git clone https://github.com/aleksei-g/python_test.git .
    ```

2. Создать виртуальное окружение с Python 3.6 и установить необходимые зависимости:

    ```
    $ python3.6 -m venv virtualenv_path
    $ source virtualenv_path/bin/activate
    (virtualenv_path) $ pip install -r requirements.txt
    ```
    
## Запуск сервера
Убедиться, что текущая директория это каталог проекта, а так же что активировано виртуальное окружение.

Запустить сервер командой:
```
(virtualenv_path) $ python3 run.py
```
Web приложение будет доступно по адресу [http://127.0.0.1:8080/](http://127.0.0.1:8080/).