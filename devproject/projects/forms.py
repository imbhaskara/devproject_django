from django.forms import ModelForm
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            'title',
            'project_image',
            'description',
            'demo_link',
            'source_link',
            'tags',
        ]