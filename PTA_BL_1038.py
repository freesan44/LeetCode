N = input()
# N = "10"
NList = input().split()
# NList = "60 75 90 55 75 99 82 90 75 50".split()
KList = input().split()[1:]
# KList = "3 75 90 88".split()[1:]

resDic = dict()#用字典方式存储
for i in NList:
    if i not in resDic:
        resDic[i] = 1
    else:
        resDic[i] += 1
resArr = []
for j in KList:
    if j in resDic:
        resArr.append(resDic[j])
    else:
        resArr.append("0")#不存在就为0
print(" ".join("%s" %a for a in resArr))#转成str输出打印