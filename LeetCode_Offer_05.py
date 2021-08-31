class Solution:
    def replaceSpace(self, s: str) -> str:
        # 简单做法
        return s.replace(" ", "%20")
        # # 正规做法
        # newS = ""
        # for i in s :
        #     if i != " ":
        #         newS += i
        #     else:
        #         newS += "%20"
        # return newS

if __name__ == '__main__':
    s = "We are happy."
    result = Solution().replaceSpace(s)
    print(result)