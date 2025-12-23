from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14, unique=True)
    birth_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
