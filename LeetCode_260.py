class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        resDic = dict()
        for i in nums:
            if i in resDic:
                del(resDic[i])
            else:
                resDic[i] = 1
        return list(resDic.keys())





if __name__ == '__main__':
    nums = [1,2,1,3,2,5]
    ret = Solution().singleNumber(nums)
    print(ret)