class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right)//2
            midNum = nums[mid]
            print(left,right,mid)
            if midNum == target:
                return mid
            #正常序列在左边
            if midNum >= nums[left]:
                if nums[left] <= target < midNum:
                    right = mid - 1
                else:
                    left = mid + 1
            else:#正常序列在右边时
                if midNum < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid -1
        return -1

if __name__ == '__main__':
    nums = [4,5,6,7,0,1,2]
    target = 0
    result = Solution().search(nums, target)
    print(result)