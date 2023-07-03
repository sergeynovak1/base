from django.db import models


class Method(models.TextChoices):
    POST = "POST"
    GET = "GET"