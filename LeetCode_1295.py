class Solution:
    def findNumbers(self, nums: [int]) -> int:
        ret = 0
        # for i in range(len(nums)):
        #     num = nums[i]
        #     tempNum = 1
        #     while num//10 != 0:
        #         num = num//10
        #         tempNum += 1
        #     if tempNum%2 == 0:
        #         ret += 1
        # return ret
        #转成字符串
        for num in nums:
            if len(str(num)) %2 == 0:
                ret += 1
        return ret

if __name__ == '__main__':
    nums = [12,345,2,6,7896]
    nums = [555, 901, 482, 1771]
    ret = Solution().findNumbers(nums)
    print(ret)