#Class: CSE 1321L
#Section: W03
#Term:  Fall 2018
#Instructor: Solomon Walker
#Name: Phil Beechler
#Lab Num:  M7 - A7

class IndexOfLargest:

    def __init__(self):
        #initializes array
        self.userList = []

    def getValues(self):
        #adds the values to the array
        print('Please enter the values for the array.')
        for x in range(0,10):
            self.userList.append(int(input('')))

    def findIndex(self):
        #finds the index
        maxValue = max(self.userList) #grabs max value
        maxValueIndex = self.userList.index(maxValue) #grabs index of max value
        return maxValueIndex #returns the index

    def printOut(self):
        print('Entered Integers: ', *self.userList)


def main():
    myIndexObject = IndexOfLargest() #creates object
    myIndexObject.getValues() #gets the values of the array from user
    myIndexObject.printOut() #gets list
    print('Index of the largest value is ', myIndexObject.findIndex()) #prints out the index of largest value


main()
