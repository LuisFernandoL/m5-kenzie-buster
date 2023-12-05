from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    birthdate = models.DateField(null=True, default=None)
    is_employee = models.BooleanField(default=False)
    email = models.EmailField(max_length=127, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
