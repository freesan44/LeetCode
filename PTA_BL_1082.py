inputCount = int(input())
# inputCount = 3
menberNoList = []
menberLengthList = []
for i in range(inputCount):
    inputList = input().split(" ")
    # inputList = "0001 5 7".split(" ")
    menberNoList.append(inputList[0])
    x = abs(int(inputList[1]))
    y = abs(int(inputList[2]))
    # 可以用平方根，但这样少算一层
    length = x*x + y*y
    menberLengthList.append(length)
#获取最长最短距离的index
maxIndex = menberLengthList.index(max(menberLengthList))
minIndex = menberLengthList.index(min(menberLengthList))
print(str(menberNoList[minIndex]) + " " + str(menberNoList[maxIndex]))