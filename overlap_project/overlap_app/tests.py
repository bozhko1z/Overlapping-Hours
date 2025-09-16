from django.contrib.auth.models import User
from django.test import TestCase
from .models import WorkingHours, Shop
from datetime import time

class TestWorkingHour(TestCase):
    def setUp(self):
        self.owner = User.objects.create(username="Yordanov", password="12233")
        self.shop = Shop.objects.create(name="Yordanov Bar & Grill", owner=self.owner)
        self.working_hour = WorkingHours.objects.create(
            shop=self.shop,
            day="Monday",
            start=time(9, 0),
            end=time(12, 0),
        )

    def test_str(self):
        self.assertEqual(str(self.working_hour), "Monday")

class TestShop(TestCase):
    def setUp(self):
        self.owner = User.objects.create(username="Yordanov", password="12233")
        self.shop = Shop.objects.create(name = "Yordanov Bar & Grill", owner = self.owner)

    def test_str(self):
        self.assertEqual(str(self.shop), "Yordanov Bar & Grill")
