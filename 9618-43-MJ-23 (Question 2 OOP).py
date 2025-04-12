#--- Q2 (a) (i) --- 5/5
class Vehicle:
#DECLARE self.__ID : STRING
#DECLARE self.__MaxSpeed : INTEGER
#DECLARE self.__IncreaseAmount : INTEGER
#DECLARE self.__CurrentSpeed: INTEGER
#DECLARE self.__HorizontalPosition : INTEGER

    def __init__(self, id, MS, IA):
        self.__ID = id
        self.__MaxSpeed = MS
        self.__IncreaseAmount = IA
        self.__CurrentSpeed = 0
        self.__HorizontalPosition = 0
#--- (a) (ii) --- 3/3
    def GetCurrentSpeed(self):
        return self.__CurrentSpeed
    def GetIncreaseAmount(self):
        return self.__IncreaseAmount
    def GetHorizontalPosition(self):
        return self.__HorizontalPosition
    def GetMaxSpeed(self):
        return self.__MaxSpeed
#--- (a) (iii) --- 3/3
    def SetCurrentSpeed(self, NewSpeed):
        self.__CurrentSpeed = NewSpeed
    def SetHorizontalPosition(self, NHorizontalPosition):
        self.__HorizontalPosition = NHorizontalPosition
#--- (a) (iv) --- 3/3
    def IncreaseSpeed(self):
        if (self.__CurrentSpeed +self.__IncreaseAmount < self.__MaxSpeed):
            self.__CurrentSpeed = self.__CurrentSpeed + self.__IncreaseAmount
            self.__HorizontalPosition = self.__HorizontalPosition + self.__CurrentSpeed
        else:
            self.__CurrentSpeed = self.__MaxSpeed
            self.__HorizontalPosition = self.__HorizontalPosition + self.__CurrentSpeed
    def OutputDetails(self):
        print("Horizontal Position", self.__HorizontalPosition)
        print("Speed", self.__CurrentSpeed)
#--- (b) (i) --- 5/5
class Helicopter(Vehicle):
#DECLARE self.__VerticalChange : INETGER
#DECLARE self.__VerticalPositon : INTEGER
#DECLARE self.__MaxHeigth : INTEGER

    def __init__(self, VC, MH, id, MS, IA):
        Vehicle.__init__(self, id, MS, IA)
        self.__VerticalChange = VC
        self.__MaxHeight = MH
        self.__VerticalPosition = 0
#--- (b) (ii) ---
    def IncreaseSpeed(self):
        #for vertical position
        if (self.__VerticalPosition < self.__MaxHeight):
            self.__VerticalPosition = self.__VerticalPosition + self.__VerticalChange
        else:
            self.__VerticalPosition = self.__MaxHeight
        #increasing speed
        # if (self.__CurrentSpeed < self.__MaxSpeed):
        #     self.__CurrentSpeed = self.__CurrentSpeed + self.__IncreaseAmount
        #     self.__HorizontalPosition = self.__CurrentSpeed
        # else:
        #     self.__CurrentSpeed = self.__MaxSpeed
        #     self.__HorizontalPosition = self.__CurrentSpeed
        Vehicle.IncreaseSpeed(self)
    def OutputDetails(self):
        print("Vertical Position", self.__VerticalPosition)
        Vehicle.OutputDetails(self)
#--- (c) ---

# Heli1 = Helicopter(2, 10, 1, 20, 5)
# Heli1.IncreaseSpeed()

#--- (d) ---
Car = Vehicle("Tiger",100, 20)
Heli1 = Helicopter(3, 100, "Lion", 350, 40)

Car.IncreaseSpeed()
Car.IncreaseSpeed()
Car.OutputDetails()

Heli1.IncreaseSpeed()
Heli1.IncreaseSpeed()
Heli1.OutputDetails()







