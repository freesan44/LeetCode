class Solution:
    def majorityElement(self, nums: [int]) -> int:
        nums.sort()
        return nums[len(nums)//2]

if __name__ == '__main__':
    nums = [3,3,2,2,3]
    result = Solution().majorityElement(nums)
    print(result)