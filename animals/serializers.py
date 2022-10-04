from rest_framework import serializers

from animals.models import AnimalModel


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalModel
        fields = ('id', 'nickname', 'age', 'weight', 'height', 'identifying_mark', 'shelter')

    # nickname = serializers.CharField(max_length=50)
    # age = serializers.IntegerField(min_value=0)
    # arrived_at = serializers.DateTimeField(read_only=True)
    # weight = serializers.DecimalField(max_digits=4, decimal_places=1)
    # height = serializers.IntegerField(min_value=0)
    # identifying_mark = serializers.CharField()
    # shelter_id = serializers.IntegerField()
    # is_deleted = serializers.BooleanField(default=False)
    #
    # def create(self, validated_data):
    #     return AnimalModel.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.nickname = validated_data.get('nickname', instance.nickname)
    #     instance.age = validated_data.get('age', instance.age)
    #     instance.weight = validated_data.get('weight', instance.weight)
    #     instance.height = validated_data.get('height', instance.height)
    #     instance.identifying_mark = validated_data.get('identifying_mark', instance.identifying_mark)
    #     instance.shelter = validated_data.get('shelter', instance.shelter)
    #     instance.save()
    #     return instance
    #
    #

# class AnimalModel(models.Model):
#     """
#     Animal model
#     """
#     nickname = models.CharField(max_length=50, verbose_name=_('nickname'))
#     age = models.PositiveSmallIntegerField(verbose_name=_('age'))
#     arrived_at = models.DateTimeField(auto_now_add=True, verbose_name=_('arrived at'))
#     weight = models.DecimalField(max_digits=4, decimal_places=1, verbose_name=_('weight'))
#     height = models.PositiveSmallIntegerField(verbose_name=_('height'))
#     identifying_mark = models.TextField(max_length=500, blank=True, verbose_name=_('identifying_mark'))
#     shelter = models.ForeignKey(ShelterModel, on_delete=models.CASCADE, default=None)
#     is_deleted = models.BooleanField(default=False)
