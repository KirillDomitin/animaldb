from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from animals.models import ShelterModel


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shelter = models.ForeignKey(ShelterModel, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('profile_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
