class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        i = max(nums)
        # 通过remove不用指定index来实现，然后再max就取到第二大值
        nums.remove(i)
        j = max(nums)
        return (i-1)*(j-1)

if __name__ == '__main__':
    nums = [1,5,4,5]
    ret = Solution().maxProduct(nums)
    print(ret)