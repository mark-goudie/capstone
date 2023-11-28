from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Subject(models.Model):
    subject = models.CharField(max_length=64)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.subject}"

