#--- Q1 (a) --- 6/6
#DECLARE FileName: STRING
#DECLARE WordArray: ARRAY
#DECLARE NumberWords: INTEGER

def ReadWords(FileName):
    global WordArray
    global NumberWords
    WordArray = []
    NumberWords = 0


    File = open(FileName, 'r')
    Line = File.readline().strip()
    while Line:
        WordArray.append(Line)
        Line = File.readline().strip() #use this to remove /n
        NumberWords = NumberWords + 1
    NumberWords = NumberWords - 1
    File.close()
ReadWords("../../Text Files/Easy.txt")
print(WordArray)
print(NumberWords)


