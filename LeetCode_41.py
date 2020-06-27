class Solution:
    def firstMissingPositive(self, nums: [int]) -> int:
        # maxNum = 0
        # contDic = {}#用字典方式存放已存在数值，遍历为O(1)
        # for i in nums:
        #     if i > maxNum:
        #         maxNum = i
        #     contDic[i] = 1
        # for j in range(1, maxNum):
        #     if j not in contDic:
        #         return j
        # return maxNum+1
        #空间复杂度O(1) 因为最小值只存在于[1,n+1]中，中通过负号来标记值对应的index已经存在，如果[1,n]中存在正号，代表那个index未被遍历赋值，为最小值
        maxNum = len(nums)
        for i in range(maxNum):
            if nums[i] <= 0:
                nums[i] = maxNum +1
        for j in nums:
            if abs(j) <= maxNum:#把值中对应的index变为负来进行标记
                # print(j)
                nums[abs(j)-1] = -abs(nums[abs(j)-1])
        # print(nums)
        for k in range(maxNum):
            if nums[k] >=0:
                return k+1
        return maxNum+1


if __name__ == '__main__':
    nums = [1,2,0]
    # nums = []
    # nums = [3,4,-1,1]
    # nums = [7, 8, 9, 11, 12]
    ret = Solution().firstMissingPositive(nums)
    print(ret)
