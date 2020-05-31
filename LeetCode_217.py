class Solution:
    def containsDuplicate(self, nums: [int]) -> bool:
        #元组实现
        # return len(nums) != len(set(nums))
        #传统处理 计算时间过长，弃置
        # for i in range(0,len(nums)):
        #     if nums[i] in nums[i+1:]:
        #         return True
        # return  False
        #排序比较
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False

if __name__ == '__main__':
    # nums = [1,2,3,4,5,6,7]
    nums = [1,2,3,1]
    res = Solution().containsDuplicate(nums)
    print(res)