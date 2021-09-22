class Solution:
    def countBits(self, n: int) -> List[int]:
        ## 暴力法
        # resList = []
        # for i in range(n+1):
        #     res = 0
        #     while i >=1:
        #         res += 1 if (i% 2 == 1) else 0
        #         i //= 2
        #     resList.append(res)
        # return resList
        # 如果i为偶数，那么是上一位i-1的1数+1
        # 如果i为奇数，那么是i/2的1数
        resList = []
        for i in range(n+1):
            res = None
            if i == 0:
                res = 0
            elif i == 1:
                res = 1
            elif i %2 == 0:#偶数
                res = resList[i//2]
            else:#奇数
                res = resList[i-1]+1
            resList.append(res)
        return resList



if __name__ == "__main__":
    n = 5
    ret = Solution().countBits(n)
    print(ret)