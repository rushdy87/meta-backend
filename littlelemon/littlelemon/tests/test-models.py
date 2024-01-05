from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


# class MenuTest(TestCase):
#     def test_instance(self):
#         menu = Menu.objects.create(
#             title='Macaroni',
#             price=11.00
#         )
#         self.assertEqual(str(menu), "Macaroni : 11.0")


class MenuViewTest(TestCase):
    def setUp(self):
        self.menu_item1 = Menu.objects.create(
            title="Macaroni", price=11.0)
        self.menu_item2 = Menu.objects.create(
            title="Burger", price=5.9)

    def test_get_all_menu_items(self):

        url = reverse('menu-items-view')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        menu_items = Menu.objects.all()
        serializer = MenuSerializer(menu_items, many=True)

        self.assertEqual(response.data, serializer.data)
