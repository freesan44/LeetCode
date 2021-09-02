class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # # 粗暴计算法
        # res = 0
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] == nums[j]:
        #             res += 1
        # return res
        #用哈希表统计每个数在序列中出现的次数
        from collections import Counter
        numsDic = Counter(nums)
        res = 0
        for val in numsDic.values():
            res += (val*(val-1))//2
        return res

if __name__ == '__main__':
    nums = [1,2,3,1,1,3]
    ret = Solution().numIdenticalPairs(nums)
    print(ret)