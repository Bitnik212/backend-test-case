from django.core.management.base import BaseCommand
from api.models.FoodCategory import FoodCategory
from api.models.Food import Food
from decimal import Decimal

class Command(BaseCommand):
    help = 'Seed the database with sample Food and FoodCategory data'

    def handle(self, *args, **kwargs):
        # Clear existing data to avoid conflicts
        self.stdout.write('Clearing existing data...')
        Food.objects.all().delete()
        FoodCategory.objects.all().delete()

        self.stdout.write('Seeding FoodCategory...')
        drinks = FoodCategory.objects.create(
            name_ru='Напитки',
            name_en='Drinks',
            order_id=10
        )
        bakery = FoodCategory.objects.create(
            name_ru='Выпечка',
            name_en='Bakery',
            order_id=20
        )
        empty_cat = FoodCategory.objects.create(
            name_ru='Пустая категория',
            name_en='Empty Category',
            order_id=30
        )
        hidden_cat = FoodCategory.objects.create(
            name_ru='Скрытая категория',
            name_en='Hidden Category',
            order_id=40
        )

        self.stdout.write('Seeding Food items for Напитки...')
        tea = Food.objects.create(
            category=drinks,
            internal_code=100,
            code=1,
            name_ru='Чай',
            description_ru='Чай 100 гр',
            is_vegan=True,
            cost=Decimal('123.00'),
            is_publish=True
        )
        cola = Food.objects.create(
            category=drinks,
            internal_code=200,
            code=2,
            name_ru='Кола',
            description_ru='Кола',
            cost=Decimal('123.00'),
            is_publish=True
        )
        sprite = Food.objects.create(
            category=drinks,
            internal_code=300,
            code=3,
            name_ru='Спрайт',
            description_ru='Спрайт',
            cost=Decimal('123.00'),
            is_publish=True
        )
        baikal = Food.objects.create(
            category=drinks,
            internal_code=400,
            code=4,
            name_ru='Байкал',
            description_ru='Байкал',
            cost=Decimal('123.00'),
            is_publish=True
        )
        # Add additional for tea
        tea.additional.add(cola)

        self.stdout.write('Seeding Food items for Выпечка...')
        croissant = Food.objects.create(
            category=bakery,
            internal_code=500,
            code=5,
            name_ru='Круассан',
            description_ru='Свежий круассан',
            cost=Decimal('150.00'),
            is_publish=True
        )
        donut = Food.objects.create(
            category=bakery,
            internal_code=600,
            code=6,
            name_ru='Пончик',
            description_ru='Сладкий пончик',
            cost=Decimal('80.00'),
            is_publish=True
        )

        self.stdout.write('Seeding Food items for Скрытая категория...')
        Food.objects.create(
            category=hidden_cat,
            internal_code=700,
            code=7,
            name_ru='Секретное блюдо',
            description_ru='Не должно отображаться',
            cost=Decimal('1000.00'),
            is_publish=False
        )

        self.stdout.write(self.style.SUCCESS('Successfully seeded data'))
