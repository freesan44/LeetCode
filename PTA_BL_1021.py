intputStrList = list(str(input()))
# intputStrList = list(str("100311"))
countDic = dict()
for i in intputStrList:
    if i in countDic:
        countDic[i] += 1
    else:
        countDic[i] = 1
# 把key数组中的str转成int，然后组成新数组
keyList = list(map(int, countDic.keys()))
# 排序
keyList.sort()
for i in keyList:
    print(str(i) + ":" + str(countDic[str(i)]))
