class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        res = -1
        length = len(nums)
        for i in range(length):
            for j in range(i+1, length):
                if j > i and nums[j]> nums[i]:
                    chaju = nums[j] - nums[i]
                    res = max(res,chaju)
        return res
if __name__ == '__main__':
    nums = [7,1,5,4]
    ret = Solution().maximumDifference(nums)
    print(ret)