from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import FoodCategory, Food

class FoodListViewTests(APITestCase):
    def setUp(self):
        self.cat1 = FoodCategory.objects.create(name_ru="Напитки", order_id=10)
        self.food1 = Food.objects.create(
            category=self.cat1,
            code=1,
            internal_code=100,
            name_ru="Чай",
            cost="123.00",
            is_publish=True
        )
        
        self.cat2 = FoodCategory.objects.create(name_ru="Выпечка", order_id=20)
        self.food2 = Food.objects.create(
            category=self.cat2,
            code=2,
            internal_code=200,
            name_ru="Булочка",
            cost="50.00",
            is_publish=False
        )
        
        self.cat3 = FoodCategory.objects.create(name_ru="Пустая", order_id=30)
        
        self.cat4 = FoodCategory.objects.create(name_ru="Смешанная", order_id=40)
        self.food3 = Food.objects.create(
            category=self.cat4,
            code=3,
            internal_code=300,
            name_ru="Опубликовано",
            cost="10.00",
            is_publish=True
        )
        self.food4 = Food.objects.create(
            category=self.cat4,
            code=4,
            internal_code=400,
            name_ru="Скрыто",
            cost="10.00",
            is_publish=False
        )

    def test_get_food_list(self):
        url = reverse('food-list')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        self.assertEqual(len(response.data), 2)
        
        cat1_data = next(item for item in response.data if item['id'] == self.cat1.id)
        self.assertEqual(len(cat1_data['foods']), 1)
        self.assertEqual(cat1_data['foods'][0]['internal_code'], 100)
        
        cat4_data = next(item for item in response.data if item['id'] == self.cat4.id)
        self.assertEqual(len(cat4_data['foods']), 1)
        self.assertEqual(cat4_data['foods'][0]['internal_code'], 300)
        
        cat_ids = [item['id'] for item in response.data]
        self.assertNotIn(self.cat2.id, cat_ids)
        self.assertNotIn(self.cat3.id, cat_ids)
