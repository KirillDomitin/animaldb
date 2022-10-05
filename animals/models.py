from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
from django.contrib.auth.models import User


class ShelterModel(models.Model):
    """
    Модель приюта состоит только из названия, можно добавить любые поля
    """
    title = models.CharField(max_length=100, verbose_name=_('title'))

    class Meta:
        verbose_name = _('shelter')
        verbose_name_plural = _('shelters')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('shelters', kwargs={'id': self.pk})


class AnimalModel(models.Model):
    """
    Модель животного
    """
    nickname = models.CharField(max_length=50, verbose_name=_('nickname'))
    age = models.PositiveSmallIntegerField(verbose_name=_('age'))
    arrived_at = models.DateTimeField(auto_now_add=True, verbose_name=_('arrived at'))
    weight = models.DecimalField(max_digits=4, decimal_places=1, verbose_name=_('weight'))
    height = models.PositiveSmallIntegerField(verbose_name=_('height'))
    identifying_mark = models.TextField(max_length=500, blank=True, verbose_name=_('identifying mark'))
    shelter = models.ForeignKey(ShelterModel, on_delete=models.CASCADE, default=None)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'animal'
        verbose_name_plural = 'animals'

    def __str__(self):
        return self.nickname

    def get_absolute_url(self):
        return reverse('animals', kwargs={'id': self.pk})

    def save_delete(self):
        # Функция 'мягкого' удаления
        self.is_deleted = True
        self.save()

    def restore(self):
        # Функция востановление после 'мягкого' удаления
        self.is_deleted = False
        self.save()
