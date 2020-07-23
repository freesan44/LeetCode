class Solution:
    def maxScore(self, s: str) -> int:
        sList = list(s)
        left = 1 if sList[0]=='0' else 0
        right = sList[1:].count('1')
        index = 0
        maxNum = left + right
        while index<len(sList)-2:
            index = index + 1
            if sList[index] == '0':
                left = left + 1
            else:
                right = right - 1
            maxNum = max(maxNum, left+right)
        return maxNum


if __name__ == '__main__':
    s = "011101"
    s = "1111"
    s = "00111"
    s = "010"
    s = "00"
    result = Solution().maxScore(s)
    print(result)