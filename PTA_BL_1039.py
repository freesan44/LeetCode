inputStrList = list(str(input()))
requestStrList = list(str(input()))
# inputStrList = list(str("ppRYYGrrYBR2258"))
# inputStrList = list(str("ppRYYGrrYB225"))
# requestStrList = list(str("YrR8RrY"))
inputStrSet = set(inputStrList)
requestStrSet = set(requestStrList)
inputDic = dict()
requestDic = dict()
# 统计每个字符串的keyValue
for i in inputStrSet:
    inputDic[i] = inputStrList.count(i)
for i in requestStrSet:
    requestDic[i] = requestStrList.count(i)
# print(inputDic)
duoyuCount = 0 #记录多余的珠子
qianCount = 0 #记录欠多少珠子
for key,value in inputDic.items():
    if key in requestDic:
        #如果大于0就是有多余的
        requestValue = requestDic[key]
        requestDic[key] = requestValue - value
        if value > requestValue:duoyuCount += value-requestValue #把扣除要求的数量后，多余数量记录下来
    else:
        duoyuCount += value
isSuccess = True
for key,value in requestDic.items():
    if value > 0:
        isSuccess = False
        qianCount += value
if isSuccess == True:
    print("Yes" + " " + str(duoyuCount))
else:
    print("No" + " " + str(qianCount))