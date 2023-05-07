from rest_framework.generics import ListCreateAPIView

import fruit
from fruit.api.v1.serializers import FruitSerializer
from fruit.models import FruitModel


class FruitListCreateView(ListCreateAPIView):
    serializer_class = FruitSerializer
    queryset = FruitModel.objects.exclude(spoiled=True)
