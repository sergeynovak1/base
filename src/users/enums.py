from django.db import models


class Role(models.TextChoices):
    admin = "admin", "Администратор"
    staff = "staff", "Сотрудник"
    user = "user", "Пользователь"


class Method(models.TextChoices):
    POST = "POST"
    GET = "GET"
