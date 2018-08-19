# WRITTEN BY    : BHANUKA GAMAGE (1000176)
# LAST MODIFIED : 09:00 PM 23/08/2017

################################# Assignment 1 ###############################
#################################### TASK 2 ##################################

################################## IMPORTS ###################################

# Importing os libarary
import os

################################## FUNCTIONS #################################

## Function to fiter the line to remove the escape characters and put it in
## to a list
def filteringTheLine(line):
    # Splitting the line where there is a tab
    line = line.split("\t")
    # Splitting replacing the \n escape character with a blank space
    line[-1]=line[-1].replace("\n","")
    # Return the line
    return line

## Function to swap two elements in a list
def swap(aList,element1,element2):
    # Creating a temperory variable and assigning the value in the first index
    # of the list
    temp = aList[element1]
    # Assigning the item in the second index to the first index of the list 
    aList[element1] = aList[element2]
    # Assigning the temporary value to the second element
    aList[element2] = temp

## Function to swap two elements in a table
def swapElementsInTable(aTable,element1,element2):
    # Creating a temperory variable and assigning the value in the first index
    # of the table
    temp = aTable[element1]
    # Assigning the item in the second index to the first index of the table
    aTable[element1] = aTable[element2]
    # Assigning the temporary value to the second element of the table
    aTable[element2] = temp
    
## Function to sort a list using Selection Sort Algorithm
def selectionSort(aList):
    # Travesing through all the elements in the list
    for element in range(len(aList)):
        #Assigning the first element as the minumum value
        minIndex = element
        # Travesing through remaining elements in the list
        for elementUnsorted in range(element+1,len(aList)):
            # Checking whether the item in the next index is less than the
            # current minimum
            if (int(aList[elementUnsorted]) < int(aList[int(minIndex)])):
                # If so, changing the index of that to the minimum index
                minIndex = elementUnsorted
        #Calling the swap function to swap the two elements               
        swap(aList,element,minIndex)

## Function to sort a table using Selection Sort Algorithm, index parameter is
## used to input the index of the table in which the sorting should happen
def selectionSortForTable(aTable,index):
    # Travesing through all the elements in the table
    for element in range(len(aTable)):
        #Assigning the first element as the minumum value
        minIndex = element
        # Travesing through remaining elements in the table
        for elementUnsorted in range(element+1,len(aTable)):
            # Checking whether the item in the next index is less than the
            # current minimum
            if (int(aTable[elementUnsorted][index]) < int(aTable[int(minIndex)][index])):
                # If so, changing the index of that to the minimum index
                minIndex = elementUnsorted
        #Calling the swap function to swap the two elements in the table                    
        swapElementsInTable(aTable,element,minIndex)

## Function to print the items in a list
def printAList(aList):
    # Traversing through the whole list
    for item in aList:
        # Printing the item with the end deliminator
        print(item, end=' ')

# Function to add a zero infront of the month if it is less than 10 
# and is entered without a leading zero
def convertMonth(month):
    #Checking if the month is between 10 and 0
    if int(month)<10 and int(month)>0:
        # If the leading zero is not present
        if month[0]!="0":
            # Add a leading zero
            month="0"+month
    return month

################################## CODE ######################################

## Defining the varaibles
yearsInDataSet=[]               # List to store the years in the dataset
monthsInDataSet=[]              # List to store the months in the dataset      
dateList=[];                    # List to store all the recorded dates in dataset
bedsInUse=[];                   # List to store all the details about the beds in use
bedsInUseSet=[];                # List to keep track of the beds currently in use
emptySet=[];                    # List to output the empty beds
totalOfCurrentPlantsInBeds = 0  # Variable to calculate the total beds planted


## Printing the header of the output
print("---------------------- MCD4710 ASSIGNMENT 1 --------------------------")
print("------------------------ BHANUKA GAMAGE ------------------------------")
print("---------------------------- TASK B ----------------------------------")
print("------------------------- BED OCCUPANCY ------------------------------")
print("----------------------------------------------------------------------")
print()


