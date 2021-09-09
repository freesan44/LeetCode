class Solution:
    def maxDepth(self, s: str) -> int:
        # 栈的形式来记录
        maxRet = 0
        tempCount = 0
        for i in s:
            if i == "(":
                tempCount += 1
            elif i == ")":
                if maxRet < tempCount:
                    maxRet = tempCount
                tempCount -= 1
        return maxRet



if __name__ == '__main__':
    s = "(1+(2*3)+((8)/4))+1"
    ret = Solution().maxDepth(s)
    print(ret)