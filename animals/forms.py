from django.forms import forms, ModelForm
from .models import AnimalModel


class AnimalCreateForm(ModelForm):
    class Meta:
        model = AnimalModel
        fields = ('nickname', 'age', 'weight', 'height', 'identifying_mark', 'shelter')
        # fields = ('nickname', 'age', 'weight', 'height', 'identifying_mark', 'shelter')