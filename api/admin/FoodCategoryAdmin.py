from django.contrib import admin
from api.models import FoodCategory


@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ('name_ru', 'order_id')
    search_fields = ('name_ru',)
