class Solution:
    def minOperations(self, n: int) -> int:
        average = n
        maxNum = (n-1)*2+1
        res = 0
        # print(average, maxNum)
        while maxNum > average:
            res += maxNum - average
            maxNum -= 2
        return res


if __name__ == '__main__':
    n = 6
    ret = Solution().minOperations(n)
    print(ret)