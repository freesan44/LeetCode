class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        #指针
        nLen = len(needle)
        print(needle in haystack)
        if nLen == 0: return 0
        for i in range(len(haystack)-nLen+1):
            if haystack[i:i+nLen] == needle[:]:
                return i
        return -1


if __name__ == '__main__':
    haystack = "hello"
    needle = "ll"
    ret = Solution().strStr(haystack, needle)
    print(ret)