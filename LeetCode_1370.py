class Solution:
    def sortString(self, s: str) -> str:
        # from collections import Counter
        # sCounter = Counter(s).most_common()
        # sCounter.sort(key= lambda x:x[0])
        # print(sCounter)
        sSetList = sorted(list(set(s)))
        sList = list(s)
        resList = []
        while len(sList) != 0:
            # 先正序，后倒序
            for i in sSetList:
                if i in sList:
                    resList.append(i)
                    sList.remove(i)
            for i in sSetList[::-1]:
                if i in sList:
                    resList.append(i)
                    sList.remove(i)
        return "".join(resList)



if __name__ == '__main__':
    s = "aaaabbbbcccc"
    s = "leetcode"
    ret = Solution().sortString(s)
    print(ret)