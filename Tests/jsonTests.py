import unittest
import json

class TestJSONSRowProperties(unittest.TestCase):
    def setUp(self):
        self.filename = 'data.json'

    def test_json_have_12_properties(self):
        with open(self.filename, mode='r', encoding='utf-8') as f:
            data = json.load(f)

            self.assertIsInstance(data, list, "The JSON-file should have a list with objects")

            for i, obj in enumerate(data):
                self.assertIsInstance(obj, dict, f"Row {i} is not an object (dict)")
                self.assertEqual(len(obj), 12, f"The object on row {i} have {len(obj)} properties, not 12")

if __name__ == '__main__':
    unittest.main()
    
