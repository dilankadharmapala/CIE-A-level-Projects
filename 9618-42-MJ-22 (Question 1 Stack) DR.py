#--- Q1 (a)--- 3/3
#DECLARE StackArray: Array of 10 elements
#DECLARE StackPointer: INTEGER
global StackArray
global StackPointer
StackArray = ["" for i in range(10)]
StackPointer = 0

#---(b)--- 3/3
def OutputAll():
    global StackArray
    global StackPointer
    length = len(StackArray)
    index = 0
    for index in range (length):
        print(StackArray[index])
    print("The stack pointer is: ", StackPointer)
#---(c)--- 6/6
#DECLARE Value: INTEGER
def Push(Value):
    global StackArray
    global StackPointer
    maxsize = len(StackArray)

    if (StackPointer == maxsize): #when stack is full
        return False
    else: #when stack is not full
        StackArray[StackPointer] = Value
        StackPointer = StackPointer + 1
        return True
#----------------main
#---(d) (i) --- 4/5 tiny doubt need ms
StackArray = ["" for b in range(11)]
checkfull = True
while (checkfull == True):
    Data = input("Please enter a number: ")
    if (Push(Data) == False):
        print("Sorry the stack is full the value cannot be added")
        checkfull = False
    else:
        print("Successfully added")
print(StackArray) #is this okay?

#---(d) (ii)--- 1/1

#---(e) (i)--- 5/5
def Pop():
    global StackArray
    global StackPointer
    maxsize = len(StackArray)

    if (StackPointer == 0): #when stack is empty
        return -1
    else: #when stack is not empty
        RemoveValue = StackArray[StackPointer-1]
        StackPointer = StackPointer - 1
        return RemoveValue



#---(e) (ii)--- 0/2 It doesnt work
Pop()
Pop()
