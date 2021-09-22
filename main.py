import pprint #used for requirement 3
import datetime #used for requirement 4


# read csv file
import csv
#requirenment 1
def req1():
    # read csv file and convert value to float and append list
    with open('Python Developer Test Dataset.csv', 'r') as file:
        reader = csv.DictReader(file)
        
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
def req2():
    with open('Python Developer Test Dataset.csv', 'r') as file:
        reader = csv.DictReader(file)
        
        rent = list()
        #get rows where lease years = 25
        wantedLease = [row for row in reader if int(row['Lease Years']) == 25 ]
        for row in wantedLease:
            print('\n')
            print(row)
            #append rent values to rent list as floats
            rent.append(float(row['Current Rent']))
        #calculate the total rent
        totalRent = sum(rent)
        print('\n')
        print('Total Rent = ', totalRent)   
        
#requirement 3
def req3():
    with open('Python Developer Test Dataset.csv', 'r') as file:
        reader = csv.DictReader(file)
         
        tenantMastCount = {}
        #iterate through tenant names
        for row in reader:
            #if alredy in dic , increase count
            if row['Tenant Name'] in tenantMastCount:   
                tenantMastCount[row['Tenant Name']] += 1
                #else initialize key
            else: tenantMastCount[row['Tenant Name']] = 1

        #Printing 
        #using pprint library
        #pprint.pprint(tenantMastCount)
        #iterating through key:value pairs
        print("Tenant mast count:")
        for name, count in tenantMastCount.items():  # dct.iteritems() in Python 2
            print("{} ({})".format(name, count))

#requirement 4    
def req4():
    with open('Python Developer Test Dataset.csv', 'r') as file:
        reader = csv.DictReader(file)
        
        #set the bhoundaries for the lease start date
        lowerBound = datetime.datetime(1999, 6, 1)
        upperBound = datetime.datetime(2007, 8, 31)
        
        #filter data according to boundaries by converting date strings to datetime fields
        wantedRentalDates = [row for row in reader if datetime.datetime.strptime(row['Lease Start Date'], '%d %b %Y') >lowerBound and datetime.datetime.strptime(row['Lease Start Date'], '%d %b %Y') < upperBound ]
        
        #print the data
        for ele in wantedRentalDates:
            print('\n')
            print(ele)
#all requirements
def allReq():
    req1()
    req2()
    req3()
    req4()

#if __name__ == '__main__':
#dictionary to hold key value pairs of finctions to perform depending on user input
func_dict = {'1':req1, '2':req2, '3':req3, '4':req4, '5': allReq}
userInput = input('Enter 1,2,3,4 to perform one of the operations or Enter 5 to perform all operations: ')
try:
    #check if userinput is a number
    value = int(userInput)
    if value in range(1,6):
        func_dict[userInput]()
    else: print('Entered number out of range, please reload program and choose a number between 1 and 5')
except:print('Please reload the program and enter a number')







    
    
    
       

    

     
        

        
