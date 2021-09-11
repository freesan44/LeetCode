n, MAXP = map(int,input().split())
# n, MAXP = map(int,"5 1000".split())
# n, MAXP = map(int,"10 2".split())


import math
def isSushu(input:int)->bool:
    if input == 2 or input == 3 or input == 1:
        return True
    sqrtInt = int(math.sqrt(input))
    for i in range(2,sqrtInt+1):
        if input%i == 0:
            return False
    return True
sushuList = []
for i in range(2,MAXP+1):
    if isSushu(i) == True:
        sushuList.append(i)
# print(sushuList)
if len(sushuList) == 0:
    print("")
resList = []
for index,val in enumerate(sushuList):
    for i in sushuList[index+1:]:
        dengcha = i - val
        shifoucunzai = True##是否存在等差数列
        for chengshu in range(1,n):
            dengchashu = val + dengcha*(chengshu)
            if dengchashu not in sushuList:
                shifoucunzai = False
                break
        if shifoucunzai == True:
            resList.append((val, dengcha))
# 有解的数组
resList.sort(key= lambda x:(-x[1],-x[0]))
# print(resList)
if len(resList)>0:#如果解存在，则在一行中按递增序输出等差最大的一组解；若解不唯一，则输出首数最大的一组解。
    num,cha = resList[0]
    res = [str(num+cha*i) for i in range(n)]
    print(" ".join(res))
else:
    try:
        print(str(sushuList[-1]))
    except:
        print("")