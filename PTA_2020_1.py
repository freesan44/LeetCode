N = int(input())
KList = input().split()

# N = int("5")
# KList = "123 7 43 2333 56160".split()

for i in KList:
    zhengchu = True
    resStr = ""
    for s in i:
        resStr += s
        if len(resStr)> 1 and  int(resStr)%len(resStr) != 0:
            # print(resStr,len(resStr))
            zhengchu = False
            break
    if zhengchu == True:
        print("Yes")
    else:
        print("No")
