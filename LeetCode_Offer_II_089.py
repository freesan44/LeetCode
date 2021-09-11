class Solution:
    def rob(self, nums: [int]) -> int:
        dp = [0]*len(nums)
        # 边界条件
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0],nums[1])
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2]+nums[i],dp[i-1])
        # print(dp)
        return dp[-1]
if __name__ == "__main__":
    nums = [2,7,9,3,1]
    nums = [1, 2, 3, 1]
    nums = [2,1,1,2]
    ret = Solution().rob(nums)
    print(ret)