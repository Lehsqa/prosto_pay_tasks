import unittest

from hash_map import HashMap


class TestHashMap(unittest.TestCase):
    def setUp(self):
        # Initialize a HashMap with a size of 5 for testing
        self.hash_map = HashMap(5)

    def test_put_and_get(self):
        # Test putting key-value pairs and getting values using the 'put' and 'get' methods
        self.hash_map.put("key1", "value1")
        self.assertEqual(self.hash_map.get("key1"), "['key1', 'value1']")

        self.hash_map.put("key2", "value2")
        self.assertEqual(self.hash_map.get("key2"), "['key2', 'value2']")

    def test_update_existing_key(self):
        # Test updating an existing key with a new value using the 'put' method
        self.hash_map.put("key1", "value1")
        self.assertEqual(self.hash_map.get("key1"), "['key1', 'value1']")

        # Update the existing key
        self.hash_map.put("key1", "new_value")
        self.assertEqual(self.hash_map.get("key1"), "['key1', 'new_value']")

    def test_remove(self):
        # Test removing a key-value pair using the 'remove' method
        self.hash_map.put("key1", "value1")
        self.hash_map.put("key2", "value2")
        self.hash_map.put("key3", "value3")
        self.assertEqual(self.hash_map.get("key1"), "['key1', 'value1']")
        self.assertEqual(self.hash_map.get("key2"), "['key2', 'value2']")

        # Remove 'key2' and assert that it's now None
        self.hash_map.remove("key2")
        self.assertIsNone(self.hash_map.get("key2"))

    def test_serialize(self):
        # Test serializing the HashMap using the 'str' method
        self.hash_map.put("key1", "value1")
        self.hash_map.put("key2", "value2")

        # The expected serialized representation of the HashMap
        expected = "[][][][['key1', 'value1']][['key2', 'value2']]"
        self.assertEqual(str(self.hash_map), expected)
