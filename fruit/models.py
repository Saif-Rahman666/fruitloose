from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.

class FruitModel(models.Model):
    name = models.CharField(max_length=200, verbose_name=_("Name"))
    color = models.CharField(max_length=50, verbose_name=_("Color"))
    spoiled = models.BooleanField(default=False, verbose_name=_("Spoiled"))

    def __str__(self):
        return f"{self.name}-{self.color}"

    class Meta:
        ordering = ('-id',)
        verbose_name = _("Fruit")
        verbose_name_plural = _("Fruits")
