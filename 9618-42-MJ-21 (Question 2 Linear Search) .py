#--- Q2 (a) --- 2/2
#DECLARE arrayData: ARRAY [0:9] OF INTEGER
arrayData = []
arrayData.append(10)
arrayData.append(5)
arrayData.append(6)
arrayData.append(7)
arrayData.append(1)
arrayData.append(12)
arrayData.append(13)
arrayData.append(15)
arrayData.append(21)
arrayData.append(8)

#--- (b) (i) --- 6/6
#DECLARE num: INTEGER
def linearSearch(num):
    boundary = len(arrayData)
    check = False
    for i in range (0,boundary):
        if (arrayData[i] == num):
            check = True
    return check

    # if (check == True):
    #     print(num, "exists in the array")
    # else:
    #     print(num, "does not exist in the array")

#--- (b) (ii) --- 4/4
userNum = int(input("Please enter a number: "))
SearchValue = linearSearch(userNum)
if (SearchValue == True):
    print(userNum, "was found")
else:
    print(userNum, "was not found")
 #---- (c) ---- inner loop is always one lesser than the outer loop 6/6
 #DECLARE temp: INTEGER

def bubbleSort():
    for x in range (0,10):
        #print("outer loop" , x)
        for y in range(0,9):
            #print("inner loop", y)
            if (arrayData[y] < arrayData[y + 1]):
                temp = arrayData[y]
                arrayData[y] = arrayData[y+1]
                arrayData[y+1] = temp
    print(arrayData)
bubbleSort()
