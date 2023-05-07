from django.urls import path

from fruit.api.v1.views import FruitListCreateView, MakeFruitSpoilView

app_name = "fruit-v1-api"

urlpatterns = [
    path("list-create/", FruitListCreateView.as_view(), name="fruitListCreate"),
    path("make-spoiled/<int:id>/", MakeFruitSpoilView.as_view(), name="makeFruitSpoil"),
]
