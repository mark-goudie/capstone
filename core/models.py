from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Subject(models.Model):
    subject = models.CharField(max_length=64)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.subject}"

class Post (models.Model):
    post = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    timestamp = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, blank=True, related_name="liked_posts")
    def __str__(self):
        return f"{self.user} posted {self.post} on {self.timestamp}"

class UserExtended(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class ContactSubmission(models.Model):
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    message = models.TextField(blank=True)
    submitted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} sent a message: {self.message}"
    