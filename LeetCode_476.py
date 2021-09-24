class Solution:
    def findComplement(self, num: int) -> int:
        binNum = list("{0:b}".format(num))
        res = ""
        for i in binNum:
            res += str(int(i)^1)
        return int(res,2)
if __name__ == '__main__':
    num = 5
    ret = Solution().findComplement(num)
    print(ret)