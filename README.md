# Ray App

Приложение обладает грандиозной функциональностью:

- Микросервис по загрузке файлов
- Микросервис прогноза погоды в любом городе (веб-интерфейс либо чат-бот на выбор)
- Сайт "Дневник чувств"

## Переменные окружения

Создайте файл .env и заполните его следующими данными:

- DEBUG
- SECRET_KEY
- ALLOWED_HOSTS
- YANDEX_WEATHER_API_KEY [Yandex Weather API service](https://yandex.ru/dev/weather/doc/dg/concepts/about.html)
- DATABASE_URL (строка подключения к БД PosgreSQL формата: postgres://postgres:пароль@адрес/бд)
- FILES_DIR

Для работы с telegram-ботом:
- Создайте нового бота в Telegram и получите токен   
  (вы можете получить бота от @BotFather в Telegram, [см. пример](https://telegra.ph/Awesome-Telegram-Bot-11-11))
- TELEGRAM_API_TOKEN
  
## Как запустить dev-версию сервиса

- Скачайте код:

```bash
git clone https://github.com/Rostwik/ray_app.git
```

- Установите зависимости:

```bash
pip install -r requirements.txt
```
- Создайте файл базы данных:
```bash
python manage.py migrate
```

- Запустите сервер:
```bash
python manage.py runserver
```
- Запустите Redis в новом окне терминала (должен быть установлен [Docker](https://docs.docker.com/engine/install/)):
```bash
docker run -p 6379:6379 --name some-redis -d redis
```

- Запустите Celery в новом окне терминала:
```bash
celery -A picasso worker --loglevel=info
```

- Для корректной работы прогноза погоды, в бд необходимо загрузить координаты городов,
обратите внимание на наличие файла "towns_coordinates.txt" :

```bash
python manage.py load_towns
```

Сервис готов к работе.

Опционально:

- Для запуска телеграм-бота:
```bash
python manage.py weather_bot
```
- Удалить все города из бд:
```bash
python manage.py delete_all_towns
```

## Тесты

Запуск тестов из каталога diary_project:

```bash
python manage.py test file_app
```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