## Getting the user input file
cropDataFile = input("Please enter the name of the data file : ")
## Assigning the file name to filePath
filePath = cropDataFile
# Checking whether the file exist
pathExist = os.path.exists(filePath)

# Running a loop until the correct file in entered
while pathExist == False:
    ## Getting the user input file
    cropDataFile = input("FILE NOT FOUND. Please re-enter the name of the data file : ")
    ## Assigning the file name to filePath
    filePath = cropDataFile
    # Checking whether the file exist
    pathExist = os.path.exists(filePath)
    
    
## Opening the user input file
inputFile = open(cropDataFile,"r")

######################## Getting user data and verification ##################
#----------------------------------------------------------------------------#

## Travesing through the lines in the file
for line in inputFile:
    # Calling the filteringTheLine function
    line = filteringTheLine(line)
    # Skipping the first line of the text file
    if (line[0].lower() != "date") :
        # Splitting the data into three
        line[0]=(line[0].split("/"))
        # Appending the date to the date list
        dateList.append(line[0])
        # Checking whether the year is in yearsInDataSet list
        if line[0][-1] not in yearsInDataSet:
            # Adding the year to the yearsInDataSet list
            yearsInDataSet.append(line[0][-1])
        # Checking whether the month is in monthsInDataSet list
        if line[0][-2] not in monthsInDataSet:
            # Adding the month to the monthsInDataSet list
            monthsInDataSet.append(line[0][-2])

# Getting the user input for the year
year = input("Please enter the year :")
# Checking whether the user input is present in the list
while year not in yearsInDataSet:
    # If it is not present in the list, Display error message and get user
    # input
    year = input("YEAR NOT FOUND. Please enter a year in the Data File :")

# Getting the user input for the month
month = input("Please enter the month :")

# Calling the convert month function which will convert the month to the
# correct form
month = convertMonth(month)

# Checking whether the user input is present in the list           
while month not in monthsInDataSet:
    # If it is not present in the list, Display error message and get user
    # input
    month = input("MONTH NOT FOUND. Please enter a month in the Data File :")
    # Calling the convert month function which will convert the month to the
    # correct form
    month = convertMonth(month)

# Getting the user input for the day
day = input("Please enter the day (1-31):")

# Checking whether the user input is valid
while (int(day)>31 or int(day)<1):
    # If its not valid, displaying error message and getting valid input
    day = input("NOT A VALID DAY. Please enter a valid day:")

# Converting the user input date in to a string similar to the data set
userDate = str(day+"/"+month+"/"+year)

## Getting the last recorded date for the user entered date
# Travesing through the date list
for date in range(len(dateList)):
    # Checking whether the year is similar
    if dateList[date][-1]==year:
        # If the year is similar then checking the month
        if dateList[date][-2]==month:
            # Checking whether the date is between two recorded data values in the month
            if int(dateList[date][-3])<int(day) and int(dateList[date+1][-3])>int(day):
                #If so then consider crop date as the last recorded date for the month
                cropDate = dateList[date]
            # Else it is greater than the date
            elif int(dateList[date][-3])<int(day):
                # Then consider the next date as the crop date
                cropDate = dateList[date+1]
                # Break out of the loop
                break
            # Check whether the date is less than the recorded value for the month
            elif int(dateList[date][-3])>int(day):
                # If so consider the previous date
                cropDate = dateList[date-1]
                # Break out of the loop
                break

# Generating the last recorded value considering the user input
cropDate = str(cropDate[0]+"/"+cropDate[1]+"/"+cropDate[2])

########################### Calculating Bed Occupancy ########################
#----------------------------------------------------------------------------#

# Re-opening the file
inputFile = open(cropDataFile,"r")

