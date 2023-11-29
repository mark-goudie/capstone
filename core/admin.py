from django.contrib import admin

# Register your models here.
from .models import User, Subject, Post

admin.site.register(User)
admin.site.register(Subject)
admin.site.register(Post)

