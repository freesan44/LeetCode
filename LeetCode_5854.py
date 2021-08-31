class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        resArr : list = []
        for i in range(len(nums)-k+1):
            each = nums[i:i+k] #把最接近差值的数组抽取出来
            res = each[-1] - each[0] #最大值与最小值差值
            resArr.append(res)
        return min(resArr)

if __name__ == '__main__':
    # nums = [9,4,1,7]
    # k = 2
    nums = [90]
    k = 1
    result = Solution().minimumDifference(nums, k)
    print(result)