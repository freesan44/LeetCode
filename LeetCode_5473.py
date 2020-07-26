class Solution:
    def minFlips(self, target: str) -> int:
        targetList = list(target)
        pre = 0
        ret = 0
        for i in targetList:
            # print(int(i)^pre)
            if int(i)^pre == 1:
                ret = ret + 1
                pre = int(i)
            # print(pre)
        return ret
if __name__ == '__main__':
    target = "10111"
    result = Solution().minFlips(target)
    print(result)