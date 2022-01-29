from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    first_name = models.CharField(
        max_length=255,
        blank=True, null=True,
        verbose_name='Имя'
    )
    last_name = models.CharField(
        max_length=255,
        blank=True, null=True,
        verbose_name='Фамилия'
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.username}'
