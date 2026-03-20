from django.urls import path
from api.views import FoodListView

urlpatterns = [
    path('foods/', FoodListView.as_view(), name='food-list'),
]
