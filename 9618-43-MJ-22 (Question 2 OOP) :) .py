#---Q2 (a)--- 5/5
class Balloon:
# DECLARE Health: INTEGER
# DECLARE Colour: STRING
# DECLARE DefenceItem: STRING
    def __init__ (self, d, c):
        self.__DefenceItem = d
        self.__Colour = c
        self.__Health = 100
#---(b)--- 2/2
    def GetDefenceItem(self):
        return "Your defence item is", self.__DefenceItem
#---(c)--- 2/2
    #DECLARE Value: INTEGER
    def ChangeHealth(self, Value):
        self.__Health = self.__Health + Value
#---(d)--- 2/2
    #DECLARE Check: BOOLEAN
    def CheckHealth(self):
        if (self.__Health <= 0):
            Check = True
        else:
            Check = False
        return Check

#main--------------------------------------
#---(e)--- 3/3
DItem = str(input("Please select your defence item: "))
BColour = str(input("Please enter the colour of your balloon"))

Balloon1 = Balloon(DItem, BColour)
#---(f)--- 8/8
def Defend(Balloon2):
    OpponentStrength = int(input("Please enter you opponent's strength value"))
    Health = Balloon2.ChangeHealth(-OpponentStrength)
    print(Balloon2.GetDefenceItem())
    HealthStatus = Balloon2.CheckHealth()
    if (HealthStatus == True):
        print("No health remaining you cannot defend anymore")
    else:
        print("Health remaining, keep defending!")
    return Balloon2
#---(g)--- 2/2
Balloon1 = Defend(Balloon1)
#---(g) (i) ---

