from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_add_item(self):
        item = Menu.objects.create(ID=3, Title='IceCream', Price=80.00, Inventory=100)
        self.assertEqual(item, "IceCream : 80")