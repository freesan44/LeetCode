class Solution:
    def sortSentence(self, s: str) -> str:
        sList = s.split(" ")
        resList = [""]*len(sList)
        # 抽取每个单词的数字，并根据数值插入对应的resList
        for i in sList:
            index = int(i[-1])-1
            resList[index] = i[:-1]
        # print(resList)
        return " ".join(resList)

if __name__ == '__main__':
    s = "is2 sentence4 This1 a3"
    ret = Solution().sortSentence(s)
    print(ret)