# WRITTEN BY    : BHANUKA GAMAGE (1000176)
# LAST MODIFIED : 07:00 AM 24/08/2017

################################ Assignment 1 ################################
################################### TASK 3 ###################################

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

## Function to swap two elements in a table
def swapElementsInTable(aTable,element1,element2):
    # Creating a temperory variable and assigning the value in the first index
    # of the table
    temp = aTable[element1]
    # Assigning the item in the second index to the first index of the table
    aTable[element1] = aTable[element2]
    # Assigning the temporary value to the second element of the table
    aTable[element2] = temp

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
            if (int(aTable[elementUnsorted][index]) > int(aTable[int(minIndex)][index])):
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
    # Going to the next line       
    print()

################################## CODE ######################################

## Defining the varaibles
totalPlanted=0              # Varaible to store the total planted
totalHarvested=0            # Variable to store the total harvested
plants=[]                   # List to store the name of the plants 
plantedHarvestedTable=[]    # List to store the details of the yeilds

## Printing the header of the output
print("---------------------- MCD4710 ASSIGNMENT 1 --------------------------")
print("------------------------ BHANUKA GAMAGE ------------------------------")
print("---------------------------- TASK C ----------------------------------")
print("-------------------------- YIELD DATA --------------------------------")
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

## Travesing through the lines in the file
for line in inputFile:
    # Calling the filteringTheLine function
    line = filteringTheLine(line)
    # Skipping the first line of the text file
    if (line[0].lower() != "date") :
        # Checking if the plant is in the list
        if line[1] not in plants:
            # If not, append it to the plants list
            plants.append(line[1])
            # Appending to the plants harvested table
            plantedHarvestedTable.append([line[1]])
            # Appending zero to item in the list
            plantedHarvestedTable[-1].append(0)
            # Appending zero to item in the list
            plantedHarvestedTable[-1].append(0)
            
        # Checking whether the activity is planting
        if (line[-2].lower()=="planting"):
            # Travesing all the items in plants
            for item in range(len(plants)):
                # If item is equal to the data file item
                if (plantedHarvestedTable[item][0]==line[1]):
                    # Add the amount of harvested to the list
                    plantedHarvestedTable[item][1]=int(plantedHarvestedTable[item][1]) + int(line[-1])
                                      
        # Checking whether the activity is harvesting                 
        elif (line[-2].lower()=="harvesting"):
            # Travesing all the items in plants
            for item in range(len(plants)):
                # If item is equal to the data file item
                if (plantedHarvestedTable[item][0]==line[1]):
                    # Add the amount of harvested to the list
                    plantedHarvestedTable[item][2]=int(plantedHarvestedTable[item][2]) + int(line[-1])
                    # Breaking out of the loop
                    break

########################### Calculating the Percentage #######################
#----------------------------------------------------------------------------#
                
# Traversing through items in plants
for item in range(len(plants)):
    # Calculating the propotion
    harvestedPropotion = int(plantedHarvestedTable[item][2])/int(plantedHarvestedTable[item][1])
    # Appedning the propotion to the list
    plantedHarvestedTable[item].append(harvestedPropotion)
    # Multiplying the propotion by 100 to get the percentage
    plantedHarvestedTable[item][-1]=plantedHarvestedTable[item][-1]*100

# Calling the selection sort function to sort the items in the table in
# desecnding order
selectionSortForTable(plantedHarvestedTable,3)

## Printing the output
print()
print("------------------------ Annual Yeilds -------------------------------")
print("----------------------------------------------------------------------")

print("%-23s%-15s%-15s" %(" ","Plant Type","Yeild"))
print("%-23s%-15s%-15s" %(" ","----------","-----"))

# Printing all the items in the plantedHarvestedTable list
for item in range(len(plantedHarvestedTable)):
    print("%-23s%-15s%.2f %%" %(" ",str(plantedHarvestedTable[item][0]),(plantedHarvestedTable[item][-1])))

