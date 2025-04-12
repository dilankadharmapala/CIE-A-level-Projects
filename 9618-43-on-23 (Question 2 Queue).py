#--- Q2 (a) (i) --- 2/2
#DECLARE Queue: ARRAY [0:49] OF STRING
#DECLARE HeadPointer: INTEGER
#DECLARE TailPointer: INTEGER
global Queue
global HeadPointer
global TailPointer

Queue = []
HeadPointer = -1
TailPointer = 0

#--- (a) (ii) ---
def Enqueue(ID):
    global Queue
    global HeadPointer
    global TailPointer

    if (TailPointer == 50): #queue is full
        print("The queue is full")
    else:
        Queue.append(ID)
        TailPointer = TailPointer + 1
        if (HeadPointer == -1):
            HeadPointer = 0

#--- (a) (iii) ---
def Dequeue():
    global Queue
    global HeadPointer
    global TailPointer


    if (TailPointer == 0) or (HeadPointer == -1): #queue is empty
        print("The queue is Empty")
        return "Empty"
    else:
        ReturnValue =  Queue[HeadPointer]
        Queue[HeadPointer] = ""
        HeadPointer = HeadPointer + 1
        return ReturnValue
#--- (b)  DOUBT
def ReadData():
    try:
        File = open("QueueData.txt", 'r')
        Line = File.readline().strip() #to start the loop
        while Line: #checks if there is a line
        #for Line in File picks each line
            Enqueue(Line)
            Line = File.readline().strip()
        File.close()

    except Exception as e:
        print(e)


ReadData()
print(Queue)


