from django.contrib import admin
from api.models import Food


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('name_ru', 'category', 'is_publish', 'cost')
    list_filter = ('category', 'is_publish', 'is_vegan', 'is_special')
    search_fields = ('name_ru', 'description_ru', 'internal_code', 'code')
