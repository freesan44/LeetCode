count, MaxScore = map(int, input().split(" "))
# count, MaxScore =1, 50
for i in range(count):
    scoreStrList =  list(input().split(" "))
    # scoreStrList = list("30 250 -25 27 45 31".split(" "))
    scoreList = []
    for x in scoreStrList:
        scoreList.append(int(x))
    laoshiScore = int(scoreList.pop(0))
    # 排序并剔除不符合评分的
    # print(scoreList)
    # 通过filter 进行筛选
    scoreList = list(filter(lambda x:x>=0 and x<=int(MaxScore),scoreList))
    # for j in range(len(scoreList)):
    #     num = scoreList[j]
    #     if num<0 or num>int(MaxScore):
    #         scoreList.remove(num)
    # 去掉最高最低
    # print(scoreList)
    scoreList.sort()
    scoreList.pop()
    scoreList.pop(0)
    # print(scoreList)
    # 计算小组平均值,+0.5用于四舍五入
    xiaozuScore = (sum(scoreList)/len(scoreList))
    # print((xiaozuScore + laoshiScore)/2)
    resScore = int(((xiaozuScore + laoshiScore)/2)+0.5)
    print(resScore)

