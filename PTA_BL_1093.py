inputStr1 = str(input())
# inputStr1 = "This is a sample test"
inputStr2 = str(input())
# inputStr2 = "to show you_How it works"
strDic = dict()
res = ""
str = inputStr1 + inputStr2
# print(str)
for i in str:
    # print(i)
    # # 字符串不存在就写入
    if i not in strDic:
        res = res + i
        strDic[i] = 1
print(res)

