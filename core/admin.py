from django.contrib import admin

# Register your models here.
from .models import User, Subject, Post, ContactSubmission, Resource

admin.site.register(User)
admin.site.register(Subject)
admin.site.register(Post)
admin.site.register(Resource)


@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'submitted_on']
    search_fields = ['name', 'email']