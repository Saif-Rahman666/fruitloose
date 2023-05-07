from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, UpdateAPIView
from rest_framework.response import Response

import fruit
from fruit.api.v1.serializers import FruitSerializer, FruitFullDetailsSerializer
from fruit.models import FruitModel


class FruitListCreateView(ListCreateAPIView):
    serializer_class = FruitSerializer
    queryset = FruitModel.objects.exclude(spoiled=True)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'color']


class MakeFruitSpoilView(UpdateAPIView):
    queryset = FruitModel.objects.all()
    serializer_class = FruitFullDetailsSerializer
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()

        # Check if the fruit is already spoiled
        if instance.spoiled:
            return Response({'detail': 'Fruit is already spoiled.'}, status=status.HTTP_400_BAD_REQUEST)

        instance.spoiled = True
        instance.save()

        serializer = self.get_serializer(instance)
        return Response(serializer.data)
