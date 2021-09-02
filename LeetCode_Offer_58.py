class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        # res = s + s#拼接成两段，然后切片
        # return res[n:n+len(s)]
        return s[n:]+s[:n]

if __name__ == '__main__':
    s = "abcdefg"
    k = 2
    result = Solution().reverseLeftWords(s, k)
    print(result)