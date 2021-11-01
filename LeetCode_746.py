class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        length = len(cost)
        dp = [0]* (length+1)
        dp[0],dp[1] = cost[0],cost[1]
        for i in range(2,length+1):
            # print(i,cost[i])
            dp[i] = min(dp[i-1],dp[i-2]) +  (cost[i] if i<length else 0)
        # print(dp)
        return dp[-1]


if __name__ == '__main__':
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    cost = [10, 15, 20]
    res = Solution().minCostClimbingStairs(cost)
    print(res)