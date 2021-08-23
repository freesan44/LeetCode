NCount = int(input())
# 登记全部学位列表,用字典查询比较快
kaoshiDict = dict()
for i in range(NCount):
    xuehao, shiji, kaoshi = map(str, input().split())
    kaoshiDict[shiji] = [xuehao, shiji, kaoshi]
MCount = int(input())
testList = map(str, input().split())
for testStr in testList:
    res = kaoshiDict[testStr]
    print(res[0], res[2])