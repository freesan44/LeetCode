inputList = list(map(int,input().split()))
# inputList = list(map(int,"3 2 3 1".split()))

res = 0
res += inputList[0]*5

eleList = [0]+inputList[1:]
for i in range(1,len(eleList)):
    #升
    if eleList[i]>=eleList[i-1]:
        res += 6*(eleList[i]-eleList[i-1])
    else:
        res += 4 * (eleList[i-1] - eleList[i])
print(res)