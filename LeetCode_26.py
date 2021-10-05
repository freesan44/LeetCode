class Solution:
    def removeDuplicates(self, nums:[int]) -> int:
        # 双指针方法
        left, right = 0, 0
        while right < len(nums):
            if nums[left] == nums[right]:
                right += 1
            else:
                nums[left+1] = nums[right]
                right += 1
                left += 1
            # print(nums)
        return left+1

if __name__ == '__main__':
    nums = [0,0,1,1,1,2,2,3,3,4]
    # nums = [1,1,2]
    # nums = [2]
    # nums = [1,1]
    res = Solution().removeDuplicates(nums)
    # res = nums[1:]
    print(nums)
    print(res)