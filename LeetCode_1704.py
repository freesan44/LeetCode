class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        leftStr, rightStr = s[:len(s)//2], s[len(s)//2:]
        from collections import Counter
        leftCount = Counter(leftStr)
        rightCount = Counter(rightStr)
        testDict = {
            'a':0,
            'e':0,
            'i':0,
            'o':0,
            'u':0,
            'A': 0,
            'E': 0,
            'I': 0,
            'O': 0,
            'U': 0,
        }
        # 找出字典的交集，得出元音字典，并导出数量
        leftDictList = leftCount.keys() & testDict.keys()
        leftDict = dict()
        for i in leftDictList:
            leftDict[i] = leftCount[i]
        # print(leftDict)

        rightDictList = rightCount.keys() & testDict.keys()
        rightDict = dict()
        for i in rightDictList:
            rightDict[i] = rightCount[i]
        # print(rightDict)
        return sum(leftDict.values()) == sum(rightDict.values())

if __name__ == '__main__':
    s = "textbook"
    s = "book"
    s = "AbCdEfGh"
    ret = Solution().halvesAreAlike(s)
    print(ret)