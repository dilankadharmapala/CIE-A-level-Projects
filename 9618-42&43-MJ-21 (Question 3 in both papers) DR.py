#---Q3 (a)--- 5/5
class TreasureChest:
#DECLARE self.__question : STRING
#DECLARE self.__answer : INTEGER
#DECLARE self.__points : INTEGER
    def __init__ (self, q, a, p):
        self.__question = q
        self.__answer = a
        self.__points = p

#---(b)--- 1/8 I need to learn the File Handling code
def readData():

#---(c) (i)--- 1/1
    def getQuestion(self):
        return self.__question
#---(c) (ii)--- 1/3 I don't understand the parameter selected
    def checkAnswer(self, UserAnswer ):
        if (UserAnswer == self.__Answer):
            return True
        else:
            return False
#---(c) (iii)--- 2/5 I don't understand thi
    def getPoints(self, NumOfAttempts):
        if (NumOfAttempts == 1):
            return self.__points
        elif (NumOfAttempts == 2):
            return int(self.__points/2)
        elif (NumOfAttempts == 3 or NumOfAttempts == 4):
            return int(self.__points/4)
        else:
            return 0
#---(c) (iv)--- 2/7
readData()
Num = int(input("Please enter a number between 1 and 5"))




