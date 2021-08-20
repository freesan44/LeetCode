str1 = input()
# str1 = "6 2"
str2 = input()
# str2 = "1 2 3 4 5 6"
list1 = str1.split(" ")
# 移动步数
moveStep = int(list1[1])
# 原始数组
numList = str2.split(" ")

# print(numList)
for i in range(moveStep):
    item = numList.pop()
    numList.insert(0, item)
# 输出结果
res = " ".join(numList)
print(res)