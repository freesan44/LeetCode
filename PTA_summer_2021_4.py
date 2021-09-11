N, K = map(int,input().split())
# N, K = map(int,"6 7".split())
testList = []
maxLength = 0
neicunDict = dict()
for i in range(N):
    x,y = map(int,input().split())
    # x, y = map(int, "2048 5".split())
    maxLength += y
    testList.append(y)
    neicunDict[i] = x

inputList = list(map(int, input().split()))
# inputList = list(map(int, "2 12 25 50 28 8 39".split()))

maxShuzu = 0
for i in inputList:
    if i >= maxLength:
        print("Illegal Access")
        continue
    for index,y in enumerate(testList):
        if (i - y)<0:
            neicundizhi = neicunDict[index]
            address = neicundizhi+i*4
            print(address)
            maxShuzu = max(index+1,maxShuzu)
            break
        i -= y
print(maxShuzu)

