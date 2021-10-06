class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        from collections import defaultdict
        resDict = defaultdict(int)
        for i in nums:
            resDict[i] += 1
        res = 0
        for key,val in resDict.items():
            if val == 1:
                res += key
            # print(key,val)
        return res

if __name__ == '__main__':
    nums = [1,2,3,2]
    nums = [1, 2, 3, 4, 5]
    ret = Solution().sumOfUnique(nums)
    print(ret)