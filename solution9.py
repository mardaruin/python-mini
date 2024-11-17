from collections import OrderedDict
import unittest

class LRUCache:

    def __init__(self, capacity = 16):
        self.capacity = capacity
        self.cache = OrderedDict()

    def put(self, key, value):
        if key in self.cache:
            del self.cache[key]
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last = False)

    def get(self, key):
        if key not in self.cache:
            return None
        value = self.cache[key]
        del self.cache[key]
        self.cache[key] = value
        return value

class TestLRUCache(unittest.TestCase):
    def setUp(self):
        self.cache = LRUCache(capacity=3)

    def test_put_and_get(self):
        self.cache.put('a', 1)
        self.assertEqual(self.cache.get('a'), 1)

    def test_overflow(self):
        self.cache.put('a', 1)
        self.cache.put('b', 2)
        self.cache.put('c', 3)
        self.cache.put('d', 4)
        self.assertEqual(self.cache.get('b'), 2)
        self.assertEqual(self.cache.get('c'), 3)
        self.assertEqual(self.cache.get('d'), 4)
        self.assertEqual(self.cache.get('a'), None)

    def test_update_value(self):
        self.cache.put('a', 1)
        self.cache.put('a', 10)
        self.assertEqual(self.cache.get('a'), 10)


if __name__ == "__main__":
    unittest.main()
