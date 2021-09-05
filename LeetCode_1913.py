class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        # print(nums)
        res = (nums[-1]*nums[-2] - nums[0]*nums[1])
        return res

if __name__ == '__main__':
    nums = [4,2,5,9,7,4,8]
    ret = Solution().maxProductDifference(nums)
    print(ret)