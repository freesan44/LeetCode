N = int(input())
# N = int("3")

inputList = []
for _ in range(N):
    i = int(input())
    # i = int("91")
    inputList.append(i)
maxNum = max(inputList)
import math
sqrtNum = int(math.sqrt(2*maxNum))
# sqrtNum = int(maxNum//2)
duishuDict = dict()
for i in range(1,sqrtNum):
    for j in range(i+1,sqrtNum):
        # print(i,j)
        res = (i+j)**2-(i*j)
        if res>0:
            if res in duishuDict:
                duishuDict[res] += [(i,j)]
            else:
                duishuDict[res] = [(i,j)]
# print(duishuDict)
duishuList = [int(i) for i in duishuDict.keys()]
duishuList.sort()
# print(duishuDict)
for test in inputList:
    if test in duishuDict:
        print("Yes")
        arr = duishuDict[test]
        for x,y in arr:
            print(x,y)
    else:
        #定位最近好熟
        for i in duishuList:
            if i > test:
                print("No",i)
                arr = duishuDict[i]
                for x, y in arr:
                    print(x, y)
                break
