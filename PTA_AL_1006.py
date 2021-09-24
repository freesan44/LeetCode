N = int(input())
# N = 3
def strToTimestamp(input:str) -> int:
    H,m,s = map(int,input.split(":"))
    res = H*3600 + m * 60 + s
    return res
resList = []
for _ in range(N):
    name,start,end = map(str,input().split())
    # name, start, end = map(str, "CS301111 15:30:28 17:00:10".split())
    resList.append([name,strToTimestamp(start),strToTimestamp(end)])
# print(resList)
resList.sort(key= lambda x:(x[1]))#根据开始时间排序，然后获取最低值的ID
#sorted(resList,key= lambda x:(x[1]))
# print(resList)
startNo = resList[0][0]
#sorted(resList,key= lambda x:(x[2]))
resList.sort(key= lambda x:(x[2]))#根据结束时间排序，然后获取最高值的ID
# print(resList)
endNo = resList[-1][0]
print(startNo,endNo)

