from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import patch
from orders.infrastructure.repositories import JsonOrderRepository
from orders.application.services import OrderService


class JsonOrderRepositoryTests(TestCase):
    def setUp(self):
        self.repository = JsonOrderRepository()
    
    def test_get_order_status(self):
        order = self.repository.get_order_status()
        self.assertIsNotNone(order)
        self.assertEqual(len(order.rounds), 3)

class OrderServiceTests(TestCase):
    def setUp(self):
        self.order_service = OrderService(order_repository=JsonOrderRepository())
    
    def test_get_order_status(self):
        order = self.order_service.get_order_status()
        self.assertEqual(order.created, "2024-09-10 12:00:00")
        self.assertTrue(len(order.rounds) > 0)

class OrderStatusViewTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_order_status(self):
        url = reverse('orders:order-status')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        response_data = response.json()
        data = response_data.get('data', {})

        # Verificar que los campos esperados estén presentes
        self.assertIn("created", data)
        self.assertIn("rounds", data)


    def test_stock_status(self):
        url = reverse('orders:stock-status')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn("last_updated", response.json())
        self.assertIn("beers", response.json())

class OrderStatusViewErrorTests(TestCase):
    def setUp(self):
        self.client = Client()
    
    @patch('orders.application.services.OrderService.get_order_status')
    def test_order_status_service_error(self, mock_get_order_status):
        mock_get_order_status.side_effect = Exception("Service error")
        url = reverse('orders:order-status')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 500)