startInt, round = map(str, input().split())
# startInt, round = map(str, "1 8".split())
res = startInt
# res = str(1231)
for _ in range(int(round)-1):
    # resList = list(res)
    resList = res
    tempStr = None
    tempCount = 0
    res = ""
    for val in resList:
    # for index,val in enumerate(resList):
        if val == tempStr:
            tempCount += 1
        else:#如果不相等，就把上一个输出并新赋值
            if tempStr != None:
                res += tempStr + str(tempCount)
            tempStr = val
            tempCount = 1
    #处理最后一个符号
    res += tempStr + str(tempCount)
print(res)
