class Solution:
    def moveZeroes(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # nums.sort()
        # while nums[0] == 0:
        #     nums[:-1] = nums[1:]
        #     nums[-1] = 0
        iL = len(nums)
        i = 0
        n = 0
        while i != iL:
            if nums[i] == 0:
                nums.pop(i)
                i -= 1
                iL -= 1
                n += 1
            i += 1
        for i in range(n):
            nums.append(0)


if __name__ == '__main__':
    arr = [0,1,0,3,12]
    ret = Solution().moveZeroes(arr)
    print(arr)