class Solution:
    def minSubArrayLen(self, s: int, nums: [int]) -> int:
        if not nums:return 0 #处理特例
        #双指针
        left = 0
        right = left+1
        minCount = len(nums)+1
        tempSum = nums[left]
        if tempSum >= s: return 1#处理特例
        while right < len(nums):
            # tempSum = sum(nums[left:right])
            tempSum = tempSum + nums[right]
            if tempSum <s:#数值不够s，right++
                right = right + 1
            else:#更新最小值
                # while sum(nums[left+1:right]) >= s:#尝试缩进left
                while tempSum - nums[left] >= s:  # 尝试缩进left
                    tempSum = tempSum - nums[left]
                    left = left + 1
                # print("{} {}".format(left,right+1))
                minCount = min(minCount, right+1-left)
                # minCount = min(minCount, len(nums[left:right]))
                right = right + 1
        return minCount if minCount<len(nums)+1 else 0


if __name__ == '__main__':
    # s = 7
    # nums = [2,3,1,2,4,3]
    # s = 100
    # nums = []
    # s = 11
    # # s = 15
    # nums = [1, 2, 3, 4, 5]
    # s = 4
    # nums = [1,4,4]
    s = 6
    nums = [10, 2, 3]
    ret = Solution().minSubArrayLen(s, nums)
    print(ret)
