num = int(input())
# num = int(1234567890987654321123456789)
count = 0
#计算总数
for i in list(str(num)):
    count = int(i) + count
print(count)
countList = list(str(count))
# countList.reverse()
outPutStr = ""
for i in countList:
    i = int(i)
    if i == 0:
        str = "ling"
    elif i == 1:
        str = "yi"
    elif i == 2:
        str = "er"
    elif i == 3:
        str = "san"
    elif i == 4:
        str = "si"
    elif i == 5:
        str = "wu"
    elif i == 6:
        str = "liu"
    elif i == 7:
        str = "qi"
    elif i == 8:
        str = "ba"
    elif i == 9:
        str = "jiu"
    outPutStr = outPutStr + str + " "
print(outPutStr[:-1])
# print(str(count)[1])