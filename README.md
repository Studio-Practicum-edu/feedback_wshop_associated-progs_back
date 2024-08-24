Workshop #2 associated programs backend 2024

##### Стек
- Python >3.10, Django 4.2, DRF 3.15

Структура файлов и директорий:

```
.
└── project_name/
    ├── api/ -> добавить приложение
    ├── fb_proj/
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── feedback/
    │   ├── migrations/
    │   │   └── __init__.py
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   └── models.py
    ├── .gitignore
    ├── manage.py
    ├── README.md
    └── requirements.txt
```

### Задание
1. Клонировать репозиторий
2. Установить зависимости из requirements.txt
3. Создать и применить миграции
4. Создать суперпользователя
5. Проверить работоспособность:
   1. Запустить сервер
   2. Зайти на страницу админки и залогиниться
   3. Добавить несколько сообщений
6. Добавить приложение api
7. Зарегистрировать приложение api
8. Создать сериализатор для модели Feedback (используем все доступные поля модели)
9. Создать представление CR (Create, Read) для модели Feedback
10. Настроить маршруты (URLs) для API
    1. POST /api/feedback/ -> создание сообщения
    2. GET /api/feedback/ -> просмотр всех сообщений
    3. GET /api/feedback/{id}/ -> просмотр сообщения по id
    4. DU запросы запрещены (реализовать корректные коды ответа сервера)
11. Проверить с помощью Postman создание и получение сообщений
12. Проверить с помощью Postman поведение при обновлении и удалении сообщений


### Рекомендации
1. Использовать вьюсеты (`from rest_framework import viewsets`)
2. Использовать `serializers.ModelSerializer`
3. Для маршрутов использовать роутер, например, `from rest_framework.routers import DefaultRouter`
4. Для запрета DU использовать `ListModelMixin, CreateModelMixin, RetrieveModelMixin` и `http_method_names`

### Дополнительное задание
- Настроить на уровне сериализатора валидацию поля `name` на отсутствие в нем цифр.
- Проверить, что имя формата `Сергей Иван0в` вызывает сообщение об ошибке.
