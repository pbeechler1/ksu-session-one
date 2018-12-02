#Class: CSE 1321L
#Section: W03
#Term:  Fall 2018
#Instructor: Solomon Walker
#Name: Phil Beechler
#Lab Num:  M7 - A7

class MinMaxAvg:

    def __init__(self):
        #initializes variables
        self.gradesMatrix = []
        self.highestGrade = 0
        self.lowestGrade = 100
        self.classAverage = 0.0

    def grades(self):
        #appends random values to grades matrix
        import random
        for x in range(0,4):
            tempArray = []
            for y in range(0,4):
                tempArray.append(random.randint(1,100))
            self.gradesMatrix.append(tempArray)

    def minMaxAvg(self):
        #calculatues highest, lowest, and class avg
        tempGrade = 0
        for x in range (0,4):
            for y in range (0,4):
                if self.gradesMatrix[x][y] > self.highestGrade: #gets highest
                    self.highestGrade = self.gradesMatrix[x][y]
                if self.gradesMatrix[x][y] < self.lowestGrade: #gets lowest
                    self.lowestGrade = self.gradesMatrix[x][y]
                tempGrade += self.gradesMatrix[x][y]#adds all values
        self.classAverage = tempGrade / 16.0 #calculates average
        #return tuple with highest, lowest, and average
        return self.highestGrade, self.lowestGrade, self.classAverage

    def printMatrix(self):
        #prints out matrix in 4x4 pattern
        for x in range(0,4):
            for y in range(0,4):
                print(self.gradesMatrix[x][y], end=' ')
            print()

def main():
    myGradesObj = MinMaxAvg()
    myGradesObj.grades()
    minMaxAvg = myGradesObj.minMaxAvg()
    print('Array Grades: ')
    myGradesObj.printMatrix()
    print('Highest grade: ', minMaxAvg[0])
    print('Lowest grade: ', minMaxAvg[1])
    print('Class average: ', minMaxAvg[2])


main()
