inputStr = input()
# inputStr = "This is a simple TEST.  There ARE numbers and other symbols 1&2&3..........."
res = dict()#用字典方式统计
for i in inputStr:
    if i.isalpha() == True:
        iStr = i.lower()#转小写
        # print(iStr)
        if iStr not in res:
            res[iStr] = 1
        else:
            res[iStr] += 1
maxVal = max(res.values())#获取最高值
maxList = [key for key,val in res.items() if val == maxVal]#获取拥有最高值的字母字典，并排序
maxList.sort()
print(maxList[0], maxVal)