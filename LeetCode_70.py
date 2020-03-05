class Solution:
    def climbStairs(self, n: int) -> int:
        #动态规划 方法版
        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 2
        # if n == 0:
        #     return 0
        # return (self.climbStairs(n-1) + self.climbStairs(n-2))
        #动态规划 字典版
        dic = dict()
        dic[0] = 0
        dic[1] = 1
        dic[2] = 2
        for i in range(3, n+1):
            dic[i] = dic[i-1] + dic[i-2]
        return dic[n]

if __name__ == '__main__':
    # result = Solution().longestCommonPrefix(["a", "b"])
    result = Solution().climbStairs(35)
    print(result)


