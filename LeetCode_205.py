class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        resDict = dict()
        for index,val in enumerate(s):
            if val in resDict:
                if resDict[val] != t[index]:
                    return False
            else:
                resDict[val] = t[index]
        resDict = dict()
        for index,val in enumerate(t):
            if val in resDict:
                if resDict[val] != s[index]:
                    return False
            else:
                resDict[val] = s[index]
        return True
if __name__ == '__main__':
    s = "egg"
    t = "add"
    s = "foo"
    t = "bar"
    s = "badc"
    t = "baba"
    ret = Solution().isIsomorphic(s,t)
    print(ret)