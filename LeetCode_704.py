class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 二分查找法 设置中间位
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right)//2
            # print(left,mid,right)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        return -1

if __name__ == '__main__':
    # nums = [-1,0,3,5,9,12]
    # target = 9
    nums = [-1, 0, 3, 5, 9, 12]
    target = 2
    nums = [2, 5]
    target = 5
    result = Solution().search(nums, target)
    print(result)
