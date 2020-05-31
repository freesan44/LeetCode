class Solution:
    def maxProfit(self, prices:[int]) -> int:
        lenP = len(prices)
        i = 0
        profit = 0
        while i < lenP-1:
            if prices[i]< prices[i+1]:
                #后一个比前面一个高，就有利润，然后累积
                profit += prices[i+1]-prices[i]
            i += 1
        return profit



if __name__ == '__main__':
    # nums = [7,1,5,3,6,4]
    # nums = [1,2,3,4,5]
    nums = [7]
    res = Solution().maxProfit(nums)
    # print(nums)
    print(res)