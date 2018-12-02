#Class: CSE 1321L
#Section: W03
#Term:  Fall 2018
#Instructor: Solomon Walker
#Name: Phil Beechler
#Lab Num:  M7 - A7

class WeeklyHours:

    def __init__(self):
        #initializes variables and substantiates matrix
        self.employeeHours = []
        self.employeeWeekHrs = []
        import random
        for x in range(0,3):
            tempArray = []
            for y in range(0,7):
                tempArray.append(random.randint(1,10))
            self.employeeHours.append(tempArray)

    def addHours(self):
        #adds weekly hours and inputs into new array
        for x in range(0,3):
            weekHours = 0
            for y in range(0,7):
                weekHours += self.employeeHours[x][y]
            self.employeeWeekHrs.append(weekHours)
        return self.employeeWeekHrs

    def printMatrix(self):
        #prints out matrix in 3x7 pattern
        for x in range(0,3):
            if x<1:
                print('Employee#     M  T  W  TH  F  S  SU')
            print(x+1, end='            ')
            for y in range(0,7):
                print('', self.employeeHours[x][y], end=' ')
            print()

def main():
    myEmployeeObj = WeeklyHours()
    weeklyHours = myEmployeeObj.addHours()
    print('Employees Data:')
    myEmployeeObj.printMatrix()
    print('Employee #     Weekly Hours')
    for x in range(0,3):
        print('   ', x+1, '           ', weeklyHours[x])


main()
