# N, maxZijin = map(int, input().split())
# inputList = list(map(int, input().split()))
N, maxZijin = map(int, "5 85".split())
inputList = list(map(int, "38 42 15 24 9".split()))

ans = []
def dfs(idx:int, cur:int, patch:[int]):
    #递归结束
    if cur <= 0:
        # ans.append(patch[:])
        return
    elif idx == len(inputList):
        return
    if cur >= inputList[idx]:
        if len(patch) == 0 or idx==(patch[-1]+1):
            # print(idx, cur, patch,inputList[idx])
            # print(idx, cur, patch)
            # and (idx == (patch[-1] + 1))
            patch.append(idx)
            ans.append(patch[:])
            dfs(idx+1, cur - inputList[idx] ,patch)
            # return
            #消除影响【重要】
            patch.pop()
    dfs(idx + 1, cur, patch)

dfs(0,maxZijin,[])
print(len(ans))

