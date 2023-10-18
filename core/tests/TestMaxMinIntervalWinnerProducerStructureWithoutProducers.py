from rest_framework.test import APITestCase
from unittest.mock import MagicMock

from core.models import Producer


class TestMaxMinIntervalWinnerProducerStructureWithoutProducers(APITestCase):
    def setUp(self):
        self.original_filter = Producer.objects.all
        Producer.objects.all = MagicMock(return_value=list())

    def tearDown(self):
        Producer.objects.all = self.original_filter

    def test_maxminwinnerinterval_without_producers_structure(self):
        response = self.client.get("/api/maxminwinnerinterval/")

        self.assertEqual(response.status_code, 404)

        response_data = response.json()

        self.assertIsInstance(response_data, dict)
        self.assertIn("mensagem", response_data)
        self.assertIsInstance(response_data["mensagem"], str)
