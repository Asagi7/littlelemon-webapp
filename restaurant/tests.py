# Unit tests for the menu and table booking APIs.
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase

from .models import Booking, Menu


class MenuApiTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        Menu.objects.create(title='Greek Salad', price=12.99, inventory=10)

    def test_get_menu_items(self):
        response = self.client.get('/api/menu-items/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_create_menu_item(self):
        response = self.client.post('/api/menu-items/', {
            'title': 'Bruschetta',
            'price': 7.99,
            'inventory': 8,
        }, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Menu.objects.count(), 2)

    def test_menu_item_detail_update_delete(self):
        item = Menu.objects.get(title='Greek Salad')
        response = self.client.patch(f'/api/menu-items/{item.id}/',
                                     {'price': 10.99}, format='json')
        self.assertEqual(response.status_code, 200)
        item.refresh_from_db()
        self.assertEqual(float(item.price), 10.99)
        response = self.client.delete(f'/api/menu-items/{item.id}/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Menu.objects.count(), 0)


class BookingApiTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_get_bookings(self):
        Booking.objects.create(name='John Doe', no_of_guests=2,
                               booking_date='2026-12-13T18:00:00Z')
        response = self.client.get('/api/bookings/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_create_booking(self):
        response = self.client.post('/api/bookings/', {
            'name': 'Jane Doe',
            'no_of_guests': 4,
            'booking_date': '2026-12-14T19:00:00Z',
        }, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Booking.objects.count(), 1)

    def test_booking_requires_authentication(self):
        anonymous = APIClient()
        response = anonymous.get('/api/bookings/')
        self.assertEqual(response.status_code, 401)
