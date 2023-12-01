from django import forms
from .models import Resource

class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['title', 'description', 'file_link', 'subject', 'grade_level', 'resource_type']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
