## Run
- Убедитесь, что на вашей системе установлен Docker и Docker Compose.
- Откройте файл .env и настройте соответствующие переменные окружения для подключения к базе данных PostgreSQL по примеру файла .env.example.

- Соберите образ и запустите контейнеры:
```shell
  docker-compose up --build
```


## Добавить админа
- Запустите контейнеры.
- Создайте админа и введите его username, email и password:
```shell
  docker-compose exec django python src/manage.py createsuperuser
```
- Перейдите на http://127.0.0.1:8000/admin/

## Получить значение настройки
- Запустите контейнеры.
```shell
  docker-compose exec django python src/manage.py get_system_setting {key}
```
