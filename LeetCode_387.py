class Solution:
    def firstUniqChar(self, s: str) -> int:
        # #通过内置函数in来实现
        # sList = list(s)
        # if len(s) == 1:return 0#处理1个字符串的异常情况
        # for i in range(len(s)):
        #     if (sList[i] not in sList[i+1:]) and (sList[i] not in sList[:i]):
        #         return i
        # return -1
        # #字典实现
        # wordsList = [chr(i) for i in range(97, 97+26)]
        # valueList = [0]*26
        # wordsDic = dict(zip(wordsList, valueList))
        # sList = list(s)
        # if len(s) == 1: return 0  # 处理1个字符串的异常情况
        # for i in range(len(s)):
        #     wordsDic[sList[i]] += 1
        # for i in range(len(s)):
        #     if wordsDic[sList[i]] == 1:
        #         return i
        # return -1
        #取巧方法,左右遍历如果找到的索引是相同，代表只有一个字母
        for i in s:
            if s.find(i) == s.rfind(i):
                return s.find(i)
        return -1


if __name__ == '__main__':
    # str = "loveleetcode"
    # str = "cc"
    str = "z"
    str = ""
    str = "aadadaad"
    str = "dddccdbba"
    ret = Solution().firstUniqChar(str)
    print(ret)