## Travesing through the lines in the file
for inputLine in inputFile:
        # Running the filter line function
        inputLine = filteringTheLine(inputLine)
        # Skipping the first line of the text file
        if (inputLine[0].lower() != "date") :
            # Checking whether the bed is in the bedsInUseSet List
            if inputLine[-3] not in bedsInUseSet:
                # If not present, append the Bed nuber to beds in use
                bedsInUse.append([inputLine[-3]])
                # Appending the amount to bedsInUse
                bedsInUse[-1].append(inputLine[1])
                # Appednig a zero to the last index to calculate the current yeild
                bedsInUse[-1].append(0)

            # Checking if the activity on the bed is planting
            if (inputLine[-2].lower()=="planting"):
                # If so, travesing through the item in bedsInUse
                for item in range(len(bedsInUse)):
                    # Checking if the bed in bedsInUse is equal to the input file
                    if (bedsInUse[item][0]==inputLine[2]):
                        # If so adding the total planting to the last index (the sum)
                        bedsInUse[item][-1]=int(bedsInUse[item][-1]) + int(inputLine[-1])
                        # Adding the bed to the bedInUseSet
                        bedsInUseSet.append(inputLine[-3])                   
            # Else, checking if the activity on the bed is harvesting                      
            elif (inputLine[-2].lower()=="harvesting"):
                # If so, travesing through the item in bedsInUse
                for item in range(len(bedsInUse)):
                    # Checking if the bed in bedsInUse is equal to the input file
                    if (bedsInUse[item][0]==inputLine[2]):
                        # Pooping the item from the bedsInUse list
                        bedsInUse.pop(item)
                        # Removing the bed from the bedInUseSet list
                        bedsInUseSet.remove(inputLine[-3])
                        # Breaking out of the inner for loop
                        break
            # Checking if the line date is equal to the crop date                                                   
            if (inputLine[0]==cropDate):
                # Breaking out of the outer loop
                break

########################### Calculating the Empty Beds #######################
#----------------------------------------------------------------------------#

# Re-opening the file           
inputFile = open(cropDataFile,"r")


# Travesing through the input file
for line in inputFile:
    # Running the filter line function
    line = filteringTheLine(line)
    # Skipping the first line of the text file
    if (line[0].lower() != "date") :
        # Checking if the bed is in the empty list
        if line[-3] not in emptySet:
            # If not add eevrthing to the empty list
            emptySet.append(line[-3])

# Traversing through all the items in the bedsInUseSet         
for item in bedsInUseSet:
    # If the item is in the empty list
    if item in emptySet:
        # Remove the item
        emptySet.remove(item)

################## Calculating the total items in the farm ###################
#----------------------------------------------------------------------------#

# Traversing through the items in bedsInUse list       
for item in range(len(bedsInUse)):
    # Calculating the sum of the total plants in the farm
    totalOfCurrentPlantsInBeds += int(bedsInUse[item][-1])
    
# Calling the selection sort function to sort the items in the table
selectionSortForTable(bedsInUse,0)

# Calling the selection sort funtion to sort the items in the emptySet list
selectionSort(emptySet)

## Printing the output
print()
print("------- The Current Number of Plants in the Farm on "+userDate+ " -------")
print("----------------------------------------------------------------------")
print()

print("Beds that are currently being occupied")
print("---------------------------------------")
print()

print("%-10s%-12s%-12s%-12s" %(" ","Bed","Plant Type","Total Number Of Current Plants"))
print("%-10s%-12s%-12s%-12s" %(" ","---","----------","------------------------------"))

# Printing all the items in the bedsInUse list
for item in range(len(bedsInUse)):
    print("%-10s%-12s%-12s%-12s" %(" ",str(bedsInUse[item][0]),str(bedsInUse[item][1]),str(bedsInUse[item][2])))


print()
print("Empty Beds in the Farm")
print("-----------------------")
print()

## Calling the printAList function
printAList(emptySet)

print()
print("Total Plants in the Farm : "+ str(totalOfCurrentPlantsInBeds))


## Please comment out the above output, to view in the output that is displayed in the assignment
## Code to output in the line view
'''
print(date,end=" ")

# Printing all the items in the bedsInUse list
for item in range(len(bedsInUse)):
    print(str(bedsInUse[item][0])+" : "+str(bedsInUse[item][1])+"\t"+str(bedsInUse[item][2])+")", end=" ")
   
print("empty : [",end=" ")

printAList(emptySet)
print()
print("]", end=" ")
print("total :" + str(totalOfCurrentPlantsInBeds))

'''
