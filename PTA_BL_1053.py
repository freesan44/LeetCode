N, e, D = map(str, input().split())
# N, e, D = map(str, "5 0.5 10".split())
N = int(N)
e = float(e)
D = int(D)
maybeKongzhi = 0
kongzhi = 0
for _ in range(N):
    inputList = list(map(float, input().split()))
    # inputList = list(map(float, "10 0.0 0.1 0.2 0.3 0.0 0.8 0.6 0.7 0.0 0.5".split()))
    EList = inputList[1:]
    days = int(inputList[0])
    diyuCount = 0
    for eEach in EList:
        if eEach < e:#如果电量低于阈值就+1
            diyuCount += 1
    #计算比率
    if (diyuCount > days//2) and (days > D):
        kongzhi += 1
    elif diyuCount > days//2:
        maybeKongzhi += 1
print("{:.1%} {:.1%}".format(maybeKongzhi/N, kongzhi/N))#用于输出百分百的格式化