def BubbleSort(MyList):
  MaxIndex = len(MyList)
  counter = MaxIndex - 1
  for i in range(0,counter):
    for j in range(0, counter):
      if(MyList[j] < MyList[j+1]):
        Temp = MyList[j]
        MyList[j] = MyList[j+1]
        MyList[j+1] = Temp
    counter = counter-1 #reduction of comparisons
MyList1 = [5,3,2,4,1]
print(BubbleSort(MyList1)) 
MyList2 = [5,2,78,4,1]
print(BubbleSort(MyList2)) 
MyList3 = [5,3,2,6,1]
print(BubbleSort(MyList3)) 