class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # #排序
        # sList = list(s)
        # tList = list(t)
        # sList.sort()
        # tList.sort()
        # if sList == tList:
        #     return True
        # return False
        #remove内置函数实现
        if len(s) > len(t):
            s, t = t, s #保证s长度最短
        tList = list(t)
        for i in s:
            print(tList)
            try:
                tList.remove(i)
            except:
                return False
        if len(tList) >0:
            return False
        else:
            return True



if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    # s = "rat"
    # t = "car"
    ret = Solution().isAnagram(s, t)
    print(ret)