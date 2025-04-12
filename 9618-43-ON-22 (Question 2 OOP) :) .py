#--- Q2 (a) (i)--- 5/5
class Card:
    def __init__(self, n, c):
        #DECLARE Number: INTEGER
        #DECLARE Colour: STRING
        self.__Number = n
        self.__Colour = c
#--- (a) (ii)--- 3/3
    def GetNumber(self):
        return self.__Number
    def GetColour(self):
        return self.__Colour
#---(a)(iii)--- 2/2
Card1 = Card(1,"red")
Card2 = Card(2, "red")
Card3 = Card(3, "red")
Card4 = Card(4, "red")
Card5 = Card(5, "red")
Card6 = Card(1,"blue")
Card7 = Card(2,"blue")
Card8 = Card(3,"blue")
Card9 = Card(4,"blue")
Card10 = Card(5,"blue")
Card11 = Card(1,"yellow")
Card12 = Card(2,"yellow")
Card13 = Card(3,"yellow")
Card14 = Card(4,"yellow")
Card15 = Card(5,"yellow")
#---(b)(i)--- 6/6
class Hand:
    #DECLARE Cards ARRAY [0:9] OF Card
    #DECLARE FirstCard: INTEGER
    #DECLARE NumberCards: INTEGER
    def __init__(self, Card1, Card2, Card3, Card4, Card5):
        self.__Cards = ["","","","",""]
        self.__Cards[0] = Card1
        self.__Cards[1] = Card2
        self.__Cards[2] = Card3
        self.__Cards[3] = Card4
        self.__Cards[4] = Card5
        self.__FirstCard = 0
        self.__NumberCards = 5
#---(b)(ii)--- 2/2
    def GetCard(self, index):
        return self.__Cards[index]
#---(b)(iii)--- 2/2
Player1 = Hand(Card1, Card2, Card3, Card4, Card11)
Player2 = Hand(Card12, Card13, Card14, Card15, Card6)

# print(Player1.GetCard(0))
# Player1Card1 = Player1.GetCard(0)
# print(Player1Card1.GetColour())
# print(Player1Card1.GetNumber())
# Player2Card3 = Player2.GetCard(2)
# print(Player2Card3.GetColour())

#---(c)(i)--- 6/6
def CalculateValue(Player):
    #DECLARE Score: INTEGER
    #DCELARE Index: INTEGER
    #DECLARE CurrentColor: STRING
    #DECLARE CurrentNumber: INTEGER
    #DELCARE CurrentCard: Card
    Score = 0
    Index = 0
    while (Index <= 4):
        CurrentCard = Player.GetCard(Index)
        CurrentColor = CurrentCard.GetColour()
        CurrentNumber = CurrentCard.GetNumber()

        if (CurrentColor == "red"):
            Score = Score + 5 + CurrentNumber
        elif (CurrentColor == "blue"):
            Score = Score + 10 + CurrentNumber
        else:
            Score = Score + 15 + CurrentNumber
        Index = Index + 1
    return Score
#---(c) (ii)--- 4/4
PlayerScore1 = CalculateValue(Player1)
PlayerScore2 = CalculateValue(Player2)
print(PlayerScore1)
print(PlayerScore2)
if PlayerScore1 > PlayerScore2:
    print("Player 1 wins with a score of", PlayerScore1)
elif (PlayerScore2  PlayerScore1):
    print("Player 2 wins with a score of", PlayerScore2)
elif (PlayerScore1 == PlayerScore2):
    print("Draw both players have the same score")
#---(c) (iii)---