from django.test import TestCase
from reservation.models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="tagine", price=10.00, inventory=5)
        self.assertEqual(str(item), 'tagine : 10.0')

