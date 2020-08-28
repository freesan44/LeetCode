class Solution:
    def getWinner(self, arr: [int], k: int) -> int:
        count = 0
        preMaxNum = None
        if k > len(arr):
            return max(arr)
        return max(arr[:k])
        # while True:
        #     one = arr.pop(0)
        #     two = arr.pop(0)
        #     maxNum = max(one, two)
        #     minNum = min(one, two)
        #     if preMaxNum == maxNum:
        #         count = count+1
        #     else:
        #         count = 0
        #         preMaxNum = maxNum
        #     if count == k-1:
        #         return maxNum
        #     arr.append(min(one,two))
        #     arr.insert(0, max(one,two))
        #     # print(arr)
        # return preMaxNum
if __name__ == '__main__':
    arr = [2,1,3,5,4,6,7]
    k = 2
    # arr = [3, 2, 1]
    # k = 10
    # arr = [1, 9, 8, 2, 3, 7, 6, 4, 5]
    # k = 7
    result = Solution().getWinner(arr, k)
    print(result)