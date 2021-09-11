N = int(input())
# N = 6
resList = []
for _ in range(N):
    no,length,time = map(int,input().split())
    # no, length, time = map(int, "886 500 12".split())
    resList.append((no,length/time))
# print(resList)
resList.sort(key= lambda x:(x[1],x[0]))
res = [str(x) for (x,y) in resList]
print(" ".join(res[:3]))