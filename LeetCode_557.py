class Solution:
    def reverseWords(self, s: str) -> str:
        sArr = s.split()
        for index, val in enumerate(sArr): #带index方式的遍历
            # print(index)
            sArr[index] = val[::-1] #用切片方式翻转单词
        return " ".join(sArr) #用空格隔开来输出字符串



if __name__ == '__main__':
    s = "Let's take LeetCode contest"
    ret = Solution().reverseWords(s)
    print(ret)