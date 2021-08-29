N = int(input())
# N = int("10")
chuquanDic = {
    "B": 0,
    "C": 2,
    "J": 1,
}
AWins = {
    "B": 0,
    "C": 0,
    "J": 0,
}
AChengji = [0,0,0]#胜、平、负次数
BWins = {
    "B": 0,
    "C": 0,
    "J": 0,
}

for _ in range(N):
    Achu, Bchu = map(str, input().split())
    # Achu, Bchu = map(str, "C J".split())
    res = chuquanDic[Achu] - chuquanDic[Bchu]
    if res ==1 or res == -2:#A赢
        AWins[Achu] += 1
        AChengji[0] += 1
    elif res ==-1 or res == 2:#B赢
        BWins[Bchu] += 1
        AChengji[2] += 1
    elif res == 0:#平局
        AChengji[1] += 1
# AChengjiNew = map(lambda x:str(x), AChengji)
# print(" ".join(AChengjiNew))
print(AChengji[0],AChengji[1],AChengji[2])
print(AChengji[2],AChengji[1],AChengji[0])
maxA = max(AWins.values())
maxB = max(BWins.values())
resMax = ""
for (key,val) in AWins.items():
    if val == maxA:
        resMax += key
        break
for (key,val) in BWins.items():
    if val == maxB:
        resMax = resMax + " " + key
        break
print(resMax)
