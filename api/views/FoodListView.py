from django.db.models import Prefetch
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import Food, FoodCategory
from api.serializers import FoodListSerializer


class FoodListView(APIView):
    
    def get(self, request):
        published_foods = Food.objects.filter(is_publish=True)
        categories = FoodCategory.objects.filter(
            food__is_publish=True
        ).prefetch_related(
            Prefetch('food', queryset=published_foods)
        ).distinct()
        serializer = FoodListSerializer(categories, many=True)
        return Response(serializer.data)
