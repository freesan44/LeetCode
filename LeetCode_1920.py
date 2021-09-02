class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        res = []
        for i in nums:
            res.append(nums[i])
        return res

if __name__ == '__main__':
    nums = [0,2,1,5,3,4]
    result = Solution().buildArray(nums)
    print(result)