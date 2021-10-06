class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        sList = list(s)
        resList = []
        for i in sList:
            if i == ")" and len(resList)>0 and resList[-1]=="(":
                resList.pop()
            else:
                resList.append(i)
        return len(resList)

if __name__ == '__main__':
    s = "()))(("
    s = "()"
    s = "())"
    ret = Solution().minAddToMakeValid(s)
    print(ret)