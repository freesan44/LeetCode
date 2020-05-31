class Solution:
    def rotate(self, nums: [int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # #数组段切换
        # lenN = len(nums)
        # k = k % len(nums)#防止超界
        # nums[:k], nums[k:] = nums[lenN-k:], nums[:lenN-k]
        #颠倒数组
        nums.reverse()
        for i in range(0,k):
            nums.append(nums.pop(0))
        nums.reverse()


if __name__ == '__main__':
    nums = [1,2,3,4,5,6,7]
    # nums = [1,2,3,4,5]
    k = 3
    res = Solution().rotate(nums,k)
    # nums = nums[2:]
    print(nums)