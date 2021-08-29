import sys
N = int(input())
# N = int("6")
resDic = dict()
for _ in range(N):
    bianhao, chengji = map(str, sys.stdin.readline().split())
    # bianhao, chengji = map(str, "3 65".split())
    if bianhao not in resDic:
        resDic[bianhao] = int(chengji)
    else:
        resDic[bianhao] += int(chengji)
maxChengji = max(resDic, key=resDic.get)
print(maxChengji, resDic[maxChengji])
# for (key, val) in resDic.items():
#     if val == maxChengji:
#         print(key, val)
#         break