class Solution:
    def reverseString(self, s: [str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        #交叉替换
        # midNum = len(s)//2
        # for i in range(midNum):
        #     s[i], s[len(s)-1-i] = s[len(s)-1-i], s[i]
        #python内置函数
        s.reverse()


if __name__ == '__main__':
    # nums = [[1,2,3],[4,5,6],[7,8,9]]
    strList = ["h","e","l","l","o"]
    Solution().reverseString(strList)
    print(strList)