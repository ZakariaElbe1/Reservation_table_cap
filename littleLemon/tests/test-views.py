from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from reservation.models import Menu
from reservation.serializers import MenuSerializer
import json


class MenuViewTest(APITestCase):
    def setUp(self):
        self.client.login(username='binzo', password='grizman@1212')
        self.menu_item1 = Menu.objects.create(title = "Pizza", price = 12.99, inventory = 5)
        self.menu_item2 = Menu.objects.create(title = "Burger", price = 8.99, inventory = 10)

    def test_getall(self):
        url = reverse('MenuItemsView')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        menu_items = Menu.objects.all()
        serializer = MenuSerializer(menu_items, many=True)
        self.assertEqual(json.dumps(response.data['results']), json.dumps(serializer.data))
