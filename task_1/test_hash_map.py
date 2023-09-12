import unittest
from hash_map import HashMap


class TestHashMap(unittest.TestCase):
    def setUp(self):
        self.hash_map = HashMap(5)

    def test_put_and_get(self):
        self.hash_map.put("key1", "value1")
        self.assertEqual(self.hash_map.get("key1"), "['key1', 'value1']")

        self.hash_map.put("key2", "value2")
        self.assertEqual(self.hash_map.get("key2"), "['key2', 'value2']")

    def test_update_existing_key(self):
        self.hash_map.put("key1", "value1")
        self.assertEqual(self.hash_map.get("key1"), "['key1', 'value1']")

        # Update the existing key
        self.hash_map.put("key1", "new_value")
        self.assertEqual(self.hash_map.get("key1"), "['key1', 'new_value']")

    def test_remove(self):
        self.hash_map.put("key1", "value1")
        self.hash_map.put("key2", "value2")
        self.hash_map.put("key3", "value3")
        self.assertEqual(self.hash_map.get("key1"), "['key1', 'value1']")
        self.assertEqual(self.hash_map.get("key2"), "['key2', 'value2']")

        self.hash_map.remove("key2")
        self.assertIsNone(self.hash_map.get("key2"))

    def test_serialize(self):
        self.hash_map.put("key1", "value1")
        self.hash_map.put("key2", "value2")

        expected = "[][][][['key1', 'value1']][['key2', 'value2']]"
        self.assertEqual(str(self.hash_map), expected)
