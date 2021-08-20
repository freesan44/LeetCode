# 判断是否为质数
from math import sqrt
def isZhishu(input: int) -> bool:
    if input <= 1:
        return False
    if input == 2:
        return True
    if input % 2 == 0:
        return False
    for i in range(3,int(sqrt(input)+1),2):
        if input%i == 0:
            return False
    return True

input1 = input()
# input1 = "20 5"
count = int(input1.split(" ")[1])
input2 = str(input())
# input2 = "23654987725541023819"
isExist = False
for i in range(len(input2)-count+1):
    if isZhishu(int(input2[i:i+count])):
        isExist = True
        print(str(input2[i:i+count]))
        break
if isExist == False:
    print(404)
