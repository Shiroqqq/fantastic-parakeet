from django.db import models
from django.contrib.auth.models import User

class Car(models.Model):
    brand = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    model = models.CharField(max_length=100)
    number = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cars')

    def __str__(self):
        return f"{self.brand} {self.model} ({self.number})"
