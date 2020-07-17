class Solution:
    def searchInsert(self, nums: [int], target: int) -> int:
        # try:
        #     return nums.index(target)
        # except:
        #     for idx,val in enumerate(nums):
        #         if val > target:
        #             return idx
        # return len(nums)
        #二分法
        length = len(nums)
        if target > nums[-1]: return length
        left = 0
        right = length-1
        while left <= right:
            mid = (right+left)//2
            if nums[mid]>target:
                right = mid - 1
            elif nums[mid]<target:
                left = mid + 1
            else:
                return mid
        return left



if __name__ == '__main__':
    nums = [1,3,5,6]
    target = 4
    result = Solution().searchInsert(nums, target)
    print(result)