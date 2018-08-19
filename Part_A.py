# WRITTEN BY    : BHANUKA GAMAGE (1000176)
# LAST MODIFIED : 11:10 AM 17/08/2017

################################# Assignment 1 ###############################
#################################### TASK 1 ##################################

################################## IMPORTS ###################################

# Importing os libarary
import os

################################## FUNCTIONS #################################

## Function to swap two elements in a list
def swap(aList,element1,element2):
    # Creating a temperory varible and assigning the value in the first index
    # of the list
    temp = aList[element1]
    # Assigning the item in the second index to the first index of the list 
    aList[element1] = aList[element2]
    # Assigning the temporary value to the second element
    aList[element2] = temp

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

## Function to fiter the line to remove the escape characters and put it in
## to a list
def filteringTheLine(line):
    # Splitting the line where there is a tab
    line = line.split("\t")
    # Splitting replacing the \n escape character with a blank space
    line[-1]=line[-1].replace("\n","")
    # Return the line
    return line

## Function to print the items in a list
def printAList(aList):
    # Traversing through the whole list
    for item in aList:
        # Printing the item with the end deliminator
        print(item, end=' ')



################################## CODE ######################################

## Defining the varaibles
totalPlanted = 0        # Defining the variable to store the total planted
totalHarvested = 0      # Defining the variable to store the total harvested
bedsInUse = []          # Defining the list to store the beds in use

## Printing the header of the output
print("---------------------- MCD4710 ASSIGNMENT 1 --------------------------")
print("------------------------ BHANUKA GAMAGE ------------------------------")
print("---------------------------- TASK A ----------------------------------")
print("---------------- NUMBER OF BEDS, SEEDS AND CROPS ---------------------")
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
        # Checking if the bed is in use
        if line[-3] not in bedsInUse:
            # If the bed is not in use add it to the list
            bedsInUse.append(line[-3])
        # Checking of the activity of the line is planting
        if (line[-2].lower()=="planting"):
            # If its planting, add to the totalPlanted
            totalPlanted = totalPlanted + int(line[-1])
        # Checking of the activity of the line is harvesting
        elif (line[-2].lower()=="harvesting"):
            # If its planting, add to the totalHarvested
            totalHarvested= totalHarvested + int(line[-1])

## Calling the selection sort function to sort the list
selectionSort(bedsInUse)

## Printing the output
print()
print("----------------------- Overview of the Data Set ----------------------")
print("-----------------------------------------------------------------------")

print()
print("Beds that are being used (according to the "+cropDataFile+")", end=' ')
print()

## Calling the printAList function
printAList(bedsInUse)

print()
print()
print("Total number of seeds planted   : " + str(totalPlanted))
print("Total number of crops harvested : " + str(totalHarvested))
