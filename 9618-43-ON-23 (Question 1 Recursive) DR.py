#---Q1 (a) (i)---
def IterativeVowels(Value):
    Total = 0
    LengthString = len(Value)
    for X in range(0,LengthString):
        FirstCharacter = Value[X]
        print(FirstCharacter)
        if (FirstCharacter == "a") or (FirstCharacter == "e") or (FirstCharacter == "i") or (FirstCharacter == "o") or (FirstCharacter == "u"):
            Total = Total + 1
    return Total
NumberOfVowels = IterativeVowels("dilanka")
print(NumberOfVowels)





#---(b) (i)---
def RecursiveVowels(Value):
    #
