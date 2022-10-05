from django.forms import ModelForm

from .models import AnimalModel


class AnimalCreateForm(ModelForm):
    """Форма для создания животного"""
    class Meta:
        model = AnimalModel
        fields = ('nickname', 'age', 'weight', 'height', 'identifying_mark')