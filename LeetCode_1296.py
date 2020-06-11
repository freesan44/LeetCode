class Solution:
    def isPossibleDivide(self, nums: [int], k: int) -> bool:
        #用remove实现
        # if len(nums)%k != 0: return False
        # nums.sort()
        # while len(nums) != 0:
        #     tempNum = nums[0]
        #     for i in range(k):
        #         try:
        #             nums.remove(tempNum+i)
        #         except:
        #             return False
        # return True
        #用Counter内置函数实现
        if len(nums)%k != 0: return False
        nums.sort()
        import collections
        counter = collections.Counter(nums)
        counterNum = 0
        for num in nums:
            if counter[num] == 0:continue
            for i in range(k):
                counter[num+i] -= 1
                if counter[num+i] < 0:return False
                counterNum += 1
        if counterNum != len(nums):return False
        return True



if __name__ == '__main__':
    nums = [1,2,3,3,4,4,5,6]
    k = 4
    ret = Solution().isPossibleDivide(nums, k)
    print(ret)