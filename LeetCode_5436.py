class Solution:
    def runningSum(self, nums: [int]) -> [int]:
        ret = []
        for i in range(len(nums)):
            retNum = sum(nums[:i+1])
            ret.append(retNum)
        return ret
if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    ret = Solution().runningSum(nums)
    print(ret)