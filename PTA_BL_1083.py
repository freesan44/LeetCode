countInput = int(input())
numList = input().split(" ")
# countInput = 8
# numList = [3,5,8,6,2,1,4,7]

resDic = dict()
for i in range(1, countInput+1):
    # 绝对差
    res = abs(int(numList[i-1])-i)
    # 每个值放入字典统计
    if res not in resDic:
        resDic[res] = 1
    else:
        resDic[res] = resDic[res] + 1
# print(resDic.keys())
resList = sorted(resDic.keys())
resList.reverse()
# print(resList)
for i in resList:
    if resDic[i] != 1:#次数为1就是不重复，不进行输出
        print(str(i) + " " + str(resDic[i]))
