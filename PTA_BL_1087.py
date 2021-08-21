inputInt = int(input())
# inputInt = 2017
resDic = dict()
for i in range(1, inputInt+1):
    res = i//2 + i//3 + i//5
    # 字典里面没值就添加
    if res not in resDic:
        resDic[res] = 1
print(len(resDic))