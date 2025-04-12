#--- Q3 (a) (i) --- #why aren't they private?
class Character:
    #DECLARE self.__Name : STRING
    #DECLARE self.__XPosition : INTEGER
    #DECLARE self.__YPosition : INTEGER
    def __init__(self, N, X, Y):
        self.__Name = N
        self.__XPosition = X
        self.__YPosition = Y
#---(a) (ii)---
    def GetXPosition(self):
        return self.__XPosition
    def GetYPosition(self)
        return self.__YPosition
#---(a) (iii)---
    def SetXPosition(self, MoveX):
        self.__XPosition = self.__XPosition + MoveX
        if (self.__XPosition > 10000):
            self.__XPosition = 10000
        elif (self.__XPosition < 0):
            self.__XPosition = 0

    def SetYPosition(self, MoveY):
        self.__YPosition = self.__YPosition + MoveY
        if (self.__YPosition > 10000):
            self.__YPosition = 10000
        elif (self.__YPosition < 0):
            self.__YPosition = 0
#---(a) (iv)--- #don't get it at all
    def Move(self, direction):
        XValue = self.__XPosition
        YValue = self.__YPosition
        if (direction == "up"):
            Value = YValue + 10
            SetYPosition(Value)
        elif (direction == "down"):
            Value = YValue - 10
        elif (direction == "left"):
            Value = XValue - 10
        elif (direction == "right"):
            Value = XValue + 10
#---(b)--- 2/2
Jack = Character("Jack", 50 , 50)

#---(c) (i)---
class Bike(Character):
    def __init__(self, N1, X1, Y1):
        self._Name = N1
        self._XPosition = X1
        self._YPosition = Y1
#---(d)---
Karla = Bike("Karla", )




