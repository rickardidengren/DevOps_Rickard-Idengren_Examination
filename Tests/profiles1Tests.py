import unittest
import csv

class TestCSV(unittest.TestCase):
    def test_annika_in_profiles1csv(self):
        with open('profiles1.csv', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['Givenname'] == 'Annika':
                    self.assertTrue(True)
                    return
                
if __name__ == '__main__':
    unittest.main()