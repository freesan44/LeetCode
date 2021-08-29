N, M = map(int, input().split())
# N, M = map(int, "6 3".split())
NDict = dict()#用字典Key+Arr方式保存冲突商品
for _ in range(N):
    N1, N2 = map(str, input().split())
    # N1, N2 = map(str, "10003 20004".split())
    if N1 not in NDict:
        NDict[N1] =[]
    if N2 not in NDict:
        NDict[N2] = []
    NDict[N1].append(N2)
    NDict[N2].append(N1)
for _ in range(M):
    MList = list(map(str, input().split()))[1:]
    # MList = list(map(str, "4 00001 20004 00002 20003".split()))[1:]
    isXiangtong = False
    for Meach in MList:
        if Meach in NDict:
            # print(Meach, NDict[Meach])
            arr = NDict[Meach]
            for i in arr:
                if i in MList:
                    isXiangtong = True
                    break
        if isXiangtong == True:break#多次跳出循环减少耗时
    if isXiangtong == True:
        print("No")
    else:
        print("Yes")