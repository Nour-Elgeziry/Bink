# read csv file
import csv
# read csv file and convert value to float and append list
with open('Python Developer Test Dataset.csv') as file:
    rentList = list()
    reader = csv.DictReader(file) 
    for row in reader:
        rentList.append(float(row['Current Rent']))
    
    #sort the list
    sortedRentList = sorted(rentList)
    #output first 5 values
    count = 0
    for val in sortedRentList:
        if count > 4:
            break
        print(val)
        count += 1

        
    
        
    