count = int(input())
testList = map(int, input().split())
# count = int("3")
# testList = map(int, "92 5 233".split())
for K in testList:
    K2 = K*K
    isExist = False
    resN = 0
    resNK2Str = ""
    for N in range(1, 10):
        NK2Str = str(N * K2)
        # print(str(N))
        # print(str(NK2Str))
        if str(K) == NK2Str[-len(str(K)):]:
            # print(str(NK2Str))
            # print(str(NK2Str[-2:]))
            resN = N
            resNK2Str = NK2Str
            isExist = True
            break
    if isExist == True:
        print(resN, resNK2Str)
    else:
        print("No")


