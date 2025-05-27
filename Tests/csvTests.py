import unittest
import csv

class TestCSVRowColumn(unittest.TestCase):
    def setUp(self):
        self.filename = 'profiles1.csv'

    def test_csv_has_12_columns(self):
        with open(self.filename, mode='r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
        self.assertEqual(len(header), 12, f"The file should have 12 columns but has {len(header)}")

    def test_csv_has_over_900_rows(self):
        with open(self.filename, mode='r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)
            rows = list(reader)
        self.assertGreater(len(rows), 900, f"The file should have over 900 rows but has {len(rows)}")

if __name__ == '__main__':
    unittest.main()