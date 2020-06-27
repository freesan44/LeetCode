class Solution:
    def findTargetSumWays(self, nums: [int], S: int) -> int:
        # #递归 超时
        # if len(nums) == 1:
        #     if (nums[0] == S) or (-nums[0] == S):
        #         return 1
        #     else:
        #         return 0
        # if len(nums) == 2:
        #     ret = 0
        #     if (nums[0] + nums[1]) == S:
        #         ret = ret + 1
        #     if (nums[0] - nums[1]) == S:
        #         ret = ret + 1
        #     if (-nums[0] + nums[1]) == S:
        #         ret = ret + 1
        #     if (-nums[0] - nums[1]) == S:
        #         ret = ret + 1
        #     return ret
        # ret = self.findTargetSumWays(nums[:-1], S + nums[-1]) + self.findTargetSumWays(nums[:-1], S - nums[-1])
        # return ret
        #动态规划 背包问题，f[i] = f[i-1]+f[i+1]
        dataList = [{}for j in range(len(nums)+1)]#建立数据结构存储S对应的答案
        return self.findTargetSumWaysCore(nums, S, dataList)

    def findTargetSumWaysCore(self, nums: [int], S: int, dataList:[int]) -> int:
        SDict = dataList[len(nums)]
        SStr = str(S)
        if SStr in SDict:
            # print("{} {} {}".format(nums,S, dataList[len(nums)][S]))
            return SDict[SStr]
        else:
            if len(nums) == 1:
                if (nums[0] == S) or (-nums[0] == S):
                    dataList[len(nums)][SStr] = 1
                    return 1
                else:
                    return 0
            if len(nums) == 2:
                ret = 0
                if (nums[0] + nums[1]) == S:
                    ret = ret + 1
                if (nums[0] - nums[1]) == S:
                    ret = ret + 1
                if (-nums[0] + nums[1]) == S:
                    ret = ret + 1
                if (-nums[0] - nums[1]) == S:
                    ret = ret + 1
                dataList[len(nums)][SStr] = ret
                return ret
            ret = self.findTargetSumWaysCore(nums[:-1], S + nums[-1], dataList) + self.findTargetSumWaysCore(nums[:-1], S - nums[-1], dataList)
            dataList[len(nums)][SStr] = ret
            return ret

if __name__ == '__main__':
    # nums = [1, 1, 1, 1, 1]
    # S = 3
    # nums = [1]
    # S = 1
    # nums = [1, 0]
    # S = 1
    nums = [47, 23, 35, 27, 30, 42, 26, 42, 30, 6, 8, 48, 44, 38, 41, 50, 18, 19, 19, 5]
    S = 40
    ret = Solution().findTargetSumWays(nums, S)
    print(ret)
