import json# used to print data 
import datetime #used for requirement 4
# read csv file
import csv
#requirenment 1
def req1(data):
    #sort the list
    data.sort(key=lambda r:float(r['Current Rent']))
    return data[:5] 

#requirement 2   
def req2(data):    
    #get rows where lease years = 25
    wantedLease = [row for row in data if int(row['Lease Years']) == 25 ]
    totalRent = 0
    for row in wantedLease:
        #append rent values to rent list as floats
        totalRent += float(row['Current Rent'])
    #calculate the total rent
    result = dict()
    result['Total Rent'] = totalRent
    result['Wanted Lease'] = wantedLease
    return result
          
#requirement 3
def req3(data):    
    tenantMastCount = dict()
    #iterate through tenant names
    for row in data:
        #if not in dic , init
        if not row['Tenant Name'] in tenantMastCount: 
            tenantMastCount[row['Tenant Name']] = 0
        tenantMastCount[row['Tenant Name']] += 1   
    #Printing 
    print("Tenant mast count:")
    return tenantMastCount

#requirement 4    
def req4(data):
    #set the bhoundaries for the lease start date
    lowerBound = datetime.datetime(1999, 6, 1)
    upperBound = datetime.datetime(2007, 8, 31)
    #filter data according to boundaries by converting date strings to datetime fields
    wantedRentalDates = [row for row in data
        if datetime.datetime.strptime(row['Lease Start Date'], '%d %b %Y') >lowerBound and datetime.datetime.strptime(row['Lease Start Date'], '%d %b %Y') < upperBound ]
    #print the data
    return wantedRentalDates

#all requirements
def allReq(data):
    result = dict()
    for key,func in func_dict.items():
        if key != '5': 
            result[key] = func(data)
    return result

#dictionary to hold key value pairs of finctions to perform depending on user input
func_dict = {'1':req1, '2':req2, '3':req3, '4':req4, '5': allReq}
def run(name, data):
    print(json.dumps(func_dict[name](data), indent=4))

userInput = input('Enter 1,2,3,4 to perform one of the operations or Enter 5 to perform all operations: ')    
with open('Python Developer Test Dataset.csv', 'r') as file:
    reader = csv.DictReader(file)
    data = [row for row in reader]
    if userInput in func_dict.keys():
        run(userInput, data)           
    else: print('Entered number out of range or a letter was entered, please reload program and choose a number between 1 and 5')


