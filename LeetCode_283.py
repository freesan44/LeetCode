class Solution:
    def moveZeroes(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # lenN = len(nums)
        # i = 0
        # while i < lenN:
        #     if nums[i] == 0:
        #         nums.append(nums.pop(i))
        #         i -= 1#维持原来的序号
        #         lenN -= 1#核实的最后指证提前
        #     i += 1
        #双指针
        lenN = len(nums)
        left = 0 #检测当前元素
        right = 0 #统计已经通过的元素
        while right < lenN:
            if nums[left] == 0:
                nums[left:-1] = nums[left+1:]
                nums[-1] = 0
            else:
                left += 1
            right += 1




if __name__ == '__main__':
    nums = [0,1,0,3,12]
    # nums = [4,3,2,1]
    res = Solution().moveZeroes(nums)
    print(nums)