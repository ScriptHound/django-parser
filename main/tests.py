from django.db.models.query import QuerySet
from django.test import TestCase
from .models import ResultRow, ResultIdModel
from .queries import get_all_pids, save_pid, save_parsing_results, get_results_by_id


# Create your tests here.
class QueryTest(TestCase):
    def setUp(self):
        self.pid = save_pid("pppp")
        prices_data = {
            "price": "value",
            "another": "anval"
        }
        save_parsing_results(self.pid, **prices_data)

    def test_getting_info(self):
        self.assertIsInstance(get_results_by_id("pppp"), QuerySet)

    def test_get_all(self):
        self.assertEqual(get_all_pids(), ['pppp'])
