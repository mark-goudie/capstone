from django.contrib import admin

# Register your models here.
from .models import User, Subject, Post, ContactSubmission

admin.site.register(User)
admin.site.register(Subject)
admin.site.register(Post)


@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'submitted_on']
    search_fields = ['name', 'email']