class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        from collections import Counter
        sC = dict(Counter(s)) #通过collections组件统计字符串每个字符出现的数量
        tC = dict(Counter(t))
        for key,val in tC.items():
            if (key not in sC) or (sC[key] != val):#如果不存在对应的字符就输出
                return key
        return ""


if __name__ == '__main__':
    s = "abcd"
    t = "abcde"
    ret = Solution().findTheDifference(s, t)
    print(ret)