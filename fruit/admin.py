from django.contrib import admin

from fruit.models import FruitModel


# Register your models here.
@admin.register(FruitModel)
class FruitAdmin(admin.ModelAdmin):
    pass
