class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxNum = -1
        resList = [maxNum]
        for i in range(len(arr)-1,-1,-1):
            val = arr[i]
            maxNum = max(val,maxNum)
            resList.append(maxNum)
        resList.pop()
        resList.reverse()
        return resList

if __name__ == '__main__':
    arr = [17,18,5,4,6,1]
    arr = [400]
    ret = Solution().replaceElements(arr)
    print(ret)