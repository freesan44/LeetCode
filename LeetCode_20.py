class Solution:
    def isValid(self, s: str) -> bool:
        inList = ["(", "{", "["]
        outList = [")", "}", "]"]
        tempList = list()
        strList = list(s)
        for each in strList:
            if each in inList:
                tempList.append(each)
            elif each in outList:
                if len(tempList) <= 0:
                    return False
                lastS = tempList[-1]
                if (lastS in inList) and (inList.index(lastS) == outList.index(each)):
                    tempList.pop()
                else:
                    return False
        if len(tempList) > 0:
            return False
        return True


if __name__ == '__main__':
    # result = Solution().longestCommonPrefix(["a", "b"])
    result = Solution().isValid("([)]")
    print(result)

