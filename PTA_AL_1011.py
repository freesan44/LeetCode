inputList = []
for _ in range(3):
    inputData = list(map(float,input().split()))
    # inputData = list(map(float, "1.1 2.5 1.7".split()))
    inputList.append(inputData)
retList = []
res = 1
for i in inputList:
    maxVal = max(i)
    indexVal = i.index(maxVal)
    if indexVal == 0:
        retList.append("W")
    elif indexVal == 1:
        retList.append("T")
    else:
        retList.append("L")
    res *= maxVal
res = 2 * (res*0.65 - 1)
## 难点是格式化方式
res = "%.2f" % res
retList.append(res)
print(" ".join(retList))


