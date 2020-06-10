class Solution:
    def decompressRLElist(self, nums: [int]) -> [int]:
        ret = []
        countList = nums[::2]
        valueList = nums[1::2]
        for i in range(len(countList)):
            count = countList[i]
            ret += [valueList[i]]*count
        return ret

if __name__ == '__main__':
    nums = [1,2,3,4]
    # print([1]*5)
    ret = Solution().decompressRLElist(nums)
    print(ret)