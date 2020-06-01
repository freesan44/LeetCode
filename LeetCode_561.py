class Solution:
    def arrayPairSum(self, nums: [int]) -> int:
        nums.sort()
        res = 0
        for pairNum in nums[::2]:
            res += pairNum
        return res




if __name__ == '__main__':
    nums = [1,4,3,2]
    ret = Solution().arrayPairSum(nums)
    print(ret)