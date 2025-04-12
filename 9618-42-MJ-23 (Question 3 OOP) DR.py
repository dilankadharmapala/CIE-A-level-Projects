#---Q3 (a) (i)---
#DECLARE self.__HourlyPay : REAL
#DECLARE self.__EmployeeNumber: STRING
#DECLARE self.__JobTitle: STRING
#DECLARE PayYear2022: ARRAY [0:51] (contains 52 elements) of REAL
class Employee:
    def __init__(self,HP, EmNum, JT ):
        self.__HourlyPay = HP
        self.__EmployeeNumber = EmNum
        self.__JobTitle = JT
        self._PayYear2022 = ["" for a in range(51)]
        for b in range (0,51):
            self._PayYear2022[b] = 0.0
#---(a) (ii)---
    def GetEmployeeNumber(self):
        return "The employee number is: ", self.__EmployeeNumber
#---(a) (iii)---
    def SetPay(self, WeekNumber, HoursWorked ):
        WeekPay = self.__HourlyPay * HoursWorked
        self._PayYear2022[WeekNumber] = WeekPay
#---(a) (iv)---
    def GetTotalPay(self):
        for c in range (0,51):
            YearlyPay = 0
            YearlyPay = YearlyPay + self._PayYear2022[c]
        return "The total pay in the year 2022 is: ", YearlyPay
#---(b) (i)---
#DECLARE self.__BonusValue : REAL
class Manager(Employee):
    def __init__(self, BV, HP, EmNum, JT):
        self.__BonusValue = BV
#---(b) (ii)--- Confusing
    def SetPay(self, WeekNumber, HoursWorked):
        factor = (self.__BonusValue+100)/100
        HoursWorked = HoursWorked * factor
