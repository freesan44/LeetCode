class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0,len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if mid == 0 or mid == len(nums)-1:break
            midValue = nums[mid]
            # if nums[mid-1]< midValue < nums[mid+1]:

        return -1

if __name__ == '__main__':
    nums = [1,2,1,3,5,6,4]
    result = Solution().findPeakElement(nums)
    print(result)