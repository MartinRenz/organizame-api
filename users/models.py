from django.contrib.auth.models import AbstractUser
from django.db import models

# Modelo do usuário.
class User(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        db_table = 'users'