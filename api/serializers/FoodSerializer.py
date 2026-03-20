from rest_framework import serializers

from api.models import Food


class FoodSerializer(serializers.ModelSerializer):
    additional = serializers.SlugRelatedField(many=True, read_only=True, slug_field='internal_code')

    class Meta:
        model = Food
        fields = ('internal_code', 'code', 'name_ru', 'description_ru', 'description_en', 'description_ch', 'is_vegan', 'is_special', 'cost', 'additional')
