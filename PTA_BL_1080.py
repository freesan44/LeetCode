# ## 该写法超时
# inputList = input().split(" ")
# PCount = int(inputList[0])
# MCount = int(inputList[1])
# FCount = int(inputList[2])
# # PCount = 6
# # MCount = 6
# # FCount = 7
# PDict = dict()
# MDict = dict()
# FDict = dict()
# for i in range(PCount):
#     inputList = input().split(" ")
#     # inputList = "a1903 199".split(" ")
#     PDict[inputList[0]] = int(inputList[1])
# for i in range(MCount):
#     inputList = input().split(" ")
#     # inputList = "a1902 100".split(" ")
#     MDict[inputList[0]] = int(inputList[1])
# for i in range(FCount):
#     inputList = input().split(" ")
#     # inputList = "a1901 99".split(" ")
#     FDict[inputList[0]] = int(inputList[1])
# resArr = []
# nameDic = dict()#用于登记哪些学生已经存档
# for key,value in PDict.items():
#     stdDic = dict()
#     stdDic["name"] = key
#     stdDic["Gp"] = value
#     stdDic["Gm"] = -1
#     stdDic["Gf"] = -1
#     resArr.append(stdDic)
#     nameDic[key] = 1
# for key,value in MDict.items():
#     if key in nameDic:
#         # 遍历并添加Gm成绩
#         for eachDic in resArr:
#             if eachDic["name"] == key:
#                 eachDic["Gm"] = value
#                 break
#     else:
#     # 如果不存在就添加新字典
#         stdDic = dict()
#         stdDic["name"] = key
#         stdDic["Gp"] = -1
#         stdDic["Gm"] = value
#         stdDic["Gf"] = -1
#         resArr.append(stdDic)
#         nameDic[key] = 1
# for key,value in FDict.items():
#     # 遍历并添加Gf成绩
#     if key in nameDic:
#         for eachDic in resArr:
#             if eachDic["name"] == key:
#                 eachDic["Gf"] = value
#                 break
#     else:
#     # 如果不存在就添加新字典
#         stdDic = dict()
#         stdDic["name"] = key
#         stdDic["Gp"] = -1
#         stdDic["Gm"] = -1
#         stdDic["Gf"] = value
#         resArr.append(stdDic)
#         nameDic[key] = 1
# # 得到完整字典列表后，进行总成绩计算
# for dic in resArr:
#     if int(dic["Gm"])>int(dic["Gf"]) and dic["Gm"] != -1 and dic["Gf"] != -1:
#         tolScore = int(dic["Gm"])*4+ int(dic["Gf"])*6
#         # 四舍五入
#         if tolScore%10 >6:
#             tolScore = tolScore + 10
#         dic["G"] = tolScore//10
#     else:
#         dic["G"] = int(dic["Gf"])
# # print(resArr)
# # print(sorted(resArr, key = lambda i:(i["G"],i["name"]), reverse=True))
# # 先按姓名排序 再按成绩倒序
# resArr = sorted(resArr, key = lambda i:(i["name"]))
# resArr = sorted(resArr, key = lambda i:(i["G"]), reverse=True)
# for dic in resArr:
#         if int(dic["Gp"])>=200 and int(dic["G"])>=60:
#             print(dic["name"] + " " + str(dic["Gp"]) + " " + str(dic["Gm"]) + " " + str(dic["Gf"]) + " " + str(dic["G"]))

## 这是不超时的
# 四个字典用来保存成绩
Gp ={}
Gmidterm={}
Gfinal={}
G={}
n,m,k=map(int,input().split())
# 三个for 循环用来读入数据
for i in range(n):
    x,y=input().split()
    if int(y)>=200:
        Gp[x]=int(y)
for i in range(m):
    x,y=input().split()
    if x in Gp.keys():
        Gmidterm[x]=int(y)
for i in range(k):
    x,y=input().split()
    if x in Gp.keys():
        Gfinal[x]=int(y)
# 对>=200分的同学进行算最终成绩
for t in Gp:
    if t not in Gmidterm.keys():
        Gmidterm[t]=-1
    if t not in Gfinal.keys():
        Gfinal[t]=-1
    if Gmidterm[t]>Gfinal[t]:
        G[t]=int(Gmidterm[t]*0.4+Gfinal[t]*0.6+0.5)
    else:
        G[t]=Gfinal[t]
# 主要代码 ： 对字典的键和值同时进行排序
G=sorted(G.items(), key=lambda item:(-item[1],item[0]) , reverse=False)
for t in G:
    if int(t[1])>=60:
        id=t[0]
        print(t[0],Gp[id],Gmidterm[id],Gfinal[id],t[1])