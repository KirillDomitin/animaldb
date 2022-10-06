from rest_framework import generics
from rest_framework.response import Response

from animals.models import AnimalModel
from .serializers import AnimalSerializer


class AnimalAPIList(generics.ListCreateAPIView):
    """Получение списка всех животных"""
    queryset = AnimalModel.objects.all()
    serializer_class = AnimalSerializer

    def get(self, request, *args, **kwargs):
        """Получение списка всех животных"""
        return super(AnimalAPIList, self).get(request)

    def post(self, request, *args, **kwargs):
        """Добавление животного в базу данных"""
        return super(AnimalAPIList, self).post(request)


class AnimalRetriveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Чтение, Редактирование и Удаление конкретного животного"""
    queryset = AnimalModel.objects.filter(is_deleted=False).all()
    serializer_class = AnimalSerializer

    def delete(self, request, *args, **kwargs):
        """Удаление животного"""
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method DELETE not allowed'})

        try:
            instance = AnimalModel.objects.get(pk=pk, is_deleted=False)
        except:
            return Response({'error': 'Object does not exist'})

        instance.is_deleted = True
        instance.save()
        return Response({'animal': 'delete animal with id ' + str(pk)})

    def get(self, request, *args, **kwargs):
        """Получить детальную информацию по животному"""
        return super(AnimalRetriveUpdateDestroyAPIView, self).get(request)

    def put(self, request, *args, **kwargs):
        """Внести изменение в запись о животном"""
        return super(AnimalRetriveUpdateDestroyAPIView, self).put(request)

    def patch(self, request, *args, **kwargs):
        """Внести изменение в запись о животном"""
        return super(AnimalRetriveUpdateDestroyAPIView, self).put(request)