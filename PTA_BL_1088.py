inputList = input().split(" ")
# inputList = "48 3 7".split(" ")
M = int(inputList[0])
X = int(inputList[1])
Y = int(inputList[2])
a,b,c = 0,0,0#对应甲乙丙
for i in range(99, 9, -1):
    #遍历a的值
    strI = str(i)
    j = int(strI[::-1]) #倒序，b的值
    if Y*abs(i-j)== X * j:
        # print(i)
        # print(j)
        k = j/Y
        #c的值如果是正整数，就输出答案
        if k%1 <= 0:
            a, b, c = i, j, k
        break
# 无解
if a == 0:
    print("No Solution")
else:
    resList = [str(a)]
    for i in [a,b,c]:
        if M == i:
            resList.append("Ping")
        elif M > i:
            resList.append("Gai")
        else:
            resList.append("Cong")
    print(" ".join(resList))