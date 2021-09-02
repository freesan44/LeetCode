class Solution:
    def trailingZeroes(self, n: int) -> int:
        # ## 暴力解法
        # res = 1
        # for i in range(1,n+1):
        #     res *= i
        #     # print(res, i)
        # # print(res)
        # resStr = list(str(res))
        # resCount = 0
        # while resStr.pop() == "0":
        #     resCount += 1
        # return resCount
        #根据5因子进行除法得出
        res = 0
        while n >= 5:
            n //= 5
            res += n
        return res

if __name__ == '__main__':
    nums = 20
    result = Solution().trailingZeroes(nums)
    print(result)