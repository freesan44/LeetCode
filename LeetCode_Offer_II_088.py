class Solution:
    def minCostClimbingStairs(self, cost: [int]) -> int:
        # 动态规划
        dp = [0]*len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2,len(cost)):
            dp[i] = min(dp[i-1], dp[i-2])+cost[i]
        # print(dp)
        return min(dp[-1],dp[-2])#选择从倒数第一步还是倒数第二步跨上去

if __name__ == "__main__":
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    # cost = [10, 15, 20]
    ret = Solution().minCostClimbingStairs(cost)
    print(ret)