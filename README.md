## Описание:
Web-приложение разработано в рамках тестового задания. Получает и выводит информацию по курсу доллара по отношению к рублю. Выводит последние 10 записей, полученных из API по адресу /get-current-usd/ .
ВАЖНО: учтите, что первый запрос на API для получения курса доллара выполнится через 10 секунда после запуска web-сервера и далее будет храниться в базе данных. Поэтому при первом переходе по адресу приложение моежт вернуть пустой JSON.

## Как запустить:
- Откройте в CMD директорию в которую будете устанавливать проект
- Склонируйте репозиторий командой: ```git clone https://github.com/midirenr/CurrencyCalculator.git```

- Перейдите в папку с проектом: ```cd CurrencyCalculator```

- Создайте виртуальное окружение командой:
1) Для ubuntu/linux: ```python3 -m venv venv```
2) Для windows: ```python -m venv venv```

- Активируйте виртуальное окружение командой:
1) Для ubuntu/linux: ```source venv/bin/activate```
2) Для windows: ```.\venv\Scripts\activate```

- Установите все зависимости из файла requirements.txt: ```pip install -r requirements.txt```

- Сделайте миграции командой: ```python CurrencyCalculator/manage.py makemigrations```

- Примените миграции командой: ```python CurrencyCalculator/manage.py migrate```

- Запустите локальный сервер Django командой: ```python CurrencyCalculator/manage.py runserver```

- Перейдите по [ссылке](http://127.0.0.1:8000/get-current-usd/) или http://127.0.0.1:8000/get-current-usd/ для получения данных. Учтите, что первый запрос на API для получения курса доллара выполнится через 10 секунда после запуска web-сервера и далее будет храниться в базе данных. Поэтому при первом переходе по адресу приложение моежт вернуть пустой JSON. Далее результаты запросов будут хранится в базе данных и при перезапуске сервера информация не будет утеряна.

## Используемые библиотеки и фреймворки:
- [APScheduler](https://pypi.org/project/APScheduler/)
- [Django Framework](https://www.djangoproject.com/)
- [requests](https://requests.readthedocs.io/en/latest/)
