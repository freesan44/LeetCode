class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # #双指针
        # sList = list(s)
        # tList = list(t)
        # if len(sList) <= 0:return True
        # if len(tList) <= 0:return False
        # sIndex = 0
        # # tIndex = 0
        # for i in tList:
        #     if i == sList[sIndex]:
        #         sIndex = sIndex + 1
        #         if sIndex == len(s):
        #             return True
        # return False
        #动态规划，对t进行预处理，形成一个二维数组，记录每个字母的下一个位置
        # t = " "+t
        sLen, tLen = len(s), len(t)
        #预处理
        dp = [[-1]*26 for _ in range(tLen+1)]
        # dp.append([-1]*26)
        for i in range(tLen-1,-1,-1):
            ordChar = ord(t[i]) - 97
            for j in range(26):
                dp[i][j] = i if j == ordChar else dp[i+1][j]
        print(dp)
        #进行搜索定位
        nextIndex = 0
        for j in s:
            ordChar = ord(j) - 97
            if dp[nextIndex][ordChar] == -1:return False
            nextIndex = dp[nextIndex][ordChar] + 1
            print("ord:{} nextindex:{}".format(ordChar, nextIndex))
        return True
if __name__ == '__main__':
    # s = "abc"
    # s = "ahb"
    s = "hbg"
    t = "ahbgdc"
    # s = "axc"
    # t = "ahbgdc"
    # s = ""
    # t = "ahbgdc"
    # s = "aaaaaa"
    # t = "bbaaaa"
    result = Solution().isSubsequence(s, t)
    print(result)