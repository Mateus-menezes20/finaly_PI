
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username


class ReportConfig(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    header = models.CharField(max_length=255)

    def __str__(self):
        return f"Config de {self.user.username}"
