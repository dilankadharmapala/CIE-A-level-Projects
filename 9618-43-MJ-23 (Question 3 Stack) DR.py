#--- Q3 (a)--- 3/3
#DECLARE Animal: ARRAY [0:19] of STRING
#DECLARE Colour: ARRAY [0:9] of STRING
#DECLARE AnimalTopPointer: INTEGER
#DECLARE ColourTopPointer: INTEGER
global Animal
global Colour
global AnimalTopPointer
global ColourTopPointer

Animal = ["" for i in range(20)]
Colour = ["" for j in range (10)]
AnimalTopPointer = 0
ColourTopPointer = 0

#---(b) (i)--- 3/3
def PushAnimal(DataToPush):
    global Animal
    global AnimalTopPointer

    if (AnimalTopPointer == 20): #when stack is full
        return False
    else: #when stack is not full
       Animal[AnimalTopPointer] = DataToPush
       AnimalTopPointer = AnimalTopPointer + 1
       return True
#---(b) (ii)--- 3/3
#DECLARE ReturnData: STRING
def PopAnimal():
    global Animal
    global AnimalTopPointer

    if (AnimalTopPointer == 0): #when stack is empty
        return ""
    else: #when stack is not empty
        ReturnData = Animal[AnimalTopPointer - 1]
        AnimalTopPointer = AnimalTopPointer - 1
        return ReturnData

#---(b) (iii)--- 0/5 Need to go through file handling


#---(b) (iv)--- 2/2
def PushColour(DataToPush):
    global Colour
    global ColourTopPointer

    if ( ColourTopPointer == 10):  # when stack is full
        return False
    else:  # when stack is not full
        Colour[ColourTopPointer] = DataToPush
        ColourTopPointer = ColourTopPointer + 1
        return True

#DECLARE ReturnData: STRING
def PopColour():
    global Colour
    global ColourTopPointer

    if (ColourTopPointer == 0):  # when stack is empty
        return ""
    else:  # when stack is not empty
        ReturnData = Colour[ColourTopPointer - 1]
        ColourTopPointer = ColourTopPointer - 1
        return ReturnData

#---(b) (v)--- 0/2 Need to go through file handling

#---(c)--- 5/5 but can I use elif here?
def OutputItem():
    global Animal
    global Colour
    global AnimalTopPointer
    global ColourTopPointer

    CheckColour = PopColour()
    CheckAnimal = PopAnimal()
    if (CheckColour == ""): #
        PushAnimal(CheckAnimal)
        print("No colour")
    elif (CheckAnimal == ""):
        PushColour (CheckColour)
        print("No Animal")
    else:
        print(CheckColour, CheckAnimal)

#---(d) (i)--- 0/1 Need to go through file handling

#--(d) (ii)--- 0/1 Need to go through file handling











