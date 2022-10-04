from rest_framework import generics
from rest_framework.response import Response

from animals.models import AnimalModel
from .serializers import AnimalSerializer


class AnimalAPIList(generics.ListCreateAPIView):
    queryset = AnimalModel.objects.all()
    serializer_class = AnimalSerializer


class AnimalRetriveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AnimalModel.objects.filter(is_deleted=False).all()
    serializer_class = AnimalSerializer

    def delete(self, request, *args, **kwargs):
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
