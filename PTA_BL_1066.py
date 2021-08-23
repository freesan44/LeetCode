M,N,A,B,H = map(int,input().split())
# M,N,A,B,H = map(int, "3 5 100 150 0".split(" "))
zongResList = []
for i in range(M):
    for j in input().split():
        if A <= int(j) <= B:
            zongResList.append("%03d" % H)
        else:
            zongResList.append("%03d" % j)
    #以下方法最后案例不通过
    # # 输入转换成int的List
    # inputList = list(map(int, input().split()))
    # # inputList = list(map(int, "3 189 254 101 119".split()))
    # resList = []
    # for j in inputList:
    #     res = None
    #     if A <= int(j) <= B:
    #         # 进行补0转义
    #         # res = "{:0>3d}".format(int(H))
    #         res = "%03d" % H
    #     else:
    #         # 进行补0转义
    #         # res = "{:0>3d}".format(int(j))
    #         res = "%03d" % j
    #     # resList.append(res)
    #     zongResList.append(res)
    # # zongResList.append(resList)
    # # print(" ".join(resList))
for i in range(0, len(zongResList),N):
    print(' '.join(zongResList[i:i+N]))