round = int(input())
# round = int("6")
resDic = dict()
for i in range(round):
    inputList = input().split(" ")
    # inputList = "3-10 99".split(" ")
    duiwuNo,duiyuanNo = map(str,inputList[0].split("-"))
    chengji = int(inputList[1])
    if duiwuNo in resDic:
        resDic[duiwuNo] = resDic[duiwuNo] + chengji
    else:
        resDic[duiwuNo] = chengji
maxName = None
maxValue = 0
for key,value in resDic.items():
    if value > maxValue:
        maxName = key
        maxValue = value

print(maxName + " " + str(maxValue))
