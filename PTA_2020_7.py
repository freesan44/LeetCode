start,end = map(int,input().split())
# start,end = map(int,"10 14".split())
# start,end = map(int,"1 10".split())

inputList = [str(i) for i in range(start, end+1)]

def actionRes(a:str) -> str:
    res = 1
    for i in a:
        res = res *(int(i)**3)
    b = str(res)
    resb = 0
    for j in b:
        resb += int(j)
    return str(resb)

def sumLength(list:[str])->int:
    res = 0
    for i in list:
        res += len(i)
    return res

while sumLength(inputList) != len(inputList):
    for index,val in enumerate(inputList):
        inputList[index] = actionRes(val)
    # print(inputList)
from collections import Counter
res = Counter(inputList).most_common()
if len(res) == 0:
    print("")
else:
    resOutput = [int(x) for x,y in res if y == res[0][1]]
    resOutput.sort()
    print(res[0][1])
    resOutput = [str(x) for x in resOutput]
    print(" ".join(resOutput))
