from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=255)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"