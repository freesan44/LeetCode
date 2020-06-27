class Solution:
    def freqAlphabets(self, s: str) -> str:
        #寻找所有#的开头索引
        import re
        twoNumIndex = [m.start()-2 for m in re.finditer("#", s)]
        for i in twoNumIndex[::-1]:
            char = chr(96+int(s[i:i+2]))
            s = s[:i] + char + s[i+3:]
        for j in range(len(s)):
            if s[j].isdigit():
                char = chr(96 + int(s[j]))
                s = s[:j] + char + s[j+1:]
        return s


if __name__ == '__main__':
    s = "10#11#12"
    s = "1326#"
    s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"
    ret = Solution().freqAlphabets(s)
    print(ret)
