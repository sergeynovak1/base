from django.db import models


class SystemSettings(models.Model):
    key = models.CharField(max_length=255, unique=True)
    value = models.TextField()
    description = models.TextField()

    def __str__(self):
        return f'{self.key}: {self.value}'
