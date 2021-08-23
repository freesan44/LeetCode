inputList = list(map(int, input().split()))
# inputList = list(map(int, "2 2 0 0 0 3 0 0 1 0".split()))
resStr = ""
# 找出最低的首位
for index, value in enumerate(inputList[1:]):
    if value != 0:
        resStr += str(index+1)
        inputList[index+1] = inputList[index+1] -1 #该位数数量减1
        break
# 从低到高输出拼接字符串
for index, value in enumerate(inputList):
    for i in range(value):
        resStr += str(index)
print(resStr)

