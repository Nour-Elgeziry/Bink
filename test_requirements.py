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

    def test_req2_returns_leaseYears_equlas_25(self):
         with open('Python Developer Test Dataset.csv', 'r') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
            result = requiremetns.req2(data)
            #geting the value of the Wanted Lease key from the returned dict result
            wantedLease = result['Wanted Lease']
            leaseYears = [obj['Lease Years'] for obj in wantedLease ]
            #checking every obj in list has wanted lease value of 25
            for ele in leaseYears:
                self.assertEqual(int(ele), 25)

    def test_req2_sum_of_total_rent(self):
        with open('Python Developer Test Dataset.csv', 'r') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
            result = requiremetns.req2(data)
            #geting the value of the Total Rent key from the returned dict result
            totalRent = result['Total Rent']
            #46500.0 calculated total rent
            self.assertEqual(46500.0, totalRent)

if __name__ == "__main__":
    unittest.main()