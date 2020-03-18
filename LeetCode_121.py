class Solution:
    def maxProfit(self, prices: [int]) -> int:
        # maxNum = 0
        # while len(prices) >1:
        #     minIndex = 0
        #     maxIndex = prices.index(max(prices[1:]))
        #     # print(str(prices[maxIndex])+ "-" + str(prices[minIndex]))
        #     if (maxIndex > minIndex) and (maxNum < (prices[maxIndex] - prices[minIndex])):
        #         maxNum =  prices[maxIndex] - prices[minIndex]
        #         # print(maxNum)
        #     prices.pop(0)
        #
        # return maxNum
        #动态规划
        if len(prices) <= 0:
            return 0
        minNum = prices[0]
        maxList = [0]* len(prices)
        for i in range(1,len(prices)):
            minNum = min(minNum, prices[i])
            maxList[i] = max(maxList[i-1],prices[i]-minNum)
        return maxList[-1]


if __name__ == '__main__':
    # nums = [7,2,4,1]
    nums = [7,1,5,3,6,4]
    # nums = [2,1,2,1,0,1,2]
    result = Solution().maxProfit(nums)
    print(result)