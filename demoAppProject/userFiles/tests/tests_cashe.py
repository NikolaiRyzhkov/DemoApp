from django.test import TestCase
from django.core.cache import cache


class CacheTestCase(TestCase):
    def test_set_val(self):
        cache.set('key_1', 1)

    def test_fet_val(self):
        result = cache.get('key_1')
        TestCase.assertEqual(self, result, 1)