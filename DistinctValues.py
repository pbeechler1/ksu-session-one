#Class: CSE 1321L
#Section: W03
#Term:  Fall 2018
#Instructor: Solomon Walker
#Name: Phil Beechler
#Lab Num:  M7 - A7

class DistinctValues:

    def __init__(self):
        #initializes and adds value to array
        self.userList = []
        self.distinctArray = []
        print('Please enter the values for the array.')
        for x in range(0,10):
            self.userList.append(int(input('')))

    def getValues(self):
        #returns distinct array
        temp = 0
        for y in range(0,len(self.userList)):
            nonDistinctCounter = 0
            temp = self.userList[y]
            for z in range(0,len(self.userList)):
                if(self.userList[z] == temp):
                    nonDistinctCounter += 1
            if nonDistinctCounter <= 1:
                self.distinctArray.append(temp)

    def printOut(self):
        print('Original Array: ', *self.userList)
        print('Distinct Array: ', *self.distinctArray)


def main():
    myDistinctObj = DistinctValues()
    myDistinctObj.getValues()
    myDistinctObj.printOut()

main()
