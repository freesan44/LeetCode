inputStr1 = input().split(" ")
# inputStr1 = "5 3".split(" ")
yuebinCount = int(inputStr1[0])
cityCount = int(inputStr1[1])
countList = []
# 根据月饼种类形成列表
for i in range(yuebinCount):
    countList.append(0)
# 根据逐个输入，添加到总数
for i in range(cityCount):
    yuebinCount = input().split(" ")
    # yuebinCount = "1001 992 0 233 6".split(" ")
    for (index,value) in enumerate(yuebinCount):
        countList[index] = countList[index] + int(value)
# print(countList)
maxNum = max(countList)
maxList = []
# 把最大值的index找出来
for (index, value) in enumerate(countList):
    if value == maxNum:
        maxList.append(str(index+1))
# 打印最高值
print(maxNum)
# 最高值的index打印出来
print(" ".join(maxList))
