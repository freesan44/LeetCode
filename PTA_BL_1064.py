count = int(input())
# count = int("8")
countList = input().split()
# countList = "123 899 51 998 27 33 36 12".split()
resDic = dict()
for each in countList:
    numList = list(map(int, list(each)))
    sumNo = sum(numList)
    sumNoStr = str(sumNo)
    if sumNoStr in resDic:#如果存在朋友数就数量加1
        resDic[sumNoStr] += 1
    else:
        resDic[sumNoStr] = 1
resList = []#把符合朋友数的拿出来转成Int
for key,val in resDic.items():
    # if val >= 2:
    resList.append(int(key))
resList.sort()#进行排序
# print(resList)
print(str(len(resList)))
print(" ".join(map(str, resList)))