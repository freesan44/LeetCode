class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        # 先排序，然后头尾遍历，找出最低值
        nums.sort()
        res = 0
        for i in range(len(nums)//2):
            dui = nums[i] + nums[len(nums) - 1 - i]
            if dui>res:
                res = dui
        return res

if __name__ == '__main__':
    nums = [3,5,4,2,4,6]
    ret = Solution().minPairSum(nums)
    print(ret)