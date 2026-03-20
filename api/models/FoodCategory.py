from django.db import models
from model_utils.models import TimeStampedModel


class FoodCategory(TimeStampedModel):
    name_ru = models.CharField(verbose_name='Название на русском', max_length=255, unique=True)
    name_en = models.CharField(verbose_name='Название на английском', max_length=255,
                               unique=True, blank=True, null=True)
    name_ch = models.CharField(verbose_name='Название на китайском', max_length=255,
                               unique=True, blank=True, null=True)
    order_id = models.SmallIntegerField(default=10, blank=True, null=True)

    def __str__(self):
        return self.name_ru

    class Meta:
        verbose_name = 'Раздел меню'
        verbose_name_plural = 'Разделы меню'
        ordering = ('name_ru', 'order_id')
