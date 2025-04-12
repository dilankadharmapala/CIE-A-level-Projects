#--- Q3 (a) ---
#DECLARE self.__Number: INTEGER
#DECLARE self.__Colour: STRING
class Card:
    def __init__(self, n, c ):
        self.__Number = n
        self.__Colour = c
#---(b)---
    def GetNumber(self):
        return self.__Number
    def GetColour(self):
        return self.__Colour
#---(c)--- How do I access a file?
#DECLARE CardArray: [1:30] ARRAY of Card
CardArray = ["" for i in range(30)]
try: #for practice
    File = open("../../../Text Files/CardValues.txt", 'r')
    for i in range(30):
        Currentnum = int(File.readline())
        currentColour = File.readline()
        CardArray[i] = Card(Currentnum, currentColour)
    File.close()
    print(CardArray)
    print(CardArray[1].GetColour()) #to get each object
except Exception as e:
    print(e)
