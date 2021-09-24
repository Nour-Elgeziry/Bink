import unittest
import requiremetns 
import objToTest
import csv

class testRequirements(unittest.TestCase):
    def test_req1_with_given_csv_file(self):
        with open('Python Developer Test Dataset.csv', 'r') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
            result = requiremetns.req1(data)
            self.assertEqual(result, objToTest.obj1)

    def test_req1_with_empty_list(self):
            data = []
            result = requiremetns.req1(data)
            self.assertEqual(result, [])

    def test_req1_with_one_elemnt(self):
        obj = objToTest.obj2
        result = requiremetns.req1(obj)

        self.assertEqual(result, obj)

        
if __name__ == "__main__":
    unittest.main()