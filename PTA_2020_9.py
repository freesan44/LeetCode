N = int(input())
inputList = list(map(int, input().split()))
# N = int("10")
# inputList = list(map(int, "180 160 100 150 145 142 138 138 138 140".split()))
length = len(inputList)
resList1 = [0]*len(inputList)
for index in range(0,len(inputList)):
    # print(index)
    last = inputList[index-1] if index !=0 else 200
    val = inputList[index]
    lastQuanzhong = resList1[index-1] if index !=0 else 0
    if val == last:
        resList1[index] = lastQuanzhong
    elif val > last:
        resList1[index] = lastQuanzhong+1
    elif val < last:
        resList1[index] = 0
# print(resList1)
resList2 = [0]*len(inputList)
for index in range(len(inputList)-1,-1,-1):
    # print(index)
    last = inputList[index+1] if index !=len(inputList)-1 else 200
    val = inputList[index]
    lastQuanzhong = resList2[index+1] if index !=len(inputList)-1 else 0
    if val == last:
        resList2[index] = lastQuanzhong
    elif val > last:
        resList2[index] = lastQuanzhong+1
    elif val < last:
        resList2[index] = 0
# print(resList2)
resList = []
for i in range(length):
    res = 200 + max(resList1[i],resList2[i])*100
    resList.append(res)
print(sum(resList))