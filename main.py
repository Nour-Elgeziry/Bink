import pprint
# read csv file
import csv
# read csv file and convert value to float and append list
with open('Python Developer Test Dataset.csv', 'r') as file:
    reader = csv.DictReader(file)
    '''
    #requirenment 1
    rentList = list()
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
    
    #requirement 2
    rent = list()
    #get rows where lease years = 25
    wantedLease = [row for row in reader if int(row['Lease Years']) == 25 ]
    for row in wantedLease:
        print(row)
        #append rent values to rent list as floats
        rent.append(float(row['Current Rent']))
    #calculate the total rent
    totalRent = sum(rent)
    print(totalRent)   
'''
    #requirement 3 
    tenantMastCount = {}
    #iterate through tenant names
    
    for row in reader:
        if row['Tenant Name'] in tenantMastCount:
             #if alredy in dic , increase count
            tenantMastCount[row['Tenant Name']] += 1
            #else initialize key
        else: tenantMastCount[row['Tenant Name']] = 1

    #using pprint library
    #pprint.pprint(tenantMastCount)
    #iterating through key:value pairs
    print("Tenant mast count:")
    for name, count in tenantMastCount.items():  # dct.iteritems() in Python 2
        print("{} ({})".format(name, count))
        



    
    
       

    

     
        

        
