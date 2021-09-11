N = int(input())
# N = 7

def zhuanhua(input:str)->int:
    h,m,s = map(int,input.split(":"))
    res = s+m*60+h*60*60
    return res
inputList = []
for _ in range(N):
    start, end = map(zhuanhua, input().split())
    # start, end = map(zhuanhua, "18:00:01 23:07:01".split())
    inputList.append((start, end))
inputList.sort(key= lambda x:(-x[1],x[0]))
start = 0
maxEndTime = zhuanhua("23:59:59")
res = 0
print(inputList)
for x,y in inputList:
    if y<=maxEndTime:
        maxEndTime = x
        res += 1
print(res)
