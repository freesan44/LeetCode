class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        indexList = []
        for index,val in enumerate(s):
            if val == c:
                indexList.append(index)
        resList = []
        p = 0#通过指针检索当前index与下一个，跟当前字符距离哪个大，然后进位
        # print(indexList)
        for index,val in enumerate(s):
            # print(index)
            if p < len(indexList)-1 and (abs(index-indexList[p]) > abs(index-indexList[p+1])):
                p += 1
            resList.append(abs(index-indexList[p]))
        return resList
if __name__ == '__main__':
    s = "loveleetcode"
    c = "e"
    ret = Solution().shortestToChar(s,c)
    print(ret)