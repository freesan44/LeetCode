inputStr = str(input())
# inputStr = str("redlePayBetPATTopTeePHPereatitAPPT")
strList = ["P","A","T","e","s","t"]
inputStrDic = dict()
## 汇总全部需要的字母的数量
for i in strList:
    inputStrDic[i] = inputStr.count(i)
res = ""
# print(inputStrDic)
while len(inputStrDic) != 0:
    # 逐个字母循环
    for i in strList:
        if i in inputStrDic:
            if inputStrDic[i] == 0:
                del (inputStrDic[i])  # 如果没值了就移除
                continue
            res = res + i
            inputStrDic[i] = inputStrDic[i]-1 #添加字母后数量减1
print(res)

