from django import forms

from .models import project

class projectForm(forms.ModelForm):
    class Meta:
        model = project
        fields = [
            'team_name',
            'project_title',
            'project_description',
            'source_code',
            'webpage',
            'image',
            'developing_or_developed',
            'key',
        ]