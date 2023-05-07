from rest_framework import serializers

from fruit.models import FruitModel


class FruitSerializer(serializers.ModelSerializer):
    class Meta:
        model = FruitModel
        fields = ('name', 'id', 'color')


class FruitFullDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FruitModel
        fields = ('name', 'id', 'color', 'spoiled')
