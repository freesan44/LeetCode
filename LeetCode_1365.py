class Solution:
    def smallerNumbersThanCurrent(self, nums: [int]) -> [int]:
        tempList = nums.copy()
        tempList.sort()
        ret = [tempList.index(i) for i in nums]
        return ret

if __name__ == '__main__':
    nums = [8,1,2,2,3]
    ret = Solution().smallerNumbersThanCurrent(nums)
    print(ret)