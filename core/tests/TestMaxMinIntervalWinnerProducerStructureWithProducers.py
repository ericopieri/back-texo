from rest_framework.test import APITestCase
from unittest.mock import MagicMock

from core.models import Producer, Movie


class TestMaxMinIntervalWinnerProducerStructureWithProducers(APITestCase):
    def setUp(self):
        self.original_filter = Producer.objects.all

        producer1, producer2, producer3 = (
            MagicMock(spec=Producer, id=1, name="Producer 1"),
            MagicMock(spec=Producer, id=2, name="Producer 2"),
            MagicMock(spec=Producer, id=3, name="Producer 3"),
        )

        Producer.objects.all = MagicMock(return_value=[producer1, producer2, producer3])

        producer1.movies.all = MagicMock(
            return_value=[
                MagicMock(spec=Movie, id=1, title="Movie 1", year=2000, winner=True),
                MagicMock(spec=Movie, id=2, title="Movie 2", year=2001, winner=True),
                MagicMock(spec=Movie, id=3, title="Movie 3", year=2002, winner=True),
            ]
        )

        producer2.movies.all = MagicMock(
            return_value=[
                MagicMock(spec=Movie, id=4, title="Movie 4", year=1988, winner=True),
                MagicMock(spec=Movie, id=5, title="Movie 5", year=2005, winner=True),
                MagicMock(spec=Movie, id=6, title="Movie 6", year=2020, winner=True),
            ]
        )

        producer3.movies.all = MagicMock(
            return_value=[
                MagicMock(spec=Movie, id=7, title="Movie 7", year=1999, winner=True),
                MagicMock(spec=Movie, id=8, title="Movie 8", year=2003, winner=True),
                MagicMock(spec=Movie, id=9, title="Movie 9", year=2004, winner=True),
            ]
        )

        producer1.calc_win_interval = MagicMock(
            return_value={
                "followingWin": 2002,
                "previousWin": 2001,
                "interval": 1,
            }
        )

        producer2.calc_win_interval = MagicMock(
            return_value={
                "followingWin": 2005,
                "previousWin": 1988,
                "interval": 17,
            }
        )

        producer3.calc_win_interval = MagicMock(
            return_value={
                "followingWin": 2003,
                "previousWin": 1999,
                "interval": 4,
            }
        )

    def tearDown(self):
        Producer.objects.all = self.original_filter

    def test_maxminwinnerinterval_data_structure(self):
        response = self.client.get("/api/maxminwinnerinterval/")

        self.assertEqual(response.status_code, 200)

        response_data = response.json()

        self.assertIsInstance(response_data, dict)
        self.assertIn("max", response_data)
        self.assertIsInstance(response_data["max"], list)
        self.assertIn("min", response_data)
        self.assertIsInstance(response_data["min"], list)

        for item in response_data["min"]:
            self.assertIsInstance(item, dict)
            self.assertIn("producer", item)
            self.assertIsInstance(item["producer"], str)
            self.assertIn("interval", item)
            self.assertIsInstance(item["interval"], int)
            self.assertIn("previousWin", item)
            self.assertIsInstance(item["previousWin"], int)
            self.assertIn("followingWin", item)
            self.assertIsInstance(item["followingWin"], int)

        for item in response_data["max"]:
            self.assertIsInstance(item, dict)
            self.assertIn("producer", item)
            self.assertIsInstance(item["producer"], str)
            self.assertIn("interval", item)
            self.assertIsInstance(item["interval"], int)
            self.assertIn("previousWin", item)
            self.assertIsInstance(item["previousWin"], int)
            self.assertIn("followingWin", item)
            self.assertIsInstance(item["followingWin"], int)
