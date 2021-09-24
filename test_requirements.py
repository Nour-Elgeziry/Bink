import unittest
import requiremetns 
import objToTest
import csv
import datetime

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

    def test_req3_max_of_15_tenants(self):
         with open('Python Developer Test Dataset.csv', 'r') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
            result = requiremetns.req3(data)
            #check returned no of tenants equals 15
            self.assertEqual(len(result), 15)

    def test_req3_maximum_tenant_mast_count_equals_16(self):
        with open('Python Developer Test Dataset.csv', 'r') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
            result = requiremetns.req3(data)
            #check returned max tenant count equals 16
            maxMastKey = max(result, key=result.get)
            self.assertEqual(result[maxMastKey],16)

    def test_req4_data_leaseYear_between_given_dates(self):
        with open('Python Developer Test Dataset.csv', 'r') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
            result = requiremetns.req4(data)
            dates = [row['Lease Start Date'] for row in result]
            #check each date is between boundaries
            lowerBound = datetime.datetime(1999, 6, 1)
            upperBound = datetime.datetime(2007, 8, 31)
            for date in dates:
                date = datetime.datetime.strptime(date, '%d %b %Y')
                self.assertGreater(date, lowerBound)
                self.assertLess(date, upperBound)
    
    def test_req5_should_retunr_dict_of_length_4_key_value_pairs(self):
        with open('Python Developer Test Dataset.csv', 'r') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
            result = requiremetns.allReq(data)
            #check the length of returned dict equals 4
            self.assertEqual(len(result), 4)



    





if __name__ == "__main__":
    unittest.main()