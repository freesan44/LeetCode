count = int(input())
name = []
xuehao = []
num = []
for i in range(count):
    str = input()
    # 空格隔开分配
    tempList = str.split(" ")
    name.append(tempList[0])
    xuehao.append(tempList[1])
    num.append(int(tempList[2]))
# print(num)
maxIndex = num.index(max(num))
minIndex = num.index(min(num))

print(name[maxIndex] + " " + xuehao[maxIndex])
print(name[minIndex] + " " + xuehao[minIndex])
