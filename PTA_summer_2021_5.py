N = int(input())
maoList = list(map(int,input().split()))
renList = list(map(int,input().split()))
# N = int("10")
# maoList = list(map(int,"12 19 13 11 15 18 17 14 16 20".split()))
# renList = list(map(int,"67 90 180 98 87 105 76 88 150 124".split()))

sourtMaoList = sorted(maoList,reverse=True)
sourtRenList = sorted(renList,reverse=True)
resDict = dict()
renListDict = dict()
for index,val in enumerate(renList):
    renListDict[val] = index
for i in range(N):
    mao = sourtMaoList[i]
    ren = sourtRenList[i]
    # index = renList.index(ren)
    index = renListDict[ren]
    resDict[mao] = str(index+1)
# print(resDict)
res = []
for i in maoList:
    res.append(resDict[i])
print(" ".join(res[::-1]))