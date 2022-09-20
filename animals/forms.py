from django.forms import forms, ModelForm
from .models import AnimalModel


class AnimalCreateForm(ModelForm):
    class Meta:
        model = AnimalModel
        fields = '__all__'