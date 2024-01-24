## Описание:
Web-приложение разработано в рамках тестового задания. Получает и выводит информацию по курсу доллара по отношению к рублю. Выводит последние 10 записей, полученных из API по адресу /get-current-usd/

## Как запустить:
- Откройте в CMD директорию в которую будете устанавливать проект
- Склонируйте репозиторий командой: ```https://github.com/midirenr/CurrencyCalculator.git```

- Перейдите в папку с проектом: ```cd CurrencyCalculator```

- Создайте виртуальное окружение командой:
1) Для ubuntu/linux: ```sudo python3 -m venv venv```
2) Для windows: ```python -m venv venv```

- Активируйте виртуальное окружение командой:
1) Для ubuntu/linux: ```source venv/bin/activate```
2) Для windows: ```.\venv\Scripts\activate```

- Установите все зависимости из файла requirements.txt: ```pip install -r requirements.txt```

- Сделайте миграции командой: ```python manage.py makemigrations```

- Примените миграции командой: ```python manage.py migrate```

- Запустите локальный сервер Django командой: ```python manage.py runserver```

- Перейдите по [ссылке](http://127.0.0.1:8000/get-current-usd/) или http://127.0.0.1:8000/get-current-usd/ для получения данных

## Используемые библиотеки и фреймворки:
- [APScheduler](https://pypi.org/project/APScheduler/)
- [Django Framework](https://www.djangoproject.com/)
- [requests](https://requests.readthedocs.io/en/latest/)