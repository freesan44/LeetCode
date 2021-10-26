class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # #线性时间 线性空间
        # from collections import Counter
        # counter = Counter(nums)
        # for i in range(len(nums)+1):
        #     if i not in counter:
        #         return i
        # return -1
        #线性时间 常数空间 高斯求和公式
        length = len(nums)
        gaosuSum = (length*(length+1))//2
        numsSum = sum(nums)
        return gaosuSum-numsSum




if __name__ == '__main__':
    nums = [3,0,1]
    ret = Solution().missingNumber(nums)
    print(ret)