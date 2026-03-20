from rest_framework import serializers

from api.models import FoodCategory
from api.serializers.FoodSerializer import FoodSerializer


class FoodListSerializer(serializers.ModelSerializer):
    foods = FoodSerializer(source='food', many=True, read_only=True)

    class Meta:
        model = FoodCategory
        fields = ('id', 'name_ru', 'name_en', 'name_ch', 'order_id', 'foods')
