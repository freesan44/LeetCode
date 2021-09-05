class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #用匿名函数，根据绝对值来排序，然后平方输出
        nums.sort(key=lambda x: abs(x))
        # print(nums)
        return [x*x for x in nums]


if __name__ == '__main__':
    nums = [-7,-3,2,3,11]
    ret = Solution().sortedSquares(nums)
    print(ret)