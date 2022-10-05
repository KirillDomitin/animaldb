from rest_framework import serializers

from animals.models import AnimalModel


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalModel
        fields = ('id', 'nickname', 'age', 'weight', 'height', 'identifying_mark', 'shelter')
