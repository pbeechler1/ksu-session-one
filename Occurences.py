#Class: CSE 1321L
#Section: W03
#Term:  Fall 2018
#Instructor: Solomon Walker
#Name: Phil Beechler
#Lab Num:  M7 - A7

class Ocurrences:

    def __init__(self):
        #substantiate array
        self.userList = []
        self.countArray = [] #will be used to hold the values of each instance
        print('Please enter the values of the array.')
        for x in range(0,10):
            self.userList.append(int(input('')))
        self.userList.sort()

    def count(self):
        #count method to count the number of occurences
        temp = 0
        for y in range(0, 10):
            countTemp = 0 #holds the value of number times element is counted
            temp = self.userList[y]
            for z in range(0, 10):
                if temp == self.userList[z]:
                    countTemp += 1
            self.countArray.append(countTemp) #appends value to an array at the same position as counted element

    def printList(self):
        #print method to generate outputs
        print('Entered integers: ', *self.userList)
        for a in range(0,len(self.userList)):
            print(self.userList[a], ' occurred: ', self.countArray[a], ' times.')


def main():
    myOccurObj = Ocurrences()
    myOccurObj.count()
    myOccurObj.printList()


main()